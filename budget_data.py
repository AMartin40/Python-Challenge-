
import os
import csv

#CSV file path 
csvpath= os.path.join("budget_data.csv")

#Define variables 
Total_Months = []
Total_Net = 0
Avg_Change = []
Greatest_Increase_P = ""
Greatest_Decrease_L = ""

#Read CSV file
with open (csvpath) as csv_file:
    reader = csv.reader (csv_file)

    next(reader)

#For loop to Get Totals
    for row in reader:
     

    #Calulations 
        Total_Months.append(row[0])
        Total_Net.append(int(row [1]))

print("Financial Analysis")
print("-------------------------------")
print("Total Months: ", len(Total_Months))
print("Net Total: $", sum(Total_Net))



#Average changes over the entire period 
for i in range(1, len(Total_Net)):
    Avg_Change.append(Total_Net[i] - Total_Net[i-1])
    Change = sum(Avg_Change) / len(Avg_Change)



#Greatest increase in profits date and amount
    Increase = max(Avg_Change)
    Greatest_Increase_P = str(Total_Months[Avg_Change.index(max(Avg_Change))])


#Greatest decrease in losses date and amount
    Decrease = min(Avg_Change)
    Greatest_Decrease_L = str(Total_Months[Avg_Change.index(min(Avg_Change))])


print("Average Change: $", round(Change))  
print("Greatest Increase: ", Greatest_Increase_P, "($", Increase,")")
print("Greatest Decrease: ", Greatest_Decrease_L, "($", Decrease,")")




