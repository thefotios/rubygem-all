# Generated from json-1.4.6.gem by gem2rpm -*- rpm-spec -*-
%global gemname json

%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}
%global rubyabi 1.8

Summary: JSON Implementation for Ruby
Name: rubygem-%{gemname}
Version: 1.4.6
Release: 1%{?dist}
Group: Development/Languages
License: Ruby
URL: http://flori.github.com/json
Source0: %{gemname}-%{version}.gem
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
            --bindir .%{_bindir} \
            -V \
            --force %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gemdir}
cp -a .%{gemdir}/* \
        %{buildroot}%{gemdir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{geminstdir}/bin -type f | xargs chmod a+x
# Remove the binary extension sources and build leftovers.
rm -rf %{buildroot}%{geminstdir}/ext

%files
%dir %{geminstdir}
%{_bindir}/edit_json.rb
%{_bindir}/prettify_json.rb
%{geminstdir}/bin
%{geminstdir}/lib

%{geminstdir}/benchmarks
%{geminstdir}/tests
%{geminstdir}/tools
%{geminstdir}/data

%{geminstdir}/CHANGES
%{geminstdir}/GPL
%{geminstdir}/COPYING
%{geminstdir}/Rakefile
%{geminstdir}/TODO
%{geminstdir}/VERSION
%{geminstdir}/install.rb

%exclude %{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/README


%changelog
* Mon Feb 13 2012 Fotios Lindiakos <fotios@redhat.com> - 1.4.6-1
- Initial package
