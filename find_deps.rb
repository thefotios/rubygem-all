#!ruby

require 'yaml'
require 'rubygems'
require 'thread'
require 'progressbar'
require 'optparse'

# Parse options
options = {
  :builddir => '~/builddir'
}
OptionParser.new do |opts|

  opts.banner = "Usage: find_deps.rb [options] gem_name [gem_name ...]"

  opts.on("-v", "--verbose", "Run verbosely") do |v|
    options[:verbose] = v
  end

  opts.on("-f", "--fetch", "Fetch missing gems") do |f|
    options[:fetch] = f
  end

  opts.on("-b", "--builddir BUILDDIR", "RPM build envorinment (default is: #{options[:builddir]})") do |b|
    options[:builddir] = b
  end

  opts.on("-d", "--dev", "Also check development dependencies") do |f|
    options[:dev] = f
  end

  opts.separator ""
  opts.separator "Common options:"

  #No argument, shows at tail.  This will print an options summary.
  # Try it and see!
  opts.on_tail("-h", "--help", "Show this message") do
    puts opts
    exit
  end
end.parse!(ARGV)

@options = options

@mutex = Mutex.new
@yum = {
  :rubygem => [],
  :ruby => [],
  :none => [],
  :dependencies => {}
}
deps = []
threads = []

def find_deps(deps, name) 
  deps << name
  gem = Gem.searcher.find(name)

  if gem 
    my_deps = gem.dependencies.collect{|x| 
      x.name if (@options[:dev] || x.type == :runtime)
    }.compact

    @yum[:dependencies][name] = my_deps

    my_deps.each { |x|
      unless deps.include?(x)
        find_deps(deps, x)
      end
    }
  end

  deps
end

def add_to_hash(location,name)
  @mutex.synchronize do
    @yum[ location ] << name
    @pbar.inc
  end
end

def search(prefix,name)
  combined = "#{prefix}-#{name}"
  regex = Regexp.compile("^#{combined}\.",Regexp::MULTILINE)
  !(regex.match(`yum search -q --disablerepo=li #{combined} 2> /dev/null`).nil?)
end

# Find all of the dependencies
# These print to STDERR so that the YAML dumped to STDOUT can be piped
STDERR.print "Checking dependencies for #{ARGV.join(', ')}..."
ARGV.each do |gem|
  find_deps(deps, gem)
end
STDERR.puts "found #{deps.length}"

# Create progress bar
@pbar = ProgressBar.new('Checking yum',deps.length)
for gem in deps
  threads << Thread.new(gem) do |mygem|

    if search('rubygem',mygem)
      add_to_hash(:rubygem,mygem)
    elsif search('ruby',mygem)
      add_to_hash(:ruby,mygem)
    else
      add_to_hash(:none,mygem)
    end

  end
end

threads.each{|t| t.join }
@pbar.finish

# Remove any gems that don't have any dependencies
[@yum,@yum[:dependencies]].each{|a| a.delete_if{|k,v| v.nil? || v.empty?}}

# Prefix the dependency name with the name it has in YUM
@yum[:dependencies ] = @yum[:dependencies].map do |name,deps|
  {
    name => deps.map{|dep|
      prefix = '???'
      %w(rubygem ruby).each do |p|
        p = p.to_sym
        if @yum[p] && @yum[p].include?(dep)
          prefix = p
        end
      end
      "#{prefix}-#{dep}"
    }.sort
  }
end
puts YAML.dump @yum 
