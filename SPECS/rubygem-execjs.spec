# Generated from execjs-1.3.0.gem by gem2rpm -*- rpm-spec -*-
%global gemname execjs

%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}
%global rubyabi 1.9.1

Summary: Run JavaScript code from Ruby
Name: rubygem-%{gemname}
Version: 1.3.0
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/sstephenson/execjs
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
Source1: %{name}-%{version}-test.tgz
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: ruby 
Requires: rubygem(multi_json) => 1.0
Requires: rubygem(multi_json) < 2
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems) 
BuildRequires: ruby 
BuildRequires: rubygem(minitest)
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
ExecJS lets you run JavaScript code from Ruby.


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

# Got the tests using the following
# git clone https://github.com/sstephenson/execjs.git && cd execjs
# git checkout v1.3.0
# tar czf rubygem-execjs-1.3.0-test.tgz test/
%check
pushd .%{geminstdir}
tar xzf %{SOURCE1}
testrb -Ilib test
popd

%build

%install
mkdir -p %{buildroot}%{gemdir}
cp -a .%{gemdir}/* \
        %{buildroot}%{gemdir}/


%files
%dir %{geminstdir}
%{geminstdir}/lib
%{geminstdir}/LICENSE
%exclude %{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/README.md


%changelog
* Tue Feb 28 2012 Fotios Lindiakos <fotios@redhat.com> - 1.3.0-1
- Initial package
