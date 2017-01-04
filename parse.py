# -*- coding: utf-8 -*-
from nltk.tokenize import word_tokenize

#Import custom stopwords from file
stopwords_file = open('stopwords.txt', 'r')
stopwords = [x for x in stopwords_file.read().split()]

sample_string =  "Not so much a pale ale as an India Pale Ale. However, with as overly hopped as many of their beers are, I guess compared to them this one wouldnt be quite so bitter. Truly dont like this. Cascade is hideous, lager/epa like hop. I only drink beer for these new fandangled fruity new world hops, not boring English tasting floral spicey rubbish. But at least Ive narrowed down that filthy hop at last, this is why ratebeer is such a good idea. Bottle. Pours orange with a white head. Aroma is sweet and hoppy. Taste is sweet but the finish is bitter. Dammit. I thought Id be the first to review this... Ok, lets assume this is my 9 millionth so I best actually do this. Caramel, soft sweet orange, toasted malts, bit o pine, honey aroma. Mellow yet obvious bitterness. Bready malts with the caramel being minor, orange, pine, more citrus, the underbelly of faint spice. Finishes clear. Yumtime. 11/20 not spectacular but a decent pub/supermarket option. Piney taste, mild bitterness, easy to drink but not enough flavour for me "

#Tokenize string
words = word_tokenize(sample_string.lower())

#Remove stopwords
important_words = filter(lambda x: x not in stopwords, words)

print important_words



#Remove stopwords
important_words = filter(lambda x: x not in stopwords, words)





