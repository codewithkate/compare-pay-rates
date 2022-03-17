# Produce hourly pay rate and compare
# Input list total days and hours worked, monthly pay, and an hourly pay to compare


# Input hours
print("How many days did you work this period?")
days = int(input())
list_hrs = []
tot_hrs = 0

for i in range(days):
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

        
# Print Calculations
print(f"\nTotal hours worked:", hrs)
print(f"Hourly pay rate:", payrate(pay,hrs))

# Print Comparisons
print("\nEnter rate to compare:")
comp = compare(int(input()))
