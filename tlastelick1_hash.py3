#!/usr/local/bin/python3
import os.path
import sys
import hashlib

size = 10000;
md5 = hashlib.md5()
sha1 = hashlib.sha1()

#Check terminal input length.
if (len(sys.argv) == 2):
  
  #If file exists.
  if os.path.isfile(sys.argv[1]):
    fileToHash = open(sys.argv[1], 'rb') #Read file in binary so I don't have to encode() later.
    buf = fileToHash.read(size)
  
  #Read contents of file.
  #Update contents of md5 object with buf object every 10000 bytes.     
    while len(buf) > 0:
      md5.update(buf)
      sha1.update(buf)
      buf = fileToHash.read(size)
  
  #Create files to append too.
    md5HashFile = open('tlastelick1_MD5.txt', 'a')
    sha1HashFile = open('tlastelick1_SHA1.txt', 'a')

  #Write to files
    md5HashFile.write(sys.argv[1] + ' ' + md5.hexdigest() + '\n')
    sha1HashFile.write(sys.argv[1] + ' ' + sha1.hexdigest() + '\n')
  
  #Else file does not exist.
  else:
    print ('File does not exist: ' + sys.argv[1])
    sys.exit()

else:
  print ('Usage: ./tlastelick1_hash.py3 filepath')
  sys.exit()




#print('MD5 hash for ' + sys.argv[1] + ' is ' +  md5.hexdigest())
#print('SHA1 hash for ' + sys.argv[1] + ' is ' + sha1.hexdigest())

