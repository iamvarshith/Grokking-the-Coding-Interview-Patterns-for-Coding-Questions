def checkMagazine(magazine, note):
    magazine_dict = {}
    size_note = len(note)
    for i in magazine:
        if i in magazine_dict.keys():
            magazine_dict[i] += 1
        else:
            magazine_dict[i] = 1
    for k in note:
        if k in magazine_dict:
            if magazine_dict[k] == 1:
                del magazine_dict[k]
                size_note -= 1
            else:
                magazine_dict[k] -= 1
                size_note -= 1
    if size_note == 0:
        print("Yes")
    else:
        print('No')


note = ['give', 'one', 'grand', 'today']
magazine = ['give', 'me', 'one', 'grand', 'today', 'night']

checkMagazine(magazine = magazine,note = note)
