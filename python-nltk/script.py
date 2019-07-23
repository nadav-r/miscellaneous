import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer
from nltk.corpus import stopwords
from nltk.corpus import state_union,gutenberg
sent = 'hello today i\'ve learned about nltk and it sounds great! Mr. teacher told us something that striked us. Really.'


words = word_tokenize(sent)
# print(words)
# print('------------------------------')

stopWordsSet = set(stopwords.words('english'))

filteredSent = [w for w in words if not w in stopWordsSet]
# print(filteredSent)

text = state_union.raw('2006-GWBush.txt')
tokenized = sent_tokenize(text)

blake = gutenberg.raw('blake-poems.txt')
tokenized_blake = sent_tokenize(blake)
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
        for sent in tokenized_blake:
            words = nltk.word_tokenize(sent)
            tagged = nltk.pos_tag(words)
            
            chunkGram = r"""Chunk: {<JJ><NN>}"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            chunked.draw()
    except Exception as e:
        print(str(e))
process_content()