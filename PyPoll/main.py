import os 
import csv 


csvpath = os.path.join("..", "Resources", "election_data.csv")

#making lists to store data
totalVotes = 0
khanCount = 0
correyCount = 0
liCount = 0
otooleyCount = 0
khanPercent = 0
correyPercent = 0
liPercent = 0 
otooleyPercent = 0
candidateTotals = []
names = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    #skips first row (header) and stores it 
    header=next(csvreader)
    
    for row in csvreader:

        #conditionals to check if the name in the row is equivalent to the candidate
        #if yes, the count will increment by one
       totalVotes = totalVotes + 1
       if(row[2] == "Khan"):
           khanCount = khanCount + 1
       if(row[2] == "Correy"):
           correyCount = correyCount + 1
       if(row[2] == "Li"):
           liCount = liCount + 1
       if(row[2] == "O'Tooley"):
           otooleyCount = otooleyCount + 1

    #creating a list of the candidate's names
    names.append("Khan")
    names.append("Correy")
    names.append("Li")
    names.append("O'Tooley")

    #creating a list of the candidates's total votes
    candidateTotals.append(khanCount)
    candidateTotals.append(correyCount)
    candidateTotals.append(liCount)
    candidateTotals.append(otooleyCount)

    #using max and index to find the highest number of total votes as well as the index
    winnerIndex = candidateTotals.index(max(candidateTotals))
    
    #setting the name of the winner
    nameOfWinner = names[winnerIndex]
    
    #simple equation to calculate the percent votes each candidate got out of the total votes
    khanPercent = round(((khanCount / totalVotes)*100),2)
    correyPercent = round(((correyCount / totalVotes)*100),2)
    liPercent = round(((liCount/ totalVotes)*100), 2)
    otooleyPercent = round(((otooleyCount / totalVotes)*100),2)

    #print to test results to see if they are correct 
    print ("Election Results")
    print ("---------------------")
    print ("Total Votes: " + str(totalVotes)) 
    print ("Khan: " + str(khanPercent) + " " + str(khanCount)) 
    print ("Correy: " + str(correyPercent) + " " + str(correyCount))
    print ("Li: " + str(liPercent) + " " + str(liCount))
    print ("O'Tooley: " + str(otooleyPercent) + " " + str(otooleyCount))
    print ("---------------------")
    print ("Winner: " + nameOfWinner)
    print ("---------------------")

    #writing the results to a seperate text file in the PyPoll folder
output_file = os.path.join("PyPoll_results.txt")
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Election Results"])
    writer.writerow(["---------------------"])
    writer.writerow(["Total Votes: " + str(totalVotes)])
    writer.writerow(["---------------------"]) 
    writer.writerow(["Khan: " + str(khanPercent) + "% | " + str(khanCount)]) 
    writer.writerow(["Correy: " + str(correyPercent) + "% | " + str(correyCount)])
    writer.writerow(["Li: " + str(liPercent) + "% | " + str(liCount)])
    writer.writerow(["O'Tooley: " + str(otooleyPercent) + "% | " + str(otooleyCount)])
    writer.writerow(["---------------------"])
    writer.writerow(["Winner: " + nameOfWinner])
    writer.writerow(["---------------------"])