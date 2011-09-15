#!ruby

require 'yaml'
require 'rubygems'
require 'thread'
require 'progressbar'

@mutex = Mutex.new
@yum = {
  :rubygem => [],
  :ruby => [],
  :none => [],
  :dependencies => {}
}
deps = []
@regex = /.*N\/S Matched.*/
threads = []

def find_deps(deps, name) 
  deps << name
  gem = Gem.searcher.find(name)

  @yum[:dependencies][name] = gem ? gem.dependencies.collect{|x| x.name} : nil

  if ( gem && gem.dependencies ) 
    gem.dependencies.each do |x| 
      unless deps.include?(x.name)
        find_deps(deps, x.name)
      end
    end
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
  !(@regex.match(`yum search -q #{prefix}-#{name} 2> /dev/null`).nil?)
end

# Find all of the dependencies
# These print to STDERR so that the YAML dumped to STDOUT can be piped
STDERR.print "Checking dependencies..."
find_deps(deps, ARGV[0])
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
@yum[:dependencies].delete_if{|k,v| v.nil?}

# Prefix the depencie name with the name it has in YUM
@yum[:dependencies ] = @yum[:dependencies].map do |name,deps|
  {
    name => deps.map{|dep|
      (case
      when @yum[:rubygem].include?(dep)
        "rubygem-"
      when @yum[:ruby].include?(dep)
        "ruby-"
      else
        "???-"
      end) + dep
    }.sort
  }
end
puts YAML.dump @yum 
