#!/usr/bin/env python

"""Download specific http url image file which login need"""

__author__ = "SeongJae Park"
__email__ = "sj38.park@gmail.com"
__copyright__ = "Copyright (c) 2013, SeongJae Park"
__license__ = "GPLv3"

import os
import sys

USAGE = (
"""Usage: %s <main domain> <auth path> <download path> \ 
        <id> <password> <start> <end> <file save path> 

[OPTIONS]
   main domain: main homepage domain
   auth path: path for autentification that receives id and password
   download path: path you wish to get
   id: id for valid user of `main domain`
   password: password for valid user of `main domain`
   start: start number of download path
   end: end number of download path
   file save path: path to save downloaded file

[EXAMPLE]
   $ %s http://foo.com /auth/login_do user1 /photo/original/ \ 
            user1 password1 15 217 ./photo

   Above command will download http://foo.com/photo/original/15 ~
   http://foo.com/photo/original/217 file under ./photo directory.
""" % (sys.argv[0], sys.argv[0]))

if len(sys.argv) < 9:
    print USAGE
    exit(1)

domain = sys.argv[1]
auth_path = sys.argv[2]
down_path = sys.argv[3]
id_ = sys.argv[4]
passwd = sys.argv[5]
start = int(sys.argv[6])
end = int(sys.argv[7])
save_path = sys.argv[8]

cmd = "curl --cookie-jar cjar --output /dev/null %s" % domain
print cmd
os.system(cmd)

cmd = ("curl --cookie cjar --cookie-jar cjar " +
        "--data 'id=%s' --data 'passwd=%s' --location "
        % (id_, passwd) + 
        "--output loginresult.html %s%s" % (domain, auth_path))
print cmd
os.system(cmd)

if len(sys.argv) >= 6:
    download_path = sys.argv[5]

for i in range(start, end + 1):
    cmd = ("curl --cookie cjar --output %s/%d %s%s%d" %
        (save_path, i, domain, down_path, i))
    print cmd
    os.system(cmd)
