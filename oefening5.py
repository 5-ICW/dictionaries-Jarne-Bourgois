

def frequentie_tekens(string):
    frequentie = {}
    for teken in string:
        if teken in frequentie:
            frequentie[teken] += 1
        else:
            frequentie[teken] = 1
    return frequentie


string = input("Geef een worrd in :")
print(frequentie_tekens(string))