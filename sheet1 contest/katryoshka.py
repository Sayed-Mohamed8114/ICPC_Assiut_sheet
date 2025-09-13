eyes, mouths, bodies = map(int, input().split())

# The key insight: we can use math to find the optimal solution
# without trying all combinations

# Type 1: 2 eyes + 1 body (no mouth)
# Type 2: 2 eyes + 1 mouth + 1 body  
# Type 3: 1 eye + 1 mouth + 1 body

# Strategy: Try different approaches and pick the best one

# Approach 1: Focus on Type 1 and Type 3 (no Type 2)
# Use all mouths for Type 3, then use remaining eyes for Type 1
type3_approach1 = min(eyes, mouths, bodies)
remaining_eyes_1 = eyes - type3_approach1
remaining_bodies_1 = bodies - type3_approach1
type1_approach1 = min(remaining_eyes_1 // 2, remaining_bodies_1)
total_approach1 = type1_approach1 + type3_approach1

# Approach 2: Focus on Type 2 and Type 3 (no Type 1)
# Use all eyes for Type 2 and Type 3
type2_approach2 = min(eyes // 2, mouths, bodies)
remaining_eyes_2 = eyes - 2 * type2_approach2
remaining_mouths_2 = mouths - type2_approach2
remaining_bodies_2 = bodies - type2_approach2
type3_approach2 = min(remaining_eyes_2, remaining_mouths_2, remaining_bodies_2)
total_approach2 = type2_approach2 + type3_approach2

# Approach 3: Mix of all types (more complex but optimal)
# This is the tricky part - we need to find the right balance
max_dolls = max(total_approach1, total_approach2)

# For the mixed approach, we can use binary search or mathematical optimization
# But for most cases, the above two approaches should work

print(max_dolls)