import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer
from nltk.corpus import stopwords
from nltk.corpus import state_union, gutenberg, wordnet, movie_reviews
from nltk.stem import WordNetLemmatizer
import random
sent = 'hello today i\'ve learned about nltk and it sounds great! Mr. teacher told us something that striked us. Really.'


words = word_tokenize(sent)
# print(words)
# print('------------------------------')

stopWordsSet = set(stopwords.words('english'))

filteredSent = [w for w in words if not w in stopWordsSet]
# print(filteredSent)

text = state_union.raw('2006-GWBush.txt')
tokenized = sent_tokenize(text)

bible = gutenberg.raw('bible-kjv.txt')
tokenized_bible = sent_tokenize(bible[5:1500])


'''
POS tag list:

CC	coordinating conjunction
CD	cardinal digit
DT	determiner
EX	existential there (like: "there is" ... think of it like "there exists")
FW	foreign word
IN	preposition/subordinating conjunction
JJ	adjective	'big'
JJR	adjective, comparative	'bigger'
JJS	adjective, superlative	'biggest'
LS	list marker	1)
MD	modal	could, will
NN	noun, singular 'desk'
NNS	noun plural	'desks'
NNP	proper noun, singular	'Harrison'
NNPS	proper noun, plural	'Americans'
PDT	predeterminer	'all the kids'
POS	possessive ending	parent's
PRP	personal pronoun	I, he, she
PRP$	possessive pronoun	my, his, hers
RB	adverb	very, silently,
RBR	adverb, comparative	better
RBS	adverb, superlative	best
RP	particle	give up
TO	to	go 'to' the store.
UH	interjection	errrrrrrrm
VB	verb, base form	take
VBD	verb, past tense	took
VBG	verb, gerund/present participle	taking
VBN	verb, past participle	taken
VBP	verb, sing. present, non-3d	take
VBZ	verb, 3rd person sing. present	takes
WDT	wh-determiner	which
WP	wh-pronoun	who, what
WP$	possessive wh-pronoun	whose
WRB	wh-abverb	where, when
'''


def process_content():
    try:
        for sent in tokenized_bible:
            words = nltk.word_tokenize(sent)
            tagged = nltk.pos_tag(words)

            chunkGram = r"""Chunk: {<.*>+}
                                }<VB.?| IN " DT>+{"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            print(sent)
            chunked.draw()

    except Exception as e:
        print(str(e))


# process_content()

def process_content_2():

    for sent in tokenized_bible:
        words = nltk.word_tokenize(sent)
        tagged = nltk.pos_tag(words)

        namedEnt = nltk.ne_chunk(tagged)
        namedEnt.draw()


# process_content_2()

# lemmatizer = WordNetLemmatizer()
# print(lemmatizer.lemmatize('cats'))
# print(lemmatizer.lemmatize('cacti'))
# print(lemmatizer.lemmatize('geese'))
# print(lemmatizer.lemmatize('done',pos="v"))


# syns = wordnet.synsets('program')

# #synset
# print(syns[0].name())

# #just word
# print(syns[0].lemmas()[0].name())

# #definition
# print(syns[0].definition())

# #examples
# print(syns[0].examples())


synonyms = []
antonyms = []

for syn in wordnet.synsets('good'):
    for l in syn.lemmas():
        synonyms.append(l.name())
    if l.antonyms():
        antonyms.append(l.antonyms()[0].name())

# print(set(synonyms))
# print('---------------------------')
# print(set(antonyms))


# w1 = wordnet.synset('book.n.01')
# w2 = wordnet.synset('movies.n.01')
# print(w1)
# print(w2)
# print(w1.wup_similarity(w2))

documents = [(list(movie_reviews.words(fileid)), category)
           for category in movie_reviews.categories()
           for fileid in movie_reviews.fileids(category)]

#the one line is equivalent to:
'''
documet = []
for caegory in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
           document.append((list(movie_reviews.words(fileid)),category)
'''


random.shuffle(documents)
#print(documents[1], end ='\n-----\n')

all_words = []
for w in movie_reviews.words():
        all_words.append(w.lower())
all_words = nltk.FreqDist(all_words)
print(type(all_words))
print(all_words["stupid"])