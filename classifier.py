import enchant

def classifier(password):
	""" Classifies the given password into one of several categories.
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

	#check if password is a single character
	if len(password) == 1:
		#check if is an alphabet
		if password.isalpha():
			return "Letter"
		#check if is a digit
		elif password.isdigit():
			return "Digit"
		else:
			return "SpecialChar"

	#password is more than 1 character
	else:
		#check if password is a string of alphabets, check if a dictionary word or not
		if password.isalpha():
			if USEnglishDict.check(password) or GBEnglishDict.check(password):
				return "DictionaryWord"
			else:
				return "RandomWord"
		#check if password is a number, sort between even and odd
		elif password.isdigit():
			evenCount = 0
			oddCount = 0
			for x in range(len(password)):
				if password[x]%2 ==0:
					evenCount+=1
				else:
					oddCount+=1
			if evenCount == len(password):
				return "AllEvenDigits"
			elif oddCount == len(password):
				return "AllOddDigits"
			else:
				if password%2 == 0:
					return "EvenNumber"
				else:
					return "OddNumber"
		else:
			return "MixedCharacters"
