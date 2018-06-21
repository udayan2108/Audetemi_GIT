import requests
#import shutil

import pdb
pdb.set_trace()
url = raw_input("Enter the url:")    #user input
req = requests.get(url, stream=True) #getting the requested url 

req.raise_for_status()               #use to raise na exceptions for error codes

with open('dhanu.txt', 'wb') as fd:   #it will write the url in this jpg imagefile 

    for chunk in req.iter_content(chunk_size=1024):  #downloading a file in peice of chunks

        print('Received a Chunk', chunk)

        fd.write(chunk)	
	
	        
		
	
