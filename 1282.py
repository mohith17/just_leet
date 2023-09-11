# 1282. Group the People Given the Group Size They Belong To
# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/?envType=daily-question&envId=2023-09-11

a = list(map(int, input().split(",")))
d = dict()
for i in range(len(a)):
    if a[i] in d:
        d[a[i]].append(i)
    else:
        d[a[i]] = [i]

ans = []
for i in d:
    temp = []
    for j in d[i]:
        temp.append(j)
        if len(temp) == i:
            ans.append(temp[:])
            temp = []
print(ans)


# notes: instead of using a dict and then
# dininding into sub arrays, we can simply
# check for size==i condition in dict itself
# and whenever the condition is true just add it
# to the result and empty the temp dict arr.
