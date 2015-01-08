import string,re

allChars = string.uppercase + string.lowercase
charToSoundex = string.maketrans(allChars,"91239129922455912623919292" * 2)
isOnlyChars = re.compile('^[A-Za-z]+$').search

def soundex(source):
	"convert string to Soundex equivalent"

	if not isOnlyChars(source):
		return "0000"

	digits = source[0].upper() + source[1:].translate(charToSoundex)

	digits2 = digits[0]
	for d in digits[1:]:
		if digits2[-1] != d:
			digits2 += d

	digits3 = digits2.replace('9','')

	digits3 += '000'

	return digits3[:4]


if __name__ == '__main__':
	from timeit import Timer
	names = ('Woo','Pilgrim','Flingjingwaller')
	for name in names:
		statement = "soundex('%s')" % name
		t = Timer(statement,"from __main__ import soundex")
		print name.ljust(15),soundex(name),min(t.repeat())
