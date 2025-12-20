text = input("Enter a String:")
words = text.split()
short_words_set = {word for word in words if len(word)<5}
print("words <5 letters(Set):",short_words_set)
