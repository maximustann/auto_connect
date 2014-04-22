#!/usr/bin/env python


import sys,  urllib2, urllib





def connection(username_in, password_in):
    username = 'Student\\%s' %username_in
    password = password_in
    
    headers = {
    		'Host':'wireless.victoria.ac.nz',
    		'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:28.0) Gecko/20100101 Firefox/28.0',
    		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    		'Accept-Language':'en-US,en;q=0.5',
    		'Accept-Encoding':'gzip,deflate',
    		'Referer':'https://wireless.victoria.ac.nz/login.html',
    		'Connection':'keep-alive',
    		'Content-Type':'application/x-www-form-urlencoded',
    		'Content-Length':'133'
    		
    		}
    
    
    
    
    postdata = urllib.urlencode({
    		'buttonClicked':'4',
    		'redirect_url':'http://www.victoria.ac.nz/wirelessvic/',
    		'err_flag':'0',
    		'username':username,
    		'password':password
    		})
    url = 'https://wireless.victoria.ac.nz/login.html'
    data = postdata
    req = urllib2.Request(url, headers)
    
    try:
    	fd = urllib2.urlopen(req, data)
    except urllib2.HTTPError, e:
    	sys.exit(1)
    except urllib2.URLError, e:
    	sys.exit(2)
