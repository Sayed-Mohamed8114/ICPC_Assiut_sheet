nums=input().split()
arr=[int(nums[0]), int(nums[1])] 

operations=[(arr[0]+arr[1]),(arr[0]*arr[1]),(arr[0]-arr[1])]
print(f'{arr[0]} + {arr[1]} = {operations[0]}')
print(f'{arr[0]} * {arr[1]} = {operations[1]}')
print(f'{arr[0]} - {arr[1]} = {operations[2]}')
