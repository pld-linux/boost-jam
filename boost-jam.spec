Summary:	Boost Jam - build tool
Summary(pl):	Boost Jam - narzêdzie do budowania
Name:		boost-jam
Version:	3.1.4
Release:	2
License:	GPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/boost/%{name}-%{version}.tgz
# Source0-md5:	a927ff55c830d91d27d113182e0cf043
URL:		http://www.boost.org/
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Jam.html Jambase.html Jamfile.html RELNOTES
%attr(755,root,root) %{_bindir}/*
