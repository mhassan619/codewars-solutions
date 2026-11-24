def find_uniq(xs):
    for n in set(xs):
        if xs.count(n) == 1:
            return n