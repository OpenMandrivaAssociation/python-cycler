%define oname cycler

Summary:	Cycler python bindings
Name:		python-%{oname}
Version:	0.10.0
Release:	5
License:	LGPLv2
Group:		Development/Python
Url:		https://github.com/matplotlib/cycler
Source0:	https://github.com/matplotlib/cycler/archive/v%{version}.tar.gz
BuildRequires:	pkgconfig(python2)
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools
BuildRequires:	python2-setuptools
BuildArch:	noarch

Provides:	%{oname} = %{version}-%{release}

%description
This package includes Python bindings for cycler.

%package -n python2-%oname
Summary:	Cycler python2 bindings
License:	LGPLv2

%description -n python2-%oname
This package includes Python 2 bindings for cycler.

%prep
%setup -qn %{oname}-%{version}
%autopatch -p1

cp -a . %py2dir

%build
PYTHONDONTWRITEBYTECODE=1 python setup.py build

pushd %py2dir
PYTHONDONTWRITEBYTECODE=1 python2 setup.py build

%install
PYTHONDONTWRITEBYTECODE=1 python setup.py install --root=%{buildroot}

pushd %py2dir
PYTHONDONTWRITEBYTECODE=1 python2 setup.py install --root=%{buildroot}

%files
%python3_sitelib/cycler.py
%python3_sitelib/cycler-%{version}-py%py3ver.egg-info
%python3_sitelib/__pycache__/cycler*

%files -n python2-%oname
%python2_sitelib/cycler.py*
%python2_sitelib/cycler-%{version}-py%py2ver.egg-info

