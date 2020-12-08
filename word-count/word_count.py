def sort(sentence):
  sentence = sentence.replace(',',' ')
  sentence = sentence.replace('_',' ')
  words = [word for word in sentence.lower().split()]
  new_words = []
  for word in words:
    word.strip("!!&@$%^:&:.")
    new_words.append(word)
  return new_words

def count_words(string):
  all_words = sort(string)
  label_dict = {}
  for word in all_words:
    if word in label_dict:
      label_dict[word] = label_dict[word] + 1
    else:
      label_dict[word] = 1
  return label_dict

import re
from collections import Counter
def count_words(s):
    return Counter(re.sub("_|(\B')|('\B)|[^\w\d'\s]+", " ", s).lower().split())
