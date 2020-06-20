import os 
import csv 

csvpath = os.path.join("..", "Resources", "budget_data.csv")

#making lists to store data
numberOfMonths = 0
netTotal = 0
averageChange = 0
values = []
difference = []
sumOfChanges = 0
date = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    #skips first row (header) and stores it 
    header = next(csvreader)
    

    for row in csvreader:
        
        #finding total at the end
        netTotal = netTotal + int(row[1])
        
        #conditional to control flow of for loop
        if  (numberOfMonths == 0):
            previousValue = int(row[1])

        else:
            diff = int(row[1]) - previousValue
            sumOfChanges = sumOfChanges + (diff)
            difference.append(diff)
            previousValue = int(row[1])
            
        numberOfMonths = numberOfMonths + 1
        date.append(row[0])
    
    #finding the greatest increase by using the max and index function
    greatestInc = max(difference)
    greatestIncMonthIndex = difference.index(greatestInc)+1
    greatestIncMonth = date[greatestIncMonthIndex]

    #finding the greatest decrease by using the min and index function
    greatestDec = min(difference)
    greatestDecMonthIndex = difference.index(greatestDec)+1
    greatestDecMonth = date[greatestDecMonthIndex]

    #calculating average change with simple formula 
    averageChange = sumOfChanges/(numberOfMonths-1)
    
    #printing results to check if they are correct 
    print ("Financial Analysis")
    print ("---------------------")
    print ("Total  Months: " + str(numberOfMonths))
    print ("Total: " + str(netTotal))
    print ("Average Change: " + str(averageChange))
    print ("Greatest Increase In Profits: " + greatestIncMonth + " " + "(" + str(greatestInc) + ")")
    print ("Greatest Decrease in Profits: " + greatestDecMonth + " " + "(" + str(greatestDec) + ")")

    #writing the results to a seperate text file in the PyBank folder
output_file = os.path.join("PyBank_results.txt")
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Financial Analysis"])
    writer.writerow(["--------------------"])
    writer.writerow(["Total  Months: " + str(numberOfMonths)])
    writer.writerow(["Total: " + str(netTotal)])
    writer.writerow(["Average Change: " + "$" + str(averageChange)])
    writer.writerow(["Greatest Increase In Profits: " + greatestIncMonth + " " + "(" + "$" + str(greatestInc) + ")"])
    writer.writerow(["Greatest Decrease in Profits: " + greatestDecMonth + " " + "(" + "$" + str(greatestDec) + ")"])
