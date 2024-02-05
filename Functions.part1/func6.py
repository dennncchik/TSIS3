def reversed_sentence(sentence):
    words = sentence.split()
    reversed_words = reversed(words)
    sentence_backwards = ' '.join(reversed_words)
    return sentence_backwards
my_sentence = input("enter your sentence:")
print(reversed_sentence(my_sentence))