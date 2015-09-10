import os
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
from nltk.tag.mapping import map_tag
import numpy as np
import pickle
from textstat.textstat import textstat
from pattern.en import parse
from nltk.util import bigrams


def predict(data):
    """
    load classifiers from pickle files
    applying feature extractors on data
    compute the predicted values using the classifier
    :param data: text file
    :return:two predicted values for age and gender
    """
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, "gender_classifier.pickle")
    f = open(file_path)
    classifier = pickle.load(f)
    f.close()
    pred_gender = classifier.classify(gender_feature(data, create_feature_vect('gender_words.txt')))

    file_path = os.path.join(module_dir, "age_classifier.pickle")
    f = open(file_path)
    classifier = pickle.load(f)
    f.close()
    pred_age = classifier.classify(gender_feature(data, create_feature_vect("age_words.txt")))
    return pred_gender, pred_age


def gender_feature(text, feature_vect):
    """
    Extract the gender features
    :param text:
    :param feature_vect: contains a bag of words and a list of bigrams
    :return: a dictionary which contains the feature and its computed value
    """
    #sentence length and vocab features
    tokens = word_tokenize(text.lower())
    sentences = sent_tokenize(text.lower())
    words_per_sent = np.asarray([len(word_tokenize(s)) for s in sentences])

    #bag_of_word features
    bag_dict = {}
    for bag in feature_vect[:29]:
        bag_dict[bag] = bag in tokens

    #bigrams features
    bigram_dict = {}
    for big in feature_vect[29:]:
        bigram_dict[big] = big in bigrams(tokens)

    #POS tagging features
    POS_tag = ['ADJ', 'ADV', 'DET', 'NOUN', 'PRT', 'VERB', '.']
    tagged_word = parse(text, chunks=False, tagset='UNIVERSAL').split()
    simplified_tagged_word = [(tag[0], map_tag('en-ptb', 'universal', tag[1])) for s in tagged_word for tag in s]
    freq_POS = nltk.FreqDist(tag[1] for tag in simplified_tagged_word if tag[1] in POS_tag)

    d = dict({'sentence_length_variation': words_per_sent.std()}, **bag_dict)

    return dict(dict(d, **bigram_dict), **freq_POS)


def age_feature(text, feature_vect):
    """
    Extract age features
    :param text:
    :param feature_vect: contains a bag of words
    :return:a dictionary which contains the feature and its computed value
    """
    tokens = word_tokenize(text.lower())
    features={}
    for word in feature_vect:
        features['contains(%s)' % word] = (word in set(tokens))
    return dict(features, **dict({'FRE': textstat.flesch_reading_ease(text), 'FKGL': textstat.flesch_kincaid_grade(text)}))


def create_feature_vect(file_name):
    """
    upload for each class list of element needed in the feature extractor function
    :param file_name: path of the pickle file containing the desired list
    :return:feature list
    """
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, file_name)
    fp2 = open(file_path)
    feature_vect = pickle.load(fp2)
    fp2.close()
    return feature_vect