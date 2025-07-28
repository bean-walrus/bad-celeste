def getQuizAverages(scores):
    total = dict()
    count = dict()
    for person in scores:
        for quiz in scores[person]:
            if quiz not in total:
                total[quiz] = scores[person][quiz]
                count[quiz] = 1
            else:
                total[quiz] += scores[person][quiz]
                count[quiz] += 1
    toReturn = dict()
    for quiz in total:
        if quiz not in toReturn:
            toReturn[quiz] = total[quiz] // count[quiz]
    return toReturn


scores = {
 'Ann': { 'quiz1': 90, 'quiz2': 80, 'quiz3': 85 },
 'Ben': { 'quiz1': 70, 'quiz3': 95 },
 'Cam': { 'quiz2': 90 },
 'Del': dict(),
 }

print(getQuizAverages(scores))

assert(getQuizAverages(scores) == { 'quiz1': 80,
                                    'quiz2': 85,
                                    'quiz3': 90})
