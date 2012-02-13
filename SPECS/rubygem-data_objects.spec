# Generated from data_objects-0.10.8.gem by gem2rpm -*- rpm-spec -*-
%global gemname data_objects

%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}
%global rubyabi 1.8

Summary: DataObjects basic API and shared driver specifications
Name: rubygem-%{gemname}
Version: 0.10.8
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/datamapper/do
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: ruby 
Requires: rubygem(addressable) => 2.1
Requires: rubygem(addressable) < 3
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems) 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Provide a standard and simplified API for communicating with RDBMS from Ruby


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
%{geminstdir}/spec
%{geminstdir}/tasks
%{geminstdir}/LICENSE
%{geminstdir}/Rakefile
%{geminstdir}/ChangeLog.markdown
%exclude %{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/README.markdown


%changelog
* Mon Feb 13 2012 Fotios Lindiakos <fotios@redhat.com> - 0.10.8-1
- Initial package
