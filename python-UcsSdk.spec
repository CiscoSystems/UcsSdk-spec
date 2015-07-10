%global package_name UcsSdk

Name:           python-%{package_name}
Version:        0.8.2.2
Release:        0%{?dist} 
Summary:        Python SDK for Cisco UCS Manager

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{package_name}
Source0:        https://pypi.python.org/packages/source/U/UcsSdk/UcsSdk-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python2-devel

%description
Python development kit for Cisco UCS

%prep
%setup -q -n %{package_name}-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}

%files
%{python_sitelib}/%{package_name}/
%{python_sitelib}/%{package_name}*.egg-info



