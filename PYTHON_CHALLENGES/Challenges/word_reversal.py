# Write a function named reverse_words that reverses the order of words in a given sentence.

def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])


print(reverse_words('Hi this is Python!'))
