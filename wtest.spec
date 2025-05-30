Name:           wtest
Version:        0.0.1
Release:        1%{?dist}
Summary:        A wtest program.

License:        MIT
URL:            https://google.com
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  make,gcc

%description
A wtest program.

%prep
#%setup -q
#mkdir $RPM_BUILD_ROOT

%build
#make
#%configure
%make_build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp %{name} $RPM_BUILD_ROOT/%{_bindir}

%files
%{_bindir}/%{name}

%changelog
* Fri May 30 2025 Wertík <jregvx@gmail.com>
- First and possibly the last version.
