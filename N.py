import itertools

joined_list = []
k = []
accepts = input("enter your word : \n")
new_input = accepts.lower()
num = len(accepts)
perm = []
final = []
while num > 1:
    permutation = itertools.permutations(new_input, num)
    num -= 1
    for i in permutation:
        con = "".join(i)
        perm.append(con)
val = [] 
with open("dict.txt", "r") as f:
    f2 = list(f.readlines())

    for x in f2:
        j = list(x.strip())
        joined_list.append(j)
    for i in joined_list:
        con = "".join(i)
        k.append(con)
    for words in k:
        new_words = words.lower()
        val.append(new_words)
for wrd in perm:
    for wd in val:
        if wd == wrd:
            print(wd)
f.close()
