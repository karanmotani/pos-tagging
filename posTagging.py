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



if __name__ == '__main__':

	fileName = 'HW2_F17_NLP6320_POSTaggedTrainingSet-Unix.txt'
	
	data, tokens, tags = readData(fileName)

	unigrams = createUnigrams(tokens, tags)

	mostProbablePOS = mostProbablePOS(unigrams)