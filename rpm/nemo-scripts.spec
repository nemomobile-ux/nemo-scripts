Name:       nemo-scripts
Summary:    Helper scripts for Nemo
Version:    0.1
Release:    0
Group:      Configs
License:    LGPLv2
URL:        https://github.com/nemomobile-ux/nemo-scripts
Source0:    %{name}-%{version}.tar.bz2
BuildArch:  noarch

%description
%{summary}

%prep

%setup -q

%install
install -D systemctl-user %{buildroot}%{_bindir}/systemctl-user

%files
%defattr(-,root,root,-)
%{_bindir}/systemctl-user
