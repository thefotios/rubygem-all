# Generated from bcrypt-ruby-3.0.1.gem by gem2rpm -*- rpm-spec -*-
%global gemname bcrypt-ruby

%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}
%global rubyabi 1.8

Summary: OpenBSD's bcrypt() password hashing algorithm
Name: rubygem-%{gemname}
Version: 3.0.1
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://bcrypt-ruby.rubyforge.org
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: ruby 
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems) 
BuildRequires: ruby 
Provides: rubygem(%{gemname}) = %{version}

%description
bcrypt() is a sophisticated and secure hash algorithm designed by The
OpenBSD project
for hashing passwords. bcrypt-ruby provides a simple, humane wrapper for
safely handling
passwords.


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
%{geminstdir}/spec
%{geminstdir}/Gemfile
%{geminstdir}/Gemfile.lock
%{geminstdir}/.gitignore
%{geminstdir}/.rspec
%{geminstdir}/Rakefile
%exclude %{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec
%{geminstdir}/%{gemname}.gemspec

%files doc
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/README.md
%doc %{geminstdir}/COPYING
%doc %{geminstdir}/CHANGELOG
%doc %{geminstdir}/lib/bcrypt.rb
%doc %{geminstdir}/lib/bcrypt_engine.rb


%changelog
* Mon Feb 13 2012 Fotios Lindiakos <fotios@redhat.com> - 3.0.1-1
- Initial package
