sentence = input("Enter a sentence:")
word_lengths = {word:len(word)for word in sentence.split()}
print("Length of each word:",word_lengths)