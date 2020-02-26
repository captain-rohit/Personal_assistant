from nltk import NaiveBayesClassifier
from nltk.tokenize import word_tokenize
import csv, pickle, os.path


# Global variables
ALL_WORDS  = None
CLASSIFIER = None


# Initialize the classifier for command classification
def init():
	global ALL_WORDS
	global CLASSIFIER
	training_data = []

	if os.path.exists("classifier_data.pickle"):
		#Read from a pickle file
		classifier_file = open('classifier_data.pickle', 'rb')
		CLASSIFIER      = pickle.load(classifier_file)
		classifier_file.close()
		vocabulary_file =  open('vocabulary_data.pickle', 'rb')
		ALL_WORDS       = pickle.load(vocabulary_file)
		vocabulary_file.close()

	else:
		file   = open("training_data.csv", 'r') # Training data
		reader = csv.reader(file)
		print(reader)
		for row in reader:
			training_data.append((row[0], row[1]))

		file.close()

		ALL_WORDS       = set(word.lower() for passage in training_data for 
			                  word in word_tokenize(passage[0]))
		trainig_object  = [({word: (word in word_tokenize(x[0])) for word in 
			                 ALL_WORDS}, x[1]) for x in training_data]
		CLASSIFIER      = NaiveBayesClassifier.train(trainig_object)
		#Dump in a pickle file
		classifier_file = open('classifier_data.pickle', 'wb')
		pickle.dump(CLASSIFIER, classifier_file)
		classifier_file.close()
		vocabulary_file = open('vocabulary_data.pickle', 'wb')
		pickle.dump(ALL_WORDS, vocabulary_file)
		vocabulary_file.close()


# Decodes the given command baased on the classifier
def decode_command(command):
	global ALL_WORDS
	global CLASSIFIER

	test_sent_features = {word.lower(): (word in word_tokenize(
						  command.lower())) for word in ALL_WORDS}
	return CLASSIFIER.classify(test_sent_features)
init()