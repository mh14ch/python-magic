import sys
arg = sys.argv
def convert_time(stime,fps,delay):
	stime = stime.split(" --> ")
	seconds = int(stime[0][0:2])*3600 + int(stime[0][3:5])*60 + int(stime[0][6:8]) + (float(stime[0][-3:]) + delay)/1000
	start_frame = int(round(seconds*fps))
	start_frame = 0 if start_frame<0 else start_frame
	seconds = int(stime[1][0:2])*3600 + int(stime[1][3:5])*60 + int(stime[1][6:8]) + (float(stime[1][-3:]) + delay)/1000
	end_frame = int(round(seconds*fps))
	end_frame = 0 if end_frame<0 else end_frame
	return "{"+str(start_frame)+"}"+"{"+str(end_frame)+"}"

def convert_frames(frames,fps,delay):
    frames = float(frames)/fps
    frames += delay/1000
    if frames <= 0:
        return "00:00:00,000"
    hours = int(frames/3600)
    seconds = frames-hours*3600
    minutes = int(seconds/60)
    seconds = seconds-minutes*60
    milliseconds = (seconds-int(seconds))*1000
    return "%02d:%02d:%02d,%03d"%(hours,minutes,seconds,milliseconds)	


def convert_srt(input_file,output_file,fps,delay):
	try:
		file_inp = open(input_file,"r")
		read_data = file_inp.read() # read input file
		file_inp.close()

		split_str1="\n"				# split string for ubuntu
		split_str2="\n\n"			# split string for ubuntu

		if read_data.find('\r')!=-1:
			split_str1="\r\n"		# split string for windows
			split_str2="\r\n\r\n"	# split string for windows
		
		file_out = open(output_file,"w")
		read_data = read_data.split(split_str2) # split input subtitle file according to per subtitle
		for text in read_data:
			split_text = text.split(split_str1) 
			if len(split_text) > 1:
				split_text.pop(0)      # remove number of subtitle 
				split_text[0]=convert_time(split_text[0],fps,delay) 
				file_out.write(''.join(split_text)+split_str1) # the desired output of .sub
				
				
		file_out.close()  
		print "*"*80,"\n"
		print " %s file is ready ...."%(output_file)
		print " Thanks for using the Simple subtitle convertor "
		print "*"*80,"\n"
		
	except Exception,e:
		print "*"*80,"\n"
		print "Some error occurred , please contact the developer at mahimatrix@gmail.com "
		print "error message  ",str(e)
		print "*"*80      

def convert_sub(input_file,output_file,fps,delay):
	try:
		file_inp = open(input_file,"r")
		read_data = file_inp.read() # read input file
		file_inp.close()
		split_str1 = "\n"			# split string for ubuntu
		split_str2 = "\n\n"			# split string for ubuntu

		if read_data.find('\r')!=-1:
			split_str1 = "\r\n"		# split string for windows
			split_str2 = "\r\n\r\n"		# split string for windows
		
		file_out = open(output_file,"w")
		read_data = read_data.split(split_str1) # split input subtitle file according to per subtitle
		count=1
		for text in read_data:
			split_text = text.split("}") 
			if len(split_text) > 1:
				frames1 = convert_frames(int(split_text[0][1:]),fps,delay)				
				frames2 = convert_frames(int(split_text[1][1:]),fps,delay)					
				file_out.write(str(count) + split_str1 + frames1 + " --> " + frames2 + split_str1 + split_text[2].replace('|',split_str1) + split_str2)
				count += 1
		file_out.close()  
		print "*"*80,"\n"
		print " %s file is ready ...."%(output_file)
		print " Thanks for using the Simple subtitle convertor "
		print "*"*80,"\n"
		
	except Exception,e:
		print "*"*80,"\n"
		print "Some error occurred , please contact the developer at mahimatrix@gmail.com "
		print "error message  ",str(e)
		print "*"*80      






try:
	if arg.count('--help'):
		print "*"*80,"\n"
		print " Simple subtitle convertor v1.1 for .srt & .sub files"
		print " "*40,"-"*10,"by mahimatrix"
		print " arguments list"
		print " -i input file \n -f frames per second(optional, default 25) "
		print " -d delay(optional, delay in milliseconds, can be positive, negative or 0, default 0) " 
		print "\n","*"*23," for .srt to .sub conversion:: ","*"*23
		print " \n Example : \n python2.6 convertor.py -i dark_knight.srt -f 24 -d 1000 \n"
		print "\n","*"*23," for .sub to .srt conversion:: ","*"*23
		print " \n Example : \n python2.6 convertor.py -i dark_knight.sub -f 24 -d 1000 \n"		
		print "*"*80
	elif arg.count('-i'):
		input_file = arg[arg.index("-i") + 1]        	 # receive the input file name
		if arg.count('-f'):
		    fps = float(arg[arg.index("-f") + 1])        # receive frames per second
		    if fps==0:
		    	print "*"*80,"\n\n\n trying to be smart ... :) :) I caught you !!\n\n\n","*"*80
		    	fps=25
		else:
		    fps=25
		if arg.count('-d'):
		    delay = int(arg[arg.index("-d") + 1])        # receive delay
		else:
			delay=0
		output_file = input_file.split(".")              # receive output file name
		if output_file[-1].lower()=="sub" :
			output_file=".".join(output_file[:-1])+".srt"
			convert_sub(input_file,output_file,fps,delay)	
		elif output_file[-1].lower()=="srt" :
			output_file=".".join(output_file[:-1])+".sub"
			convert_srt(input_file,output_file,fps,delay)	
		else:
			print "*"*80,"\n"
			print "Invalid Extensions used..\nPress 'python2.6 convertor.py --help' for help "
			print "*"*80 	
	else:
		print "*"*80,"\n"
		print "Invalid Arguments..\nPress 'python2.6 convertor.py --help' for help "
		print "*"*80
except Exception,e:
		print "*"*80,"\n"
		print "Invalid Arguments..\nPress 'python2.6 convertor.py --help' for help "
		print "*"*80
       
