from classifier import classifier, isOnlySpecialCharacters, classifyCharacter

def tokeniser(tokenInfo):
	"""
	Accepts a dictionary from models.py and maps the remaining parts of the source password.
	Goes through the reamining tokens and classifies them.
	Adds key - value pairs to the original dictionary under new classifications.
	"""

	source_pass = tokenInfo["source_pass"]
	tokensToSort = []
	tokensToClassify = []

	wordStartIndex = []
	wordEndIndex = []

	for word in tokenInfo["tokens"]["words"]:
		wordStartIndex.append(word["start_index"])
		wordEndIndex.append(word["end_index"])

	tempToken = ""
	index = 0
	count = 0
	tempTokenStartIndex = 0

	while index<len(source_pass):
		if wordStartIndex[count] == index:
			index = wordEndIndex[count]+1
			count += 1
			if tempToken != "":
				tokensToSort.append({
					"content": tempToken,
					"start_index": tempTokenStartIndex,
					"end_index": tempTokenStartIndex + len(tempToken) - 1
					})
			tempTokenStartIndex = index
			tempToken = ""
		else:
			tempToken.append(source_pass[index])

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
					tempTokenBeingSorted.append(tokenBeingSorted["content"][chars+1])
				else:
					tokensToClassify.append({
						"content": tempTokenBeingSorted
						"start_index": tempStartIndex
						"end_index": tempStartIndex + len(tempTokenBeingSorted) - 1
						})
					tempStartIndex += len(tempTokenBeingSorted)
					tempTokenBeingSorted = tokenBeingSorted["content"][chars+1]

			tokensToClassify.append({
				"content": tempTokenBeingSorted
				"start_index": tempStartIndex
				"end_index": tempStartIndex + len(tempTokenBeingSorted) - 1
				})

	for token in tokensToClassify:
		
		unclassifiedToken = token["content"]
		classification = classifier(unclassifiedToken)

		tokenInfo["tokens"][classification] = {}
		tokenInfo["tokens"][classification]["content"] = unclassifiedToken
		tokenInfo["tokens"][classification]["start_index"] = token["start_index"]
		tokenInfo["tokens"][classification]["end_index"] = token["end_index"]

	return tokenInfo