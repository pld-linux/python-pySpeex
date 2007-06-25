#
%define		mod_name	pySpeex
#
Summary:	Python bindings to the Speex audio codec library
Summary(pl.UTF-8):	Wiązania języka Python do biblioteki kodeka audio Speex
Name:		python-pySpeex
Version:	0.2
Release:	0.1
License:	LGPL
Group:		Libraries/Python
Source0:	http://www.freenet.org.nz/python/pySpeex/%{mod_name}-%{version}.tar.gz
# Source0-md5:  5f6837cd74568fb58bb15d43fe2406ea
URL:		http://www.freenet.org.nz/python/pySpeex/
BuildRequires:	python-devel
BuildRequires:	python-Pyrex
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	speex-devel
%pyrequires_eq	python-modules
Requires:	speex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pySpeex is a Python interface to the Speex audio compressor/decompressor
(codec) library. With pySpeex, you can easily create an audio stream object
(of class 'speex'), and incrementally encode and decode speech audio data
with the 'encode' and 'decode' methods.

%description -l pl.UTF-8
pySpeex jest interfejsem dla języka Python do biblioteki kodera/dekodera
(kodek) Speex. Używając pySpeex można łatwo tworzyć obiekty strumieni
audio (klasy 'speex') i enkodować oraz dekodować dane zakodowane tym kodekiem
w sposób przyrostowy przy użyciu metod 'encode' i 'decode'.

%prep
%setup -q -n %{mod_name}-%{version}

%build
find -type f -exec sed -i -e 's|#!.*python.*|#!%{_bindir}/python|g' "{}" ";"
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

python setup.py install --optimize=2 --root=$RPM_BUILD_ROOT
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%doc doc
%{py_sitedir}/*.so
