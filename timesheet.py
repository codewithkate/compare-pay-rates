# Number -> TextFile
# Produce average pay rate, 
# Compare to past average(s), desired average, and local average
# Write to TextFile with formatting
# Given monthly pay and input list of hours
#a_list = [1,2,3]
#b_list = []
#for i in range(3):
#    inp = int(input())    # Initial TypeError: str used as int
 #   b_list.append(inp)


#template
#def average(given_list):
#    avg = ( (sum(given_list)) / (len(given_list)) )
#    return int(avg)

# Average pay rate
print("Enter pay:")
pay = int(input())

print("Enter hours:")
hrs = int(input())

def payrate(p,h):
    avg = (pay / hrs)
    return int(avg)


print(f"Your average pay rate is:", payrate(pay,hrs))


