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

It then dumps a hash like:

    --- 
    :rubygem: 
    - barista
    - minitest
    - flexmock
    - rake
    - rspec
    :ruby: 
    - rdoc
    - rr
    :none: 
    - execjs
    - coffee-script-source
    - coffee-script
    - jeweler
    - multi_json
    - session
    - mustang
    - simplecov
    - therubyracer
    - johnson
    - therubyrhino
