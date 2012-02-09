# Generated from dm-transactions-1.2.0.gem by gem2rpm -*- rpm-spec -*-
%global gemname dm-transactions

%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}
%global rubyabi 1.8

Summary: Adds transaction support to datamapper
Name: rubygem-%{gemname}
Version: 1.2.0
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/datamapper/dm-transactions
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: ruby 
Requires: rubygem(dm-core) => 1.2.0
Requires: rubygem(dm-core) < 1.3
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems) 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Makes transaction support available for adapters that support them


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
%{geminstdir}/Gemfile
%{geminstdir}/Rakefile
%{geminstdir}/VERSION
%{geminstdir}/%{gemname}.gemspec
%{geminstdir}/tasks
%{geminstdir}/spec
%exclude %{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/README.rdoc
%doc %{geminstdir}/.document


%changelog
* Thu Feb 09 2012 Fotios Lindiakos <fotios@redhat.com> - 1.2.0-1
- Initial package
