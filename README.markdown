# makerpm.sh
## What it does
This function generates the appropriate spec files and runs rpmbuild. 
In the process, it opens vim to let you edit your spec file. In there, you should run: `rpmbuild -ba %` so that you can make sure the build will succeed (for instance making sure you have included all files.

## Usage
    bash makerpm.sh [gem_name]


# find_deps.rb
## What it does
This script allows use to recursively check all dependencies of a gem.

It then checks yum for those dependencies.

Right now, it looks for:

 * rubygem-
 * ruby-

## Usage

**fetch and builddir are not implemented yet**

    [fotios@fotios rubygem-all]$ ruby find_deps.rb -h
    Usage: find_deps.rb [options] gem_name [gem_name ...]
      -v, --verbose                    Run verbosely
      -f, --fetch                      Fetch missing gems
      -b, --builddir BUILDDIR          RPM build envorinment (default is: ~/builddir)
      -d, --dev                        Also check development dependencies

    Common options:
      -h, --help                       Show this message


## The output

Note that the output is a valid YAML doc. I just split it up here so that I could describe it inline.

**A list of the gems and whether they were found and what their prefix was**

    --- 
    :rubygem: 
    - flexmock
    - minitest
    - rake
    - rspec
    :ruby: 
    - rdoc
    :none: 
    - multi_json
    - rr
    - therubyrhino
    - coffee-script
    - barista
    - execjs
    - coffee-script-source
    - johnson
    - simplecov
    - therubyracer
    - jeweler
    - session
    - mustang

**This next part of the hash lists any gems that had dependencies and what their package name is (if it exists already)**

    :dependencies: 
    - rake: 
      - ???-session
      - rubygem-flexmock
      - rubygem-minitest
    - coffee-script: 
      - ???-coffee-script-source
      - ???-execjs
    - barista: 
      - ???-coffee-script
      - ???-jeweler
      - ???-rr
      - rubygem-rspec
    - execjs: 
      - ???-johnson
      - ???-multi_json
      - ???-mustang
      - ???-therubyracer
      - ???-therubyrhino
      - rubygem-rake
    - multi_json: 
      - ???-simplecov
      - ruby-rdoc
      - rubygem-rake
      - rubygem-rspec
