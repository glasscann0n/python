def main():
    counting_dupes("abcde")
    counting_dupes("aabbcde")
    counting_dupes("indivisibility")
    counting_dupes("Indivisibilities")
    counting_dupes("aA11")
    counting_dupes("ABBA")

def counting_dupes(string):
    string = string.lower()
    occurrences={}
    theletters = list(occurrences.keys())
    count = 0
    for i in string:
        if i.isalpha():
            if i in occurrences:  # occurred before?
                previousCount = occurrences[i]
                occurrences[i] = previousCount + 1
            else:
                occurrences[i] = 1
        else:
            pass
    for repeats in occurrences:
        times = occurrences[repeats]
        if times == 1:
            pass
        else:
            count +=1
    print (count)
    return count

main()