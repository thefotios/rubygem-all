# Generated from coffee-script-source-1.2.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name coffee-script-source

%global rubyabi 1.9.1

Summary:        The CoffeeScript Compiler
Name:           rubygem-%{gem_name}
Version:        1.2.0
Release:        2%{?dist}
Group:          Development/Languages
License:        MIT
URL:            http://jashkenas.github.com/coffee-script/
Source0:        http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires:       ruby(abi) = %{rubyabi}
Requires:       ruby(rubygems) 
Requires:       ruby 
BuildRequires:  ruby(abi) = %{rubyabi}
BuildRequires:  rubygems-devel
BuildRequires:  ruby 
BuildArch:      noarch
Provides:       rubygem(%{gem_name}) = %{version}

%description
CoffeeScript is a little language that compiles into JavaScript.
Underneath all of those embarrassing braces and semicolons,
JavaScript has always had a gorgeous object model at its heart.
CoffeeScript is an attempt to expose the good parts of JavaScript
in a simple way.


%package doc
Summary:    Documentation for %{name}
Group:      Documentation
Requires:   %{name} = %{version}-%{release}
BuildArch:  noarch

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}


%changelog
* Wed Feb 29 2012 Fotios Lindiakos <fotios@redhat.com> - 1.2.0-2
- Rebuilt with new gem_* macros

* Mon Feb 27 2012 Fotios Lindiakos <fotios@redhat.com> - 1.2.0-1
- Initial package
