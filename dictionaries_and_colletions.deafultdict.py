from itertools import permutations



name = "voldermort"
diagrams = set()
perms = {''.join(i)for i in permutations(name)}
for perm in perms:
    for i in range(0,len(perm)-1):
        diagrams.add(perm[i] + perm[i + 1])
print(*sorted(diagrams), sep='\n' )