import urllib

def read():
    #Open is to open file on my computer and require only file path and name
    #Open creates an object of the File module which ccepts file functions like read
    cont = open(r"E:\Web Design\1MCoder\Files\word-check\movie_quotes\text.txt")
    #Read is to read content of file 
    read_cont = cont.read()
    #print read_cont
    #It is better to close a file after opening it on python with .close function
    cont.close()

    #same as open for url
    urlcheck = urllib.urlopen(r"https://www.purgomalum.com/service/containsprofanity?text="+read_cont)
    #urlcheck = urllib.urlopen("http://www.wdylike.appspot.com/?q="+read_cont)
    urlcheckread = urlcheck.read()
    #print urlcheckread
    urlcheck.close()
    if urlcheckread == "false":
        print "No BAD Words! Go on"
    elif urlcheckread == "true":
        print "Attention!! Bad words are in the text"
    else:
         print "Can't check this text"
read()
