line=input().split()
op,nums=line[1],[int(line[0]),int(line[2])]

match(op):
    case "<":
        if nums[0] < nums[1]:
            print("Right")
        else:
            print("Wrong")
    case ">":
        if nums[0] > nums[1]:
            print("Right")
        else:
            print("Wrong")
    case "=":
        if nums[0] == nums[1]:
            print("Right")
        else:
            print("Wrong")