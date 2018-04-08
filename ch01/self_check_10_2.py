wordlist = ['cat', 'dog', 'rabbit']
letterlist = [ch for ch in "".join(wordlist)]
letterlist = list(set(letterlist))
print(letterlist)
