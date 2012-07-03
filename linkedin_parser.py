from HTMLParser import HTMLParser
from urllib2 import urlopen
import time,re

class Parser(HTMLParser):
    flag=0						# flag is used as a counter of same tags , like div opens within a div, i faced  this problem in my last program
    tag_name=""					# stores the tag name for which searching is going
    class_dict = {"vcard contact":[],"vevent vcard summary-current":[],"vevent vcard summary-past":[],"projects documents":[],"education vevent vcard":[],"honors":[]}
    							# dict storing values of searching classes , insert a blank list to search more classes like 
    							# class_name:[empty list] 
    class_info = {"vcard contact":"Contact Information","vevent vcard summary-current":"Current Summary","vevent vcard summary-past":"Past Summary","projects documents":"Projects","education vevent vcard":"Education Details","honors":"Honors & Achievements"}
    temp_li=[]					# temporary list used 
    current_class=""			# current class which was found and being processed
	    	
    def handle_starttag(self,tag,attrs):
        if attrs==[]:                            # if blank attrs return
            return
        checked=False							
        for attr in attrs:						# many times more than one attribute is present
            for class_tag in attr:
            	for find_str in self.class_dict:
                	if class_tag.find(find_str)!=-1:
						self.flag +=1
						self.tag_name =tag
						checked =True
						self.current_class =find_str
						#break
						
        if checked==False and tag==self.tag_name:# div opens within a div, as i wrote above
            self.flag+=1						# increment flag
            
    def handle_data(self,data):
        if self.flag==0:						# data not useful if flag is 0
            return
        if data.find('/* extlib:')!=-1 or data.find('LI.Controls.addControl')!=-1:
            return
        data=data.replace('\n','')
        data=data.strip()
        if data=='':							# empty data 
            return
        
        self.temp_li.append(data)			# save the data
        
        
    def handle_endtag(self,tag):
        if self.flag==0:					
            return
        if self.tag_name==tag:				# tag closes , decrement flag
            self.flag-=1
            if self.temp_li!=[] and self.flag==0:	# search is complete for the given class, all tags closed ie flag is 0
				self.class_dict[self.current_class].append(" ".join(self.temp_li)+"\n")
				self.temp_li=[]				# reset temp_li
				self.tag_name=""			# reset tag_name

try:

	url=urlopen("http://www.linkedin.com/pub/mahipal-choudhary/28/850/1b2")
	parser_obj=Parser()
	time_start=time.time()
	parser_obj.feed(url.read())
	for data in parser_obj.class_dict:
		print "\n\nHeader name searching for is :",parser_obj.class_info[data]
		if parser_obj.class_dict[data]!=[]:
			print "Data found for above field ::\n" ,''.join(parser_obj.class_dict[data])
		else:
			print "Data not found for above field "


	print "time for fetching the link and parsing it :",time.time()-time_start,"seconds"
except Exception,e:
	print "Please contact the developer at mahimatrix@gmail.com with the given below error details:"
	print str(e)
