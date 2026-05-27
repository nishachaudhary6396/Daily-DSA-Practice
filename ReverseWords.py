def reverse_words(sentence):
    words = sentence.split()
    
    reversed_words = words[::-1]
    
    result = " ".join(reversed_words)
    
    return result

input_text = "Python is fun"
print(reverse_words(input_text))