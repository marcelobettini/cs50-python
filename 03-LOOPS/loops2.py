nums = [0,1,2,3]
# nums = range(4)
for num in nums:
    print(num)

for num in range(4):
    print(num)

# I don't need or care the counter i, so I put _
for _ in range(4):
    print("miau!!")

# and this? Amazing! end="" to avoid extra CR in the end, because that the default ending for print function
print("guau!!\n" * 3, end="")