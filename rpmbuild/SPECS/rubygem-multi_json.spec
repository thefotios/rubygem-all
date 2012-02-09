# Generated from multi_json-1.0.3.gem by gem2rpm -*- rpm-spec -*-
%global gemname multi_json

%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}
%global rubyabi 1.8

Summary: A gem to provide swappable JSON backends
Name: rubygem-%{gemname}
Version: 1.0.3
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/intridea/multi_json
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) >= 1.3.6
Requires: ruby 
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems) >= 1.3.6
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
A gem to provide swappable JSON backends utilizing Yajl::Ruby, the JSON gem,
JSON pure, or a vendored version of okjson.


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
%{geminstdir}
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/LICENSE.md
%doc %{geminstdir}/README.md


%changelog
* Thu Sep 15 2011 Fotios Lindiakos (fotios at redhat.com) - 1.0.3-1
- Initial package
