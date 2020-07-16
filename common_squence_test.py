names = ['A','B','C']

print(('F' in names))
print("I am keroro haha.")
print("keroro" in "I am keroro haha.")

print(names)
# Result = ['A', 'B', 'C']
names.reverse()
print(names)
# Result = ['C', 'B', 'A']

nums_test = [1,123,123456]
nums_test.append(123456789)
print(len(nums_test))
print(min(nums_test))
print(max(nums_test))
nums_test.append("TESTTEST")
print(nums_test)
# Result = [1, 123, 123456, 123456789] [1, 123, 123456, 123456789, 'TESTTEST']

nums_test.reverse()
print(nums_test)
# Result = [123456789, 123456, 123, 1] ['TESTTEST', 123456789, 123456, 123, 1]
