#
%define		mod_name	pySpeex
#
Summary:	Python bindings to the Speex audio codec library
Summary(pl.UTF-8):	Wiązania języka Python do biblioteki kodeka dźwięku Speex
Name:		python-pySpeex
Version:	0.2
Release:	0.1
License:	LGPL
Group:		Libraries/Python
Source0:	http://www.freenet.org.nz/python/pySpeex/%{mod_name}-%{version}.tar.gz
# Source0-md5:  5f6837cd74568fb58bb15d43fe2406ea
Patch0:		%{name}-fix.patch
URL:		http://www.freenet.org.nz/python/pySpeex/
BuildRequires:	python-Pyrex
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	speex-devel >= 1:1.1.5
%pyrequires_eq	python-modules
Requires:	speex >= 1:1.1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pySpeex is a Python interface to the Speex audio
compressor/decompressor (codec) library. With pySpeex, you can easily
create an audio stream object (of class 'speex'), and incrementally
encode and decode speech audio data with the 'encode' and 'decode'
methods.

%description -l pl.UTF-8
pySpeex jest interfejsem języka Python do biblioteki kodera/dekodera
(kodeka) Speex. Używając pySpeex można łatwo tworzyć obiekty strumieni
dźwięku (klasy 'speex') i kodować oraz dekodować dane zakodowane tym
kodekiem w sposób przyrostowy przy użyciu metod 'encode' i 'decode'.

%prep
%setup -q -n %{mod_name}-%{version}
%patch0 -p1

find -type f -exec sed -i -e 's|#!.*python.*|#!%{_bindir}/python|g' "{}" ";"

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%py_install
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/speex-*.egg-info
