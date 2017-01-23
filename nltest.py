from nltk.tag import pos_tag
import string

sentence = "Where can I find McDonald's?"
exclude = set('!?.,')
sentence = ''.join(ch for ch in sentence if ch not in exclude)
tagged_sent = pos_tag(sentence.split())
print tagged_sent

propernouns = [word for word, pos in tagged_sent if pos == 'NN' or pos == 'NNP']
print propernouns 

#take tweet
#exclude 
#tag/split
#propernouns
#search each proper noun
