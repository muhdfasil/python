number=input("Enter the numbers with space:")
num=[int(x) for x in number.split()]
result=['over' if x>100 else x for x in num]
print(result)
# number=[]
# limit=int(input("Enter the limit:"))
# for x in range(limit):
#     a=int(input("Enter the number:"))
#     number.append(a)
# for x in number:
#     if x>100:
#         number[x]='over'
# print(number)