def getCount(inputStr):
    num_vowels = 0
    vowels = ['a', 'e', 'i', 'o', 'u']


    for i in inputStr:
        for o in vowels:
            if i == o:
                num_vowels += 1

    return num_vowels