# first line: 1
@memory.cache
def stemmed_wrapper(term):
    return stemmer.stem(term)
