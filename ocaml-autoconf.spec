Name:           ocaml-autoconf
Version:        1.0
Release:        %mkrel 1
Summary:        Autoconf macros for OCaml
Group:          Development/Other
# https://fedoraproject.org/wiki/Licensing/BSD#3ClauseBSD
License:        BSD
URL:            http://forge.ocamlcore.org/projects/ocaml-autoconf/
Source0:        https://forge.ocamlcore.org/frs/download.php/181/ocaml-autoconf-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  perl
# Runtime requires /usr/share/aclocal subdirectory.
Requires:       automake

%description
Autoconf macros for OCaml.

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make install \
  prefix=%{_prefix} \
  datadir=%{_datadir} \
  mandir=%{_mandir} \
  DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README LICENSE
%{_mandir}/man1/*.1*
%{_datadir}/aclocal/ocaml.m4

