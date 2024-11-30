def single_root_words(root_word, *other_words):
    same_words = []
    other_words_lower = [s.lower() for s in other_words]
    for i in other_words_lower:
        if root_word.lower() in i:
            same_words.append(i)
    return same_words

print(single_root_words('Fly', 'butterfLy', 'flight', 'FLYer', 'flier'))
print(single_root_words('bOOk', 'NOTEBOOK', 'fly', 'booklet', 'sky', 'sketchbook'))
print(single_root_words('Able', 'ability', 'enable', 'capability', 'disable'))