#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-future
Version  : 0.18.2
Release  : 51
URL      : https://files.pythonhosted.org/packages/45/0b/38b06fd9b92dc2b68d58b75f900e97884c45bedd2ff83203d933cf5851c9/future-0.18.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/45/0b/38b06fd9b92dc2b68d58b75f900e97884c45bedd2ff83203d933cf5851c9/future-0.18.2.tar.gz
Summary  : Clean single-source support for Python 3 and 2
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: pypi-future-bin = %{version}-%{release}
Requires: pypi-future-license = %{version}-%{release}
Requires: pypi-future-python = %{version}-%{release}
Requires: pypi-future-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
Flask Sphinx Styles
===================
This repository contains sphinx styles for Flask and Flask related
projects.  To use this style in your Sphinx documentation, follow
this guide:

%package bin
Summary: bin components for the pypi-future package.
Group: Binaries
Requires: pypi-future-license = %{version}-%{release}

%description bin
bin components for the pypi-future package.


%package license
Summary: license components for the pypi-future package.
Group: Default

%description license
license components for the pypi-future package.


%package python
Summary: python components for the pypi-future package.
Group: Default
Requires: pypi-future-python3 = %{version}-%{release}

%description python
python components for the pypi-future package.


%package python3
Summary: python3 components for the pypi-future package.
Group: Default
Requires: python3-core
Provides: pypi(future)

%description python3
python3 components for the pypi-future package.


%prep
%setup -q -n future-0.18.2
cd %{_builddir}/future-0.18.2
pushd ..
cp -a future-0.18.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656404108
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-future
cp %{_builddir}/future-0.18.2/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-future/b41d323fb543c297b4ecc2a96425287c7dfdd5a4
cp %{_builddir}/future-0.18.2/docs/_themes/LICENSE %{buildroot}/usr/share/package-licenses/pypi-future/d0eff60551064b040266867c393e035d747b0ae5
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/futurize
/usr/bin/pasteurize

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-future/b41d323fb543c297b4ecc2a96425287c7dfdd5a4
/usr/share/package-licenses/pypi-future/d0eff60551064b040266867c393e035d747b0ae5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
