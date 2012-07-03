#!/usr/bin/python2.6
from HTMLParser import HTMLParser
from urllib2 import urlopen
from urlparse import urljoin

class WebCrawler(HTMLParser):
    def __init__(self, starting_url, no_of_links):
        HTMLParser.__init__(self)
        self.url = starting_url
        self.list_links = [self.url]   # list storing all th links traversed
        self.current_url = [self.url]  # current url
        self.no_of_links = no_of_links # max links to be traversed

    def handle_starttag(self, tag, attrs):
        if tag.lower() == 'a' and attrs and len(self.list_links)<self.no_of_links: # if html tag is of anchor type and count of traversed links are less then given links
            current_link = attrs[0][1]			# get the attribute ie the link url
            #if current_link[:4] != "http": old code
            #current_link = '/'.join(self.url.split('/')[:3])+('/'+current_link).replace('//','/') old code
	    current_link=urljoin(self.url,current_link)  # new code
            if current_link not in self.list_links:	
                print "new link found:::  %s" % current_link
                self.current_url.append(current_link)
                self.list_links.append(current_link)
                
    def crawl(self):
    	while(1):
            current_url = self.current_url[:]
            self.current_url = []
            if len(self.list_links)>=self.no_of_links: # if number of links exceeded the given maximum number of links then break
                break
            for self.url in current_url:
            	if len(self.list_links)>=self.no_of_links: # if number of links exceeded the given maximum number of links then break
            	    break
                try:
                    print "#"*80
                    print "Gathering links from :::  %s"%(self.url)
                    url_obj = urlopen(self.url) # create an object of the urlopen 
                    data = url_obj.read() 	# read the contents of the URL
                    #print data
                    self.feed(data)	        # feed the data to parser
                except (KeyboardInterrupt):
                    print "#"*80		# if user stops the execution
                    print "Keyboard Interrupt"
              	    print "*"*80,"RESULT OF CRAWLER","*"*80
                    for i in self.list_links:
		    	print "%s" %(i)
	            print "Total links found : %d "%(len(self.list_links))
	            raise SystemExit(0)
                except:
                    self.reset()		# in case of exception , reset the instance
        return self.list_links

if __name__ == "__main__":
    num_links = 100
    crawler_obj = WebCrawler(starting_url = 'http://www.python.org/',no_of_links=num_links) # create the object of the class
    print "Given number of links to be traversed are : %d"%(num_links)
    print "press ctrl+c to stop the crawler.."
    output = crawler_obj.crawl()                                                        # starting the crawler
    print "*"*80,"RESULT OF CRAWLER","*"*80
    for i in output:
    	print "%s" %(i)
    print "Total links found : %d "%(len(output))
