

scores = [

   {"naam_student" : "xander", "score" : 48  },
   {"naam_student" : "xen", "score" : 76  },
   {"naam_student" : "jarne", "score" : 98 },
   

]


def hoogste_score(score):
    hoogsteScore = {}
    for i in score :
        if 60 <= i["score"] :
            hoogsteScore[i] = i[score]
    return hoogsteScore

print(hoogste_score(scores))





