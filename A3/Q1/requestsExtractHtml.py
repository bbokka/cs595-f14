#!/usr/bin/env python
import md5
import requests
import urllib2
import socket

# Main Function
def main():
	f 		  = open('uniqueUri.txt', 'r')	
	saveFile  = open('md5_uri.txt','w')
	count = 0 
	connect = 0 
	socket = 0
	timeo =0
	unko=0
	for url in f.readlines():			
		hash_md5  = md5.new(url).hexdigest()			
		saveFile.write("{:<10}{} " .format( hash_md5 ,url))
		try :
			response    = requests.get(url,timeout = 30)
			html_content= response.content

		except requests.exceptions.Timeout:
			timeo=timeo+1
			pass
		except requests.exceptions.ChunkedEncodingError:
			unko=unko+1
			pass
		except requests.exceptions.ConnectionError :
			connect=connect+1
			pass		
		except socket.timeout:
			socket = socket+1
			pass
			
		filename    = "%s.htm" % hash_md5
		count =count +1
		print filename  , hash_md5 ,'---', url ,'**',count,connect,socket, timeo,unko
		# writing content to file created
		content_file= open(filename,"w")
		content_file.write(html_content )			
		content_file.close()
	print connect
	saveFile.close()
	f.close()
	          
        
if __name__ =="__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)


#os.system("wget -O  hash_md5 %s" %url)

# request     = urllib2.Request(url)
# response    = urllib2.urlopen(url,timeout=20)			
# html_content= response.read()