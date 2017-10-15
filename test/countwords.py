def word_count(string):
    tokens = string.split()
    n_tokens = len(tokens)
    print(n_tokens)

# Test the code.
print(word_count("Hello World!"))
print(word_count("The quick brown fox jumped over the lazy dog."))
