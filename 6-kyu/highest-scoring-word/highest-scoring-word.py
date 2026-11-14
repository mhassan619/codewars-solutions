def high(x):
    words = x.split(" ")
    scores = []
    score = 0
    for word in words:
        for i in word:
            score += ord(i) - 96
        scores.append(score)
        score = 0
    max_idx = 0
    for i in range(1,len(scores)):
        if scores[i] > scores[max_idx]:
            max_idx = i
    return words[max_idx]