import enchant

def classifier(token):
	""" Classifies the given token into one of several categories.
	categories currently defined are:
		letter (single alphabet),
		digit (single number),
		special character,
		dictionary word, 
		random word,
		all even digits,
		all odd digits, 
		even number, 
		odd number, 
		mixed characters
	"""

	#initialise dictionaries for English words
	USEnglishDict = enchant.Dict("en_US")
	GBEnglishDict = enchant.Dict("en_GB")

	#check if token is a single character
	if len(token) == 1:
		#check if is an alphabet
		if token.isalpha():
			return "Letter"
		#check if is a digit
		elif token.isdigit():
			return "Digit"
		else:
			return "SpecialChar"

	#token is more than 1 character
	else:
		#check if token is a string of alphabets, check if a dictionary word or not
		if token.isalpha():
			if USEnglishDict.check(token) or GBEnglishDict.check(token):
				return "DictionaryWord"
			else:
				return "RandomWord"
		#check if token is a number, sort between even and odd
		elif token.isdigit():
			evenCount = 0
			oddCount = 0
			for x in range(len(token)):
				if token[x]%2 ==0:
					evenCount+=1
				else:
					oddCount+=1
			if evenCount == len(token):
				return "AllEvenDigits"
			elif oddCount == len(token):
				return "AllOddDigits"
			else:
				if token%2 == 0:
					return "EvenNumber"
				else:
					return "OddNumber"
		else:
			return "MixedCharacters"
