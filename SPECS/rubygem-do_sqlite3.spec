# Generated from do_sqlite3-0.10.8.gem by gem2rpm -*- rpm-spec -*-
%global gemname do_sqlite3

%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}
%global rubyabi 1.8

Summary: DataObjects Sqlite3 Driver
Name: rubygem-%{gemname}
Version: 0.10.8
Release: 1%{?dist}
Group: Development/Languages
License: MIT
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: ruby 
Requires: rubygem(data_objects) = 0.10.8
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems) 
BuildRequires: ruby 
Provides: rubygem(%{gemname}) = %{version}

%description
Implements the DataObjects API for Sqlite3


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
%{geminstdir}/tasks
%{geminstdir}/Rakefile
%exclude %{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/ChangeLog.markdown
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/README.markdown


%changelog
* Mon Feb 13 2012 Fotios Lindiakos <fotios@redhat.com> - 0.10.8-1
- Initial package
