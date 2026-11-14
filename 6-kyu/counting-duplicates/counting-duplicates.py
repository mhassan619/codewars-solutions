def duplicate_count(text):
    text = text.lower()
    checked = []
    score = 0
    for i in text:
        if text.count(i) > 1 and i not in checked:
            score += 1
        checked.append(i)
    return score