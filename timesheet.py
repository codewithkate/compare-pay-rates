# Number -> TextFile
# Produce hourly pay rate and compare
# Given monthly pay and inputs for hours and comparative pay


# Input hours
list_hrs = []
tot_hrs = 0

for i in range(1,4):
    print("Day",i)
    inp = int(input())   
    list_hrs.append(inp)
    tot_hrs = sum(list_hrs)


# Variables for pay rates
print("\nEnter period pay:")
pay = int(input())
hrs = tot_hrs

# Average pay rate
def payrate(p,h):
    avg = (pay / hrs)
    return int(avg)


# Compare to other rates
current_rate = payrate(pay,hrs)

def compare(other_rate):
    if current_rate < other_rate: 
        print("You are underpaid.")
    else:
        print("You earn above the average pay rate.")

        
# Print Calculations and Relations
print(f"\nTotal hours worked:", hrs)
print(f"Hourly pay rate:", payrate(pay,hrs))
print("\nEnter rate to compare:")
comp = compare(int(input()))
