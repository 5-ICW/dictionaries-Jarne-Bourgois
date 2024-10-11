

boeken = [
    {"titel" : "Warriers cats", "Autheur" : "De Kesel" , "release date" : 2012 },
    {"titel" : "Cresent City3", "Autheur" : "Blomme" , "release date" : 2023 },
    {"titel" : "Dungen diver", "Autheur" : "Xen" , "release date" : 2024 }
]

def titel(boeks):
    for i in boeks :
        print(i["titel"])

titel(boeken)