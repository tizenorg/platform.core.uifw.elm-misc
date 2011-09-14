
Name:       elm-misc
Summary:    Elementary config files
Version:    0.1
Release:    1
Group:      TO_BE/FILLED_IN
License:    TO BE FILLED IN
BuildArch:  noarch
Source0:    elm-misc-%{version}.tar.bz2


%description
Elementary configuration files




%prep
%setup -q -n %{name}


%build



%install
rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_sysconfdir}/profile.d
%__cp etc/profile.d/elm.sh %{buildroot}%{_sysconfdir}/profile.d/elm.sh







%files
%defattr(-,root,root,-)
/etc/profile.d/elm.sh


