import os
import csv 

csvpath = os.path.join("Resources","budget_data.csv")

total_months = 0 
total_profit_loss = 0 
changes = [] 
dates = [] 

with open(csvpath) as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    data = list(reader)


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader)
    previous_profit_loss = 0
    for row in csvreader:
        total_months += 1 
        total_profit_loss += int(row[1]) 

        current_profit_loss = int(row[1])
        if total_months > 1:
            monthly_change = current_profit_loss - previous_profit_loss
            changes.append(monthly_change)
            dates.append(row[0]) 
        previous_profit_loss = current_profit_loss

    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit_loss}")

    average_change = round(sum(changes) / len(changes),2)
    print(f"Average Change: ${average_change}")

    greatest_increase = max(changes)
    greatest_increase_date = dates[changes.index(greatest_increase)]
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")

   
    greatest_decrease = min(changes)
    greatest_decrease_date = dates[changes.index(greatest_decrease)]
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

filepath = os.path.join("analysis","financial_analysis.txt")


with open(filepath, "w") as file:
    file.write("Financial Analysis:\n")
    file.write("-----------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profit_loss}\n")
    file.write(f"Average Change: ${average_change}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
