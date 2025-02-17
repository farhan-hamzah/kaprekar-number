num = int(input())
square = str(num ** 2)
length = len(square)  
left = square[:length // 2]   
right = square[length // 2:]  
left = int(left) if left else 0
right = int(right) if right else 0
if left + right == num:
    print(True)
else:
    print(False)