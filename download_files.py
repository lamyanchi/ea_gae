import urllib2
from os.path import isdir
import os

f = open('list.txt')
urls = [line.strip() for line in f.readlines()]
f.close()

for url in urls:
    #make dirs if not in exsitance
    dirs = url[21:].split('/')[:-1]
    file_name = url[21:].split('/')[-1]
    
    for i in range(1,len(dirs)+1):
        path = "/".join(dirs[0:i])
        if not isdir(path):
            os.system('mkdir %s' % path)
    
    file_path = url[21:]
    
    print 'processing %s' % file_path
    
    soc = urllib2.urlopen(url)
    localFile = open(file_path, 'w')
    localFile.write(soc.read())
    localFile.close()