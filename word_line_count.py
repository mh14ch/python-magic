#!/usr/bin/python2.6
import sys

'''
	function to count the number of words or lines 
'''
def count_word_lines(file_obj,line_flag,word_flag):			
	try:
		count_lines = 0
		count_words = 0
		while True:
			data=file_obj.read(1000000)												# read data
			if data=="":															# if empty data, return 
				return [count_lines,line_flag,count_words,word_flag]
			if line_flag:															# do we need to count number of lines
				count_lines +=data.count("\n")
			if word_flag:															# do we need to count number of words
				count_words +=len(data.split())
	except (KeyboardInterrupt):
		print "*"*80																# if user stops the execution
		print "No input was provided"
		return []
	except Exception,e:																# if some error occurred
		print "*"*80,"\n"
		print "Some error occurred , please contact the developer at mahimatrix@gmail.com "
		print "error message  ",str(e)
		print "*"*80 
		return []
		
		
		
		
def main():	
	try:			
		inpt=sys.argv																	# gather inputs from command line
		result=[]									
		count = inpt.count('word_line_count.py') + inpt.count('-l') + inpt.count('-w')	# count the required arguments
		if inpt.count('--help')!=0:														# if user asked for help
			print "*"*80,"\n"
			print " Python Program to count number of words and lines"
			print " "*40,"-"*10,"by mahimatrix"
			print " Arguments list ::"
			print " -l to count number of lines "
			print " -w to count number of words " 
			print " --help to view the help" 
			print "\n","*"*23," for counting number of lines: ","*"*23
			print " Example : \n python2.6 word_line_count.py -l file_name "
			print "\n","*"*23," for counting number of words: ","*"*23
			print " Example : \n python2.6 word_line_count.py -w file_name "	
			print "\n","*"*18," for counting number of lines and words: ","*"*18
			print " Example : \n python2.6 word_line_count.py  -l -w file_name "
			print "\n","*"*17," for taking the input from standard input: ","*"*17
			print " Example : \n cat filename | python2.6 word_line_count.py -l -w \n"
			print "*"*80
		elif count<2:																	# if arguments are invalid
			print "*"*80 , "\n"
			print "--invalid arguments...\n To view the help use python2.6 word_line_count.py --help \n"
			print "*"*80 , "\n"
		elif len(inpt)-count==1:														# if user provided the filename
			try:
				file_name=inpt[-1]														# take the filename from argument list
				with open(file_name) as file_obj:										
					result = count_word_lines(file_obj,inpt.count('-l'),inpt.count('-w'))
			except Exception,e:
				result=[]
				print "*"*80
				print "Error Found :",str(e[-1])
		
		elif len(inpt)-count==0:														# get input from standard input
			try:
				file_obj = sys.stdin													# get the standard input object
				result = count_word_lines(file_obj,inpt.count('-l'),inpt.count('-w'))
			except (KeyboardInterrupt):
				print "#"*80															# if user stops the execution
				print "No input was provided"
			except Exception,e:
				result=[]
				print "*"*80,"\n"
				print "Some error occurred , please contact the developer at mahimatrix@gmail.com "
				print "error message  ",str(e)
				print "*"*80 
			
		if result:																		# display result to user if its not empty
			if result[1]:
				print "number of lines : ",result[0]
			if result[3]:
				print "number of words : ",result[2]
			
			
	except Exception,e:																	# if some exception occurred
		print "*"*80,"\n"
		print "Some error occurred , please contact the developer at mahimatrix@gmail.com "
		print "error message  ",str(e)
		print "*"*80 
	
	
if __name__ == "__main__":
    main()

