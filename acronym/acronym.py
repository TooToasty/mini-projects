def abbreviate(sentence):
    ac = ""
    sentence = sentence.replace("_", " ")
    sentence = sentence.replace("-", " ")
    words = [word for word in sentence.split()]
    new_words = []
    for word in words:
      word.strip("!!&@$%^:&:.")
      new_words.append(word)
    for word in new_words:
        ac += word[0].upper()
    return ac
