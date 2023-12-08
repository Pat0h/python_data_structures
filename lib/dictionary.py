import string


def word_frequency(sentence):
    sentence = sentence.translate(str.maketrans('', '', string.punctuation)).lower()

    words = sentence.split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


statement = 'This is a test sentence. This is a test sentence'
result = word_frequency(statement)
print(result)
