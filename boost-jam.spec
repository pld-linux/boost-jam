Name:		boost-jam
Version:	3.1.4
Summary:	Build tool
Summary(pl):	Narzêdzie budowania
Release:	2
Source0:	http://dl.sourceforge.net/boost/%{name}-%{version}.tgz
# Source0-md5:	a927ff55c830d91d27d113182e0cf043
License:	GPL
Group:		Development/Tools
URL:		http://www.boost.org
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
%setup -q -n %{name}-%{version}

%build
LOCATE_TARGET=bin ./build.sh $BOOST_JAM_TOOLSET

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -m 755 bin/bjam $RPM_BUILD_ROOT%{_bindir}/bjam-%{version}
ln -sf bjam-%{version} $RPM_BUILD_ROOT%{_bindir}/bjam
ln -sf bjam-%{version} $RPM_BUILD_ROOT%{_bindir}/jam
install Jam.html Jambase.html Jamfile.html RELNOTES $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

find $RPM_BUILD_ROOT -name CVS -type d -depth -exec rm -r {} \;

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc %{_docdir}/%{name}-%{version}


%clean
rm -rf $RPM_BUILD_ROOT
