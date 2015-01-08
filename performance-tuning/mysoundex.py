import string,re

allChars = string.uppercase + string.lowercase
charToSoundex = string.maketrans(allChars,"91239129922455912623919292" * 2)

def soundex(source):
	"convert string to Soundex equivalent"

	if not source or not source.isalpha():
		return "0000"

	digits = source[0].upper() + source[1:].translate(charToSoundex)

	digits2 = digits[0]
	for d in digits[1:]:
		if (d != '9') and (digits2[-1] != d):
			digits2 += d

	return (digits2 + '000')[:4]


if __name__ == '__main__':
	from timeit import Timer
	names = ('sd4','Woo','Pilgrim','Flingjingwaller')
	for name in names:
		statement = "soundex('%s')" % name
		t = Timer(statement,"from __main__ import soundex")
		print name.ljust(15),soundex(name),min(t.repeat())
