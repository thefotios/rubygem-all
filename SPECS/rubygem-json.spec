# Generated from json-1.6.5.gem by gem2rpm -*- rpm-spec -*-
%global gemname json

%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}
%global rubyabi 1.8

Summary: JSON Implementation for Ruby
Name: rubygem-%{gemname}
Version: 1.6.5
Release: 1%{?dist}
Group: Development/Languages
License: Ruby
URL: http://flori.github.com/json
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: ruby 
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems) 
BuildRequires: ruby 
Provides: rubygem(%{gemname}) = %{version}

%description
This is a JSON implementation as a Ruby extension in C.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{gemdir}
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
gem install --local --install-dir .%{gemdir} \
            -V \
            --force %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gemdir}
cp -a .%{gemdir}/* \
        %{buildroot}%{gemdir}/

# Remove the binary extension sources and build leftovers.
rm -rf %{buildroot}%{geminstdir}/ext

%files
%dir %{geminstdir}
%{geminstdir}/lib
%{geminstdir}/benchmarks
%{geminstdir}/tests
%{geminstdir}/tools
%{geminstdir}/java
%{geminstdir}/data
%{geminstdir}/diagrams

%{geminstdir}/.gitignore
%{geminstdir}/.travis.yml
%{geminstdir}/CHANGES
%{geminstdir}/GPL
%{geminstdir}/Gemfile
%{geminstdir}/COPYING
%{geminstdir}/COPYING-json-jruby
%{geminstdir}/Rakefile
%{geminstdir}/TODO
%{geminstdir}/VERSION
%{geminstdir}/install.rb
%exclude %{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec
%{geminstdir}/json.gemspec
%{geminstdir}/json-java.gemspec
%{geminstdir}/json_pure.gemspec

%files doc
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/README.rdoc
%doc %{geminstdir}/README-json-jruby.markdown


%changelog
* Mon Feb 13 2012 Fotios Lindiakos <fotios@redhat.com> - 1.6.5-1
- Initial package
