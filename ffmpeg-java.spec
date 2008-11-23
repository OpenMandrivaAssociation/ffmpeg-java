Summary:	A Java wrapper around ffmpeg, using JNA
Name:		ffmpeg-java
Version:	20071012
Release:	%mkrel 0.0.5
License:	LGPL
Group:		Development/Java
URL:		http://fmj.sourceforge.net/
Source0:	%{name}.tar.bz2
BuildRequires:	ant
BuildRequires:	java-rpmbuild >= 1.5
#BuildRequires:	libffmpeg0-devel
BuildRequires:	update-alternatives
BuildRequires:	xml-commons-apis
Requires:	java >= 1.5
Requires:	libffmpeg
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
ffmpeg-java is a Java wrapper around ffmpeg, using JNA.

%package javadoc
Summary:	Javadoc for ffmpeg-java
Group:		Development/Java

%description javadoc
Javadoc for ffmpeg-java.

%prep
%setup -q -n %{name}

%build
%__rm src/*.html
%ant javac jar javadoc

#%ant \
#	-Dffmpeg.home="%{_includedir}/ffmpeg" \
#	compile-test-linux

%install
# jar
%__install -dm 755 %{buildroot}%{_javadir}/fmj
%__install -pm 644 build/jars/%{name}.jar \
	%{buildroot}%{_javadir}/fmj/%{name}-%{version}.jar
%__install -pm 644 build/jars/%{name}-gpl.jar \
	%{buildroot}%{_javadir}/fmj/%{name}-gpl-%{version}.jar
pushd %{buildroot}%{_javadir}/fmj
	for jar in *-%{version}*; do
		ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`
	done
popd

# javadoc
%__install -dm 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
%__cp -pr build/doc/* \
	%{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name} 

%clean
[ -d %{buildroot} -a "%{buildroot}" != "" ] && %__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc *.txt LICENSE README
%dir %{_javadir}/fmj
%{_javadir}/fmj/*.jar

%files javadoc
%defattr(0644,root,root)
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}
