la = ["aaa","bbb","ccc"]
print(la)

la[2] = "ddd"
print(la)

la.insert(2,"ccc")
print(la)

la.insert(100,"fff")
print(la)

la.append("ggg")
print(la)

la.remove("ggg")
print(la)

la.pop(1)
print(la)

la += ["hhh"]
print(la)

la = la + ["iii","jjj"]
print(la)

lb = [1,2,3,4,5,6,7,8,9]

lb[0::2] = [0]*5

print(lb)