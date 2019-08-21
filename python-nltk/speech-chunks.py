import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import inaugural
from nltk.stem import WordNetLemmatizer
import random
import pprint
import re


speech = inaugural.raw('2013-Obama.txt')
tokenizedSpeech = sent_tokenize(speech)
rndIndex = random.randint(0, len(tokenizedSpeech))
rndSent = tokenizedSpeech[rndIndex]
print('index: ', rndIndex)


def process_sent(sent):
    words = word_tokenize(sent)
    taggedWords = nltk.pos_tag(words)
    chunkGrammer = r"""Chunk: {<DT>?<JJ>*<NN>}
                    {<PRP.?>?<CD>?<JJ.?>?<NN.?>}
                    {<PRP>}"""
    chunkParser = nltk.RegexpParser(chunkGrammer)
    chunked = chunkParser.parse(taggedWords)
    #print(taggedWords, end= '\n--------\n')
    #print(chunked, end= '\n--------\n')
    # chunked.draw()
    nltk.app.chartparser_app.app()


# for sent in tokenizedSpeech:
#     process_sent(sent)
nltk.app.chartparser_app.app()
