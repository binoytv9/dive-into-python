from UserDict import UserDict

def stripnulls():
	pass

class FileInfo(UserDict):
	"store file metadata"

	def __init__(self,filename=None):
		UserDict.__init__(self)
		self["name"] = filename

class MP3FileInfo(FileInfo):
	"store ID3v1.0 MP3 tags"

	tagDataMap = {	"title"  : (  3, 33,stripnulls),
			"artist" : ( 33, 63,stripnulls),
			"album"  : ( 63, 93,stripnulls),
			"year"   : ( 93, 97,stripnulls),
			"comment": ( 97,126,stripnulls),
			"genre"  : (127,128,ord)  }

	def __setitem__(self,key,item):
		if key == "name" and item:
			self.__parse(item)
		FileInfo.__setitem__(self,key,item)

	def __parse(self,item):
		print 'this is private method shoooooo!!!'
