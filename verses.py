#Bible verse list to text - Python script

import io
import urllib2
import re

file = open("data2.txt", 'r')
stihove = file.readlines()
file.close()

ofile = open("rezultat2.txt", "w")
print >> ofile, "\n"
ofile.close()

ofile = open("rezultat2.txt", "a")
             
for line in stihove:
    temp = line.split()
    bookpr = book = temp[0]
    if temp[0].isdigit():
        book = temp[0] + "+" + temp[1]
        bookpr = temp[0] + " " + temp[1]
        temp.pop(0)
    temp.pop(0)
    
    print "\nWorking on the book of " + bookpr
  
    for s in temp:
        s= s.rstrip('\n')
        s2 = re.sub('\s+','+',s)
        s3 = re.sub(':', '%3A',s2)
        s4 = book + s3
        s4pr = bookpr + " " + s
        print "\n " + s4pr
        #print "[debug] " + s4 + "\n"
        
        result = None
        html = None
        
        url = "https://www.biblegateway.com/passage/?search=" + s4 + "&version=BPB"
        #print url + "\n"
        result = urllib2.urlopen(url)
        html = result.read()

        tarsime = "<meta property=\"og:description\" content=.*\-\s*(.*)\"\/\>"
        #tarsime = "<meta property=\"og:description\" content=\"\s*(.*)\"\/\>"
        tarsene = re.search(tarsime, html)
        if  not tarsene:
            tarsime = "<meta property=\"og:description\" content=\"\s*(.*)\"\/\>"
            tarsene = re.search(tarsime, html)
        zafile = "\n\n" + s4pr
        print >> ofile, zafile
        ofile.write(tarsene.group(1))
        print tarsene.group(1)

ofile.close()

   


