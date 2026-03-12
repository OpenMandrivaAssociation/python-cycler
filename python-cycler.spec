%define module cycler

Summary:	Cycler python bindings
Name:		python-cycler
Version:	0.12.1
Release:	1
License:	BSD-3-Clause
Group:		Development/Python
Url:		https://github.com/matplotlib/cycler
Source0:	https://github.com/matplotlib/cycler/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
Provides:	%{module} = %{version}-%{release}

%description
This package includes Python bindings for cycler.

%files
%python3_sitelib/%{module}
%python3_sitelib/%{module}-%{version}.dist-info
