def all_variants(text):
    length = len(text)

    for i in range(length):
        yield text[i]

    for start in range(length):
        for end in range(start + 2, length + 1):
            yield text[start:end]


a = all_variants("abc")
for i in a:
    print(i)
