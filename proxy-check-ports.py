#!/usr/bin/env python

from socket import *
import httplib

proxyhost = "10.10.10.131"
proxyport = 3128
rhost = "10.10.10.131"
rports = range(1, 65536)

header_template = """\
GET http://{host}:{port}/ HTTP/1.1
Host: {host}
User-Agent: Mozilla/5.0 (X11; Linux i686; rv:60.0) Gecko/20100101 Firefox/60.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Cookie: PHPSESSID=p9mfqnhob337l15j7fksvve2b4
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0

"""

def genHeader(host, port):
    return header_template.format(host=host, port=port)

for rport in rports:
    if  rport % 1000 == 0:
        print "[-] Trying Port {}".format(rport)

    conn = httplib.HTTPConnection(proxyhost, proxyport)
    conn.request("GET", "http://{}:{}/".format(rhost, rport))
    res = conn.getresponse()
    ##############
    if res.status != 503:
        print "[{} :{}] {} {}".format(rhost, rport, res.status, res.reason)
        for line in res.read().splitlines()[:3]:
            print "    {}".format(line)
    ##############
    conn.close()
