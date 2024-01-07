from itertools import permutations

def gens(str):
    perms = []
    for r in range(1, len(str) + 1):
        perm_tuples = permutations(str, r)
        for perm_tuple in perm_tuples:
            perm = ''.join(perm_tuple)
            perms.append(perm)
    return perms

def gen(str):
    perms = gens(str)
    perms.sort()
    output = ','.join(perms)
    return output

str = "abc"
x = gen(str)
print(x)