from collections import Counter

def readData(fileName):
	data = []
	tokens = []
	tags = []

	file = open(fileName, 'r')

	for sentence in file.read().split('\n'):

		for word in sentence.split():

			tokens.append(word.split('_')[0])
			tags.append(word.split('_')[1])

	return data, tokens, tags


def createUnigrams(tokens, tags):

	tokenTags = {}

	#
	# {and: [VB, NN, VB, NN]}
	#

	for i in range(len(tokens)):

		if not tokens[i] in tokenTags:
			tokenTags[tokens[i]] = [tags[i]]
		else:
			tokenTags[tokens[i]].append(tags[i])

	return tokenTags


def mostProbablePOS(dictionary):

	for key, value in dictionary.items():

		counter = Counter(value)
		maxValue = counter.most_common()[0]
		dictionary[key] = maxValue[0]

	# print (dictionary)
	return dictionary


def mostProbableErrors(tokens, tags, dictionary):

	modTags = []
	error = 0

	for word in tokens:
		modTags.append(dictionary[word])


	for i in range(len(modTags)):
		# print (modTags[i], tags[i])
		if modTags[i] != tags[i]:
			error += 1


	return modTags


def brillsPOS(tags, modTags):

	template = {}

	for i in range(len(modTags)):
		if modTags[i] != tags[i]:
			# tupel = (PREVIOUS_TAG, FROM, TO)
			tupel = (modTags[i-1], modTags[i], tags[i])
			if tupel in template:
				template[tupel] += 0
			else:
				template[tupel] = 0

	# print (template)


	sortedTemplate = sorted(template.items(), key=lambda x : x[1], reverse=True)

	print (len(sortedTemplate))
	return template

def checkError(tags, modTags, sortedTemplate):
    # bad
	error = 0
	badError = 0
	goodError = 0
	for k, v in sortedTemplate.items():
		prev = k[0]
		form = k[1]
		to = k[2]
		# print (prev, form)

		for i in range(len(tags)-1):
			if tags[i+1] == form:
				if tags[i] == prev:
					badError += 1
					sortedTemplate[k] -= 1
			elif tags[i+1] == to:
				if tags[i] == prev:
					goodError += 1
					sortedTemplate[k] += 1
	print (len(sortedTemplate))
	print (sortedTemplate)
	# print (sum(sortedTemplate.values()))

	sortedTemplate = sorted(sortedTemplate.items(), key=lambda x: x[1], reverse=True)
	print (sortedTemplate)
	# print (goodError)
	# print (badError)


if __name__ == '__main__':

	fileName = 'HW2_F17_NLP6320_POSTaggedTrainingSet-Unix.txt'

	data, tokens, tags = readData(fileName)

	unigrams = createUnigrams(tokens, tags)

	mostProbablePOS = mostProbablePOS(unigrams)

	modTags = mostProbableErrors(tokens, tags, mostProbablePOS)

	sortedTemplate = brillsPOS(tags, modTags)

	checkError(tags, modTags, sortedTemplate)