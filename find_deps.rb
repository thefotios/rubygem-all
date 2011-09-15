#!ruby

require 'yaml'
require 'rubygems'
require 'thread'
require 'progressbar'

@mutex = Mutex.new
@yum = {
  :rubygem => [],
  :ruby => [],
  :none => []
}
deps = []
@regex = /.*N\/S Matched.*/
threads = []

def find_deps(deps, name) 
  deps << name
  gem = Gem.searcher.find(name)
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
print "Checking dependencies..."
find_deps(deps, ARGV[0])
puts "found #{deps.length}"

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
puts YAML.dump @yum 
