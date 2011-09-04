# Copyright (c) 2000-2007, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%define short_name commons-discovery
%define section    free

Summary:        Jakarta Commons Discovery
Name:           jakarta-commons-discovery
Version:        0.4
Release:        5.4%{?dist}
Epoch:          1
Group:          Development/Libraries
License:        ASL 2.0
URL:            http://jakarta.apache.org/commons/discovery/
BuildArch:      noarch
Source0:        http://www.apache.org/dist/jakarta/commons/discovery/source/commons-discovery-0.4-src.tar.gz
Patch0:         %{name}-addosgimanifest.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  jpackage-utils >= 0:1.6
BuildRequires:  ant
BuildRequires:  ant-nodeps
BuildRequires:  junit >= 0:3.7
BuildRequires:  jakarta-commons-logging >= 0:1.0.4
Requires:       jakarta-commons-logging >= 0:1.0.4

%description
The Discovery component is about discovering, or finding, implementations for
pluggable interfaces.  Pluggable interfaces are specified with the intent that
multiple implementations are, or will be, available to provide the service
described by the interface.  Discovery provides facilities for finding and
instantiating classes, and for lifecycle management of singleton (factory)
classes. 

%package javadoc
Group:          Documentation
Summary:        Javadoc for %{name}
# for /bin/rm and /bin/ln
Requires(post): coreutils
Requires(postun): coreutils

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n commons-discovery-%{version}-src
%patch0
chmod u+w .

%build
ant \
  -Djunit.jar=%(find-jar junit) \
  -Dlogger.jar=%(find-jar jakarta-commons-logging) \
  test.discovery dist

%install
rm -rf $RPM_BUILD_ROOT

# jar
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p dist/%{short_name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && ln -s %{name}-%{version}.jar %{short_name}-%{version}.jar && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root,0755)
%doc LICENSE.txt
%doc NOTICE.txt
%doc RELEASE-NOTES.txt
%{_javadir}/*

%files javadoc
%defattr(0644,root,root,0755)
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1:0.4-5.4
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.4-5.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 28 2009 Alexander Kurtakov <akurtako@redhat.com> 1:0.4-4.3
- Add OSGi manifest.
- Drop gcj support.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.4-4.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1:0.4-3.2
- drop repotag
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1:0.4-3jpp.1
- Autorebuild for GCC 4.3

* Wed Mar 21 2007 Matt Wringe <mwringe@redhat.com> - 1:0.4-2jpp.1
- Merge with latest jpp version
- fix rpmlint isuses

* Sat Feb 17 2007 Fernando Nasser <fnasser@redhat.com> - 1:0.4-2jpp
- Remove distribution and vendor tags
- Fix empty post postun messages
- Use spaces and no tabs all over

* Sat Feb 17 2007 Fernando Nasser <fnasser@redhat.com> - 1:0.4-1jpp
- Upgrade to 0.4
- New license is ASL 2
- Add NOTICE.txt real file

* Thu Aug 10 2006 Matt Wringe <mwringe at redhat.com> - 1:0:3-4jpp.1
- Merge with upstream version
 - Add missing javadoc post and postun
 - Add missing javadoc requires

* Sat Jul 22 2006 Jakub Jelinek <jakub@redhat.com> - 1:0.3-3jpp_2fc
- Rebuilt

* Thu Jul 20 2006 Matt Wringe <mwringe at redhat.com> - 1:0:3-3jpp_1fc
- Merge with upstream version
- Natively compile packages

* Thu Jul 20 2006 Matt Wringe <mwringe at redhat.com> - 1:0:3-3jpp
- Added conditional native compiling

* Thu Apr 26 2006 Fernando Nasser <fnasser@redhat.com> - 1:0.3-2jpp
- First JPP 1.7 build

* Sat Jun 04 2005 Fernando Nasser <fnasser@redhat.com> - 1:1:0.3-1jpp
- Update to 0.3

* Sun Aug 23 2004 Randy Watler <rwatler at finali.com> - 1:0.2-2jpp
- Rebuild with ant-1.6.2

* Thu Apr 17 2003 Ville Skyttä <ville.skytta at iki.fi> - 1:0.2-1jpp
- Update to 0.2 and JPackage 1.5.

* Fri Sep 13 2002 Ville Skyttä <ville.skytta at iki.fi> 1:0.1-1jpp
- 0.1.

* Sat Sep  7 2002 Ville Skyttä <ville.skytta at iki.fi> 1.0-0.rc1.1jpp
- First JPackage release.
