Name:           ocaml-autoconf
Version:        1.1
Release:        2
Summary:        Autoconf macros for OCaml
Group:          Development/Other
# https://fedoraproject.org/wiki/Licensing/BSD#3ClauseBSD
License:        BSD
URL:            https://forge.ocamlcore.org/projects/ocaml-autoconf/
Source0:        https://forge.ocamlcore.org/frs/download.php/181/ocaml-autoconf-%{version}.tar.gz
# Runtime requires /usr/share/aclocal subdirectory.
Requires:       automake
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

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



%changelog
* Mon Jan 25 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.1-1mdv2010.1
+ Revision: 496356
- new version

* Thu Aug 13 2009 Florent Monnier <blue_prawn@mandriva.org> 1.0-1mdv2010.0
+ Revision: 415810
- buildrequires perl
- perldoc path
- imported from fedora's spec file by Richard Jones

