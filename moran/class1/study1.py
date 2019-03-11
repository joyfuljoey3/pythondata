

def get_counts(seq):
    counts={}
    for x in seq:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1

    return counts


a = [1, 2, 3]

print(get_counts(a))
