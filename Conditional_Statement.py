if True: # 파이썬은 대문자로 시작
    print("Python True1")
    print("Python True2")
# 파이썬은 같은 Indent를 하나의 그룹으로 보고 다른 indent가 나오기전까지를 수행한다.
print("Python True3")
# 파이썬은 Indent에 민감하다.

input = 22
real = 456456

if input == real:
    print("the same")
elif input != real: # else if -> elif
    print("different")
else:
    print("Nothing")
