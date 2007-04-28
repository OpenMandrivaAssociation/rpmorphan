Name:           rpmorphan
Version:        1.0
Release:        %mkrel 1
Epoch:          0
Summary:        Find orphaned rpm packages
Group:          System/Configuration/Packaging
License:        GPL
URL:            http://rpmorphan.sourceforge.net/
Source0:        http://umn.dl.sourceforge.net/sourceforge/rpmorphan/rpmorphan-%{version}.tar.gz
Requires:       rpm
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
rpmorphan finds orphaned packages on your system. It determines
which packages have no other packages depending on their installation,
and shows you a list of these packages.

It intends to be clone of deborphan debian tools for rpm packages.

%prep
%setup -q

%build
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}
%{__mv} %{buildroot}%{_bindir}/rpmorphan{.pl,}
%{__mv} %{buildroot}%{_bindir}/rpmusage{.pl,}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc Authors Changelog COPYING NEWS Readme rpmorphan.lsm test_rpmorphan.pl Todo
%attr(0755,root,root) %{_bindir}/rpmorphan
%attr(0755,root,root) %{_bindir}/rpmusage
%{_mandir}/man1/rpmorphan.1*
%{_mandir}/man1/rpmusage.1*
%dir %{_var}/lib/rpmorphan
%{_var}/lib/rpmorphan/keep


