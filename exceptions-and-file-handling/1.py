try:
	fs = open("/notthere")
except IOError:
	print "The file does not exist, exiting gracefully"
print "This line will always print"
