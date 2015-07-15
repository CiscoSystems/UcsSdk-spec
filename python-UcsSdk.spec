%global package_name UcsSdk

Name:           python-%{package_name}
Version:        0.8.2.2
Release:        0%{?dist}
Summary:        Python SDK for Cisco UCS Manager

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{package_name}
Source0:        https://pypi.python.org/packages/source/U/UcsSdk/UcsSdk-%{version}.tar.gz
# needed until https://github.com/CiscoUcs/UcsPythonSDK/pull/2
Source1:        README

BuildArch:      noarch

BuildRequires:  python2-devel

# needed until https://github.com/CiscoUcs/UcsPythonSDK/issues/3
BuildRequires:  dos2unix


%description
Python development kit for Cisco UCS

%prep
%setup -q -n %{package_name}-%{version}
cp %SOURCE1 .

%build
# needed until https://github.com/CiscoUcs/UcsPythonSDK/issues/3
dos2unix src/%{package_name}/{CcoImage,ConvertFromBackup}.py

%{__python2} setup.py build


%install
%{__python2} setup.py install --skip-build --root %{buildroot}

# needed until https://github.com/CiscoUcs/UcsPythonSDK/issues/4
chmod 755 %{buildroot}/%{python_sitelib}/%{package_name}/{UcsHandle,WatchUcsGui,CcoImage,ConvertFromBackup,UcsHandle_Edit}.py

%files
%{python2_sitelib}/%{package_name}/
%{python2_sitelib}/%{package_name}*.egg-info
%doc README

%changelog
* Wed Jul 15 2015 Brian Demers <brdemers@cisco.com> 0.8.2.2-0
- Initial RPM release

