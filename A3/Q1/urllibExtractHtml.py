#!/usr/bin/env python
import md5
import sys
import urllib2
import socket

# Main Function
def main():
	f 		  = open('uniqueUri.txt', 'r')	
	saveFile  = open('md5_uri.txt','w')
	count = 0
	for url in f.readlines():			
		hash_md5  = md5.new(url).hexdigest()			
		saveFile.write("{:<10}{} " .format( hash_md5 ,url))
		try :
			request     = urllib2.Request(url)
			response    = urllib2.urlopen(url,timeout=30)			
			html_content= response.read()
		
		except urllib2.HTTPError:
			pass
		except urllib2.URLError :
			pass
		except socket.timeout :
			pass

		filename    = "%s.htm" % hash_md5
		count =count +1
		print filename  , hash_md5 , url ,count
		# writing content to file created
		content_file= open(filename,"w")
		content_file.write(html_content )			
		content_file.close()

	saveFile.close()
	f.close()
	          
        
if __name__ =="__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)