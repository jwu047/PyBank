import csv

total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = [0, 0]
greatest_decrease = [0, 0]
total_net = 0

# Read CSV
with open("Resources/budget_data.csv") as budget_data:
    reader = csv.reader(budget_data)
    header = next(reader)

    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:

        total_months += 1
        total_net += int(row[1])

        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list.append(net_change)
        month_of_change.append(row[0])

        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

# Calculate the Average Net Change
net_monthly_avg = sum(net_change_list) / len(net_change_list)

# Summary
summary = (f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Show on terminal
print(summary)

# Export to text file, create if does not exist with "a"
with open("analysis/budget_analysis.txt", "a") as txt:
    txt.write(summary)
