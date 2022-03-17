# Produce hourly pay rate and compare
# Input list total days and hours worked, monthly pay, and an hourly pay to compare


# Variables for pay rates
print("\nEnter total pay:")
pay = int(input())
print("Enter total hours:")
hrs = int(input())

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
