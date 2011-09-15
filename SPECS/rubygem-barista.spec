# Generated from barista-1.2.1.gem by gem2rpm -*- rpm-spec -*-
%global gemname barista

%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}
%global rubyabi 1.8

Summary: Simple, transparent coffeescript integration for Rails and Rack applications
Name: rubygem-%{gemname}
Version: 1.2.1
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/Sutto/barista
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: ruby 
Requires: rubygem(coffee-script) => 2.2
Requires: rubygem(coffee-script) < 3
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems) 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Barista provides simple, integrated support for CoffeeScript in Rack and Rails
applications.
Much like Compass does for Sass, It also provides Frameworks (bundleable code
which can be shared via Gems).
Lastly, it also provides a Rack Application (which can be used to server
compiled code), a around_filter-style precompiler (as Rack middleware) and
simple helpers for rails and Haml.
For more details, please see the the README file bundled with it.


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
gem install --local --install-dir .%{gemdir} \
            --force %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gemdir}
cp -a .%{gemdir}/* \
        %{buildroot}%{gemdir}/


%files
%dir %{geminstdir}
%{geminstdir}/lib
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/README.md


%changelog
* Thu Sep 15 2011 Fotios Lindiakos (fotios at redhat.com) - 1.2.1-1
- Initial package
