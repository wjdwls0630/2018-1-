import urllib.request
url = 'http://robjhyndman.com/tsdldata/ecology1/hopedale.dat'
webpage = urllib.request.urlopen(url)
line = webpage.readline()
webpage.close()


#line = line.strip()
#line = line.decode('utf-8')
#print(line)


##for line in webpage:
##    line = line.strip()
##    line = line.decode('utf-8')
##    print(line)
##webpage.close()
