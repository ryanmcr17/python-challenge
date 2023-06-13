# define variables for final outputs
total_months = 0
total_profit = 0
avg_MoM_change = 0.0
max_MoM_increase = 0
max_MoM_decrease = 0


# import CSV module for reading data file

import csv


# read data file

with open('/Users/mcrey/bootcamp/work/challenges/03-Python/python-challenge/PyBank/Resources/budget_data.csv') as data_file:
    
    months_list = []
    monthly_profits_list = []
    MoM_changes_list = []
    
    data = csv.reader(data_file)


    # process reader object into separate lists for each column, excluding column headers

    for row in data:
        
        if row[0] != 'Date':
            months_list.append(row[0])
        
        if row[1] != 'Profit/Losses':
            monthly_profits_list.append(int(row[1]))


    # create and fill list of MoM changes in monthly profit
    num_MoM_changes = len(monthly_profits_list) - 1

    for i in range(num_MoM_changes):
        MoM_changes_list.append(monthly_profits_list[i+1] - monthly_profits_list[i])
        
    
    # calculate and print results

    total_months = len(months_list)
    total_profits = sum(monthly_profits_list)
    avg_MoM_change = round(sum(MoM_changes_list) / len(MoM_changes_list),2)
    max_MoM_increase = max(MoM_changes_list)
    max_MoM_decrease = min(MoM_changes_list)

    max_increase_index = MoM_changes_list.index(max_MoM_increase)
    max_decrease_index = MoM_changes_list.index(max_MoM_decrease)

    max_increase_date = months_list[max_increase_index+1]
    max_decrease_date = months_list[max_decrease_index+1]

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: {total_profits}")
    print(f"Average Change: ${avg_MoM_change}")
    print(f"Greatest Increase in Profits: {max_increase_date} (${max_MoM_increase})")
    print(f"Greatest Decrease in Profits: {max_decrease_date} (${max_MoM_decrease})")
    
    with open('analysis/results_file.txt', 'w') as results_file:
        print("Financial Analysis",file=results_file)
        print("----------------------------",file=results_file)
        print(f"Total Months: {total_months}",file=results_file)
        print(f"Total: {total_profits}",file=results_file)
        print(f"Average Change: ${avg_MoM_change}",file=results_file)
        print(f"Greatest Increase in Profits: {max_increase_date} (${max_MoM_increase})",file=results_file)
        print(f"Greatest Decrease in Profits: {max_decrease_date} (${max_MoM_decrease})",file=results_file)
        