# Directions saved here for posterity

I am assuming you have the necessary build tools installed (if not, yum install rpmdevtools) and have already created an RPM build environment, eg:

    ~/rpmbuild
     |-- BUILD
     |-- RPMS
     |-- SOURCES
     |-- SPECS
     `-- SRPMS

First, make sure gem2rpm is installed:

    yum install rubygem-gem2rpm

Then, grab the gem you want to convert to an RPM:

    cd ~/rpmbuild/SOURCES
    gem fetch capistrano

This will dump the gem file in the current directory, in this case: capistrano-2.5.14.gem.

Next, create a spec file:

    gem2rpm capistrano-2.5.14.gem  > ../SPECS/rubygem-capistrano.spec

Finally, build the RPM(s):

    rpmbuild -ba ../SPECS/rubygem-capistrano.spec


[Originally found here](http://yo61.com/building-rpms-from-ruby-gems.html)

# Using find_deps.rb
This script allows use to recursively check all dependencies of a gem.

It then checks yum for those dependencies.

Right now, it looks for:

 * rubygem-
 * ruby-

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
