import os
import csv

budget_csv = os.path.join("..", "Resources", "budget_data.csv")

# Open and read csv
with open(budget_csv) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=",")
	header = next(csv_reader)
	
	# Assign variables
	total_months = []
	total_profit = []
	profit_change = []
	
	for row in csv_reader:
		# Calculate total number of months
		total_months.append(row[0])
		months = len(total_months)

		# Calculate net total amount of "Profit/Losses" over the entire period
		total_profit.append(int(row[1]))
		profits = sum(total_profit)
	# Calculate the changes in "Profit/Losses" over the entire period
	for i in range(len(total_profit)-1):
		change = int(total_profit[i+1]) - int(total_profit[i])
		profit_change.append(change)
		avg = sum(profit_change)/len(profit_change)

	# Find the greatest increase in profits (date and amount) over the entire period
	greatest_profit = max(profit_change)
	j = profit_change.index(greatest_profit)
	greatest_month = total_months[j+1]
	
	# Find the greatest decrease in losses (date and amount) over the entire period
	least_profit = min(profit_change)
	k = profit_change.index(least_profit)
	least_month = total_months[k+1]

# Print analysis
results = (
"Financial Analysis\n"
"----------------------------\n"
f"Total number of Months: {months}\n"
f"Total: ${profits}\n"
f"Average Change: ${round(avg, 2)}\n"
f"Greatest increase in profits on {greatest_month}: (${greatest_profit})\n"
f"Greatest decrease in profits on {least_month}: (${least_profit})\n")
print(results)

# output path
output = os.path.join(".","financial analysis.txt")
with open(output, "w") as text_file:
	text_file.write(results)
	