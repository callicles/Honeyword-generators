from classifier import classifier, isOnlySpecialCharacters, classifyCharacter
import pprint

pp = pprint.PrettyPrinter(indent=1)

def tokeniser(tokenInfo):
	"""
	Accepts a dictionary from models.py and maps the remaining parts of the source password.
	Goes through the reamining tokens and classifies them.
	Adds key - value pairs to the original dictionary under new classifications as defined in classifier in classifer.
	"""

	source_pass = tokenInfo["source_pass"]
	tokensToSort = []
	tokensToClassify = []

	wordStartIndex = []
	wordEndIndex = []

	#Going through the words identified in the input and saving their start and end index in an array to use later
	for word in tokenInfo["tokens"]["words"]:
		wordStartIndex.append(word["start_index"])
		wordEndIndex.append(word["end_index"])

	tempTokenStartIndex = 0
	tempToken = ''
	for i in range(len(wordStartIndex)):
		tempToken = source_pass[tempTokenStartIndex:wordStartIndex[i]]
		if tempToken != '':
			tokensToSort.append({
					"content": tempToken,
					"start_index": tempTokenStartIndex,
					"end_index": wordStartIndex[i]-1
				})
		tempTokenStartIndex = wordEndIndex[i] + 1

	if len(source_pass) > (wordEndIndex[len(wordEndIndex)-1] + 1):
		tempToken = source_pass[wordEndIndex[len(wordEndIndex)-1]+1:len(source_pass)]
		tokensToSort.append({
					"content": tempToken,
					"start_index": wordEndIndex[len(wordEndIndex)-1],
					"end_index": len(source_pass)-1
				})

	#pp.pprint(tokensToSort)

	for tokenBeingSorted in tokensToSort:
		if tokenBeingSorted["content"].isalpha() or tokenBeingSorted["content"].isdigit() or isOnlySpecialCharacters(tokenBeingSorted["content"]) or len(tokenBeingSorted["content"])==1:
			tokensToClassify.append({
				"content": tokenBeingSorted["content"],
				"start_index": tokenBeingSorted["start_index"],
				"end_index": tokenBeingSorted["end_index"]
			})
		else:
			tempTokenBeingSorted = tokenBeingSorted["content"][0]
			tempStartIndex = tokenBeingSorted["start_index"]

			for chars in range(len(tokenBeingSorted["content"]) -1):
				if classifyCharacter(tokenBeingSorted["content"][chars]) == classifyCharacter(tokenBeingSorted["content"][chars+1]):
					tempTokenBeingSorted+=(tokenBeingSorted["content"][chars+1])
				else:
					tokensToClassify.append({
						"content": tempTokenBeingSorted,
						"start_index": tempStartIndex,
						"end_index": tempStartIndex + len(tempTokenBeingSorted) - 1
					})
					tempStartIndex += len(tempTokenBeingSorted)
					tempTokenBeingSorted = tokenBeingSorted["content"][chars+1]

			tokensToClassify.append({
				"content": tempTokenBeingSorted,
				"start_index": tempStartIndex,
				"end_index": tempStartIndex + len(tempTokenBeingSorted) - 1
			})

	for token in tokensToClassify:

		unclassifiedToken = token["content"]
		classification = classifier(unclassifiedToken)
		if classification not in tokenInfo["tokens"]:
			tokenInfo["tokens"][classification] = []

		tokenInfo["tokens"][classification].append({
		"content": unclassifiedToken,
		"start_index": token["start_index"],
		"end_index": token["end_index"]
		})

	return tokenInfo