Name:           rpmorphan
Version:        1.7
Release:        3
Summary:        Find orphaned RPM packages
Group:          System/Configuration/Packaging
License:        GPLv2+
URL:            http://rpmorphan.sourceforge.net/
Source0:        http://downloads.sourceforge.net/sourceforge/rpmorphan/rpmorphan-%{version}.tar.gz
Source1:        rpmorphan.logrotate
Requires:       perl-Tk
Requires:       rpm
Requires(post): rpm-helper
BuildArch:      noarch

%description
rpmorphan finds orphaned packages on your system. It determines
which packages have no other packages depending on their installation,
and shows you a list of these packages.

It intends to be clone of deborphan Debian tools for RPM packages.

%prep
%setup -q

%build

%install
%makeinstall_std

%{__mv} %{buildroot}%{_bindir}/rpmorphan{.pl,}
%{__mv} %{buildroot}%{_bindir}/rpmusage{.pl,}
%{__perl} -pi -e 's/^rpmorphan\.pl/rpmorphan/g' %{buildroot}%{_bindir}/rpmorphan %{buildroot}%{_mandir}/man1/rpmorphan.1
%{__perl} -pi -e 's/^rpmusage\.pl/rpmorphan/g' %{buildroot}%{_bindir}/rpmusage %{buildroot}%{_mandir}/man1/rpmusage.1

%{__mkdir_p} %{buildroot}%{_sysconfdir}/logrotate.d
%{__cp} -p %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

%post
%create_ghostfile %{_logdir}/rpmorphan.log root root 644

%files
%defattr(0644,root,root,0755)
%doc Authors Changelog COPYING NEWS Readme rpmorphan.lsm Todo
%attr(0755,root,root) %{_bindir}/rpmorphan
%attr(0755,root,root) %{_bindir}/rpmorphan-lib.pl
%attr(0755,root,root) %{_bindir}/rpmusage
%attr(0755,root,root) %{_bindir}/rpmdep
%attr(0755,root,root) %{_bindir}/rpmdep.pl
%attr(0755,root,root) %{_bindir}/rpmduplicates
%attr(0755,root,root) %{_bindir}/rpmduplicates.pl
%attr(0755,root,root) %{_bindir}/rpmorphan-curses-lib.pl
%attr(0755,root,root) %{_bindir}/rpmorphan-tk-lib.pl
%{_mandir}/man1/rpmdep.1*
%{_mandir}/man1/rpmduplicates.1*
%ghost %{_logdir}/rpmorphan.log
%{_mandir}/man1/rpmorphan.1*
%{_mandir}/man1/rpmusage.1*
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%dir %{_var}/lib/rpmorphan
%{_var}/lib/rpmorphan/keep
