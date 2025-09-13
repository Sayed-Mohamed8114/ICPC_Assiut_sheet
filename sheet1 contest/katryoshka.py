''' 
he can made dolls with this components 
1-Two eyes and one body.
2-Two eyes, one mouth, and one body.
3-One eye, one mouth, and one body.
'''
eyes,mouth,bodies=map(int,input().split())
max_dolls=0

#try all possible number of type doll 1 (2 eyes , 1 body)
for type1 in range(min(eyes//2,bodies)+1):
    remaining_eyes=eyes-2 * type1
    remaining_bodies= bodies - type1

    # try all possible number of type doll 2 (2 eyes,one mouth , one body)
    for type2 in range(min(remaining_eyes//2,mouth,remaining_bodies)+1):
        remaining_eyes_after_type2 = remaining_eyes - 2 * type2
        remaining_mouths = mouth - type2
        remaining_bodies_after_type2 = remaining_bodies - type2

         # Calculate type 3 dolls (1 eye + 1 mouth + 1 body)
        type3 = min(remaining_eyes_after_type2, remaining_mouths, remaining_bodies_after_type2)
        total_dolls = type1 + type2 + type3
        max_dolls = max(max_dolls, total_dolls)

        
print(max_dolls)


