import sys,os,re,unittest

def regressionTest():
	path = os.path.abspath(os.path.dirname(sys.argv[0]))
	#print path
	#print
	files = os.listdir(path)
	#print files
	#print
	test = re.compile("test\.py$",re.IGNORECASE)
	files = filter(test.search,files)
	#print files
	#print
	filenameToModuleName = lambda f: os.path.splitext(f)[0]
	moduleNames = map(filenameToModuleName,files)
	#print moduleNames
	#print
	modules = map(__import__,moduleNames)
	#print modules
	#print
	load = unittest.defaultTestLoader.loadTestsFromModule
	return unittest.TestSuite(map(load,modules))

if __name__ == '__main__':
	regressionTest()
	#unittest.main(defaultTest="regressionTest")
