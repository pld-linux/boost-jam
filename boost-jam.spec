Summary:	Boost Jam - build tool
Summary(pl):	Boost Jam - narzêdzie do budowania
Name:		boost-jam
Version:	3.1.13
Release:	1
License:	BSD-like
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/boost/%{name}-%{version}.tgz
# Source0-md5:	81f5ab23de817444f66dc3edf35d5ef5
URL:		http://www.boost.org/
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-utils
BuildRequires:	perl-base
BuildRequires:	sgml-tools
Provides:	jam
Obsoletes:	jam
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Boost Jam is a build tool based on FTJam, which in turn is based on
Perforce Jam. It contains significant improvements made to facilitate
its use in the Boost Build System, but should be backward compatible
with Perforce Jam.

%description -l pl
Boost Jam jest narzêdziem s³u¿±cym do budowania, opartym o FTJam,
który jest dla odmiany oparty na Perforce Jam. Zawiera znacz±ce
usprawnienia wprowadzone dla u³atwienia u¿ycia w Boost Build System,
ale powinien byæ wstecznie kompatybilny z Perforce Jam.

%prep
%setup -q

%{__perl} -pi -e 's/-s -O /%{rpmldflags} /' build.jam

%build
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
LOCATE_TARGET=bin \
./build.sh cc -d2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install bin/bjam $RPM_BUILD_ROOT%{_bindir}/bjam-%{version}
ln -sf bjam-%{version} $RPM_BUILD_ROOT%{_bindir}/bjam
ln -sf bjam-%{version} $RPM_BUILD_ROOT%{_bindir}/jam

cd debian
db2man jam.man.sgml
install -D JAM.1 $RPM_BUILD_ROOT%{_mandir}/man1/bjam.1
echo '.so bjam.1' > $RPM_BUILD_ROOT%{_mandir}/man1/jam.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc jam LICENSE_1_0.txt index.html images boost.png boostbook.css
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*jam.1*
