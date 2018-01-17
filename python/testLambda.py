# lambda parameters: expression
# expression不能包含分支或循环，但是可以包括条件
#

test_lam = lambda x: "Y" if x == 1   else "X"
print(test_lam(1))
print(test_lam(2))

