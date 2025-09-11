line=input().split()
op,nums=line[1],[int(line[0]),int(line[2]),int(line[4])]

match(op):
    case "+":
        if nums[0] + nums[1]==nums[2]:
            print("Yes")
        else:
            print(nums[0]+nums[1])
    case "-":
        if nums[0] - nums[1]==nums[2]:
            print("Yes")
        else:
            print(nums[0]-nums[1])
    case "*":
        if nums[0] * nums[1]==nums[2]:
            print("Yes")
        else:
            print(nums[0]*nums[1])
     