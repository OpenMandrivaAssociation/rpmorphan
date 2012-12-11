Name:           rpmorphan
Version:        1.11
Release:        1
Epoch:          0
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
%attr(0755,root,root) %{_bindir}/rpmextra
%attr(0755,root,root) %{_bindir}/rpmextra.pl
%attr(0755,root,root) %{_bindir}/grpmorphan
%attr(0755,root,root) %{_bindir}/rpmdep
%attr(0755,root,root) %{_bindir}/rpmdep.pl
%attr(0755,root,root) %{_bindir}/rpmduplicates
%attr(0755,root,root) %{_bindir}/rpmduplicates.pl
%attr(0755,root,root) %{_bindir}/rpmorphan-curses-lib.pl
%attr(0755,root,root) %{_bindir}/rpmorphan-tk-lib.pl
%{_mandir}/man1/rpmdep.1.xz
%{_mandir}/man1/rpmextra.1.xz
%{_mandir}/man1/rpmduplicates.1.xz
%ghost %{_logdir}/rpmorphan.log
%{_mandir}/man1/rpmorphan.1*
%{_mandir}/man1/rpmusage.1*
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config /etc/rpmorphanrc
%dir %{_var}/lib/rpmorphan
%{_var}/lib/rpmorphan/keep
/usr/lib/%{name}/locale/en/rpmorphan_trans.pl
/usr/lib/%{name}/locale/fr_FR/rpmorphan_trans.pl

%changelog
* Thu Mar 04 2010 Frederik Himpe <fhimpe@mandriva.org> 0:1.7-1mdv2010.1
+ Revision: 514208
- update to new version 1.7

* Fri Jan 22 2010 Frederik Himpe <fhimpe@mandriva.org> 0:1.6-1mdv2010.1
+ Revision: 495045
- Update to new version 1.6

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0:1.3-2mdv2010.0
+ Revision: 442761
- rebuild

* Wed Oct 22 2008 David Walluck <walluck@mandriva.org> 0:1.3-1mdv2009.1
+ Revision: 296364
- 1.3
- add logrotate support
- fix License

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 0:1.1-4mdv2009.0
+ Revision: 260322
- rebuild

* Mon Jul 28 2008 Thierry Vignaud <tv@mandriva.org> 0:1.1-3mdv2009.0
+ Revision: 251496
- rebuild

* Sat Jan 19 2008 David Walluck <walluck@mandriva.org> 0:1.1-1mdv2008.1
+ Revision: 155106
- 1.1

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 16 2007 David Walluck <walluck@mandriva.org> 0:1.0-2mdv2008.0
+ Revision: 64097
- remove duplicate docs
- reflect name that we install as
- Requires: perl-Tk

* Sat Apr 28 2007 David Walluck <walluck@mandriva.org> 0:1.0-1mdv2008.0
+ Revision: 18912
- 1.0


* Wed Apr 04 2007 David Walluck <walluck@mandriva.org> 0.9-1mdv2007.1
+ Revision: 150461
- 0.9

* Thu Mar 08 2007 David Walluck <walluck@mandriva.org> 0:0.8-1mdv2007.1
+ Revision: 138535
- 0.8

* Wed Feb 28 2007 Lenny Cartier <lenny@mandriva.com> 0:0.4-1mdv2007.1
+ Revision: 127181
- Update to 0.4

* Mon Feb 05 2007 David Walluck <walluck@mandriva.org> 0:0.3-1mdv2007.1
+ Revision: 116398
- 0.3

* Wed Jan 24 2007 David Walluck <walluck@mandriva.org> 0:0.1-1mdv2007.1
+ Revision: 113033
- Import rpmorphan

* Wed Jan 24 2007 David Walluck <walluck@mandriva.org> 0:0.1-1mdv2007.1
- release

