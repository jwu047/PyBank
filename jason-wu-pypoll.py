
#Dependencies#Depend 
import os
import csv
#Set Path
csvpath = os.path.join("PyPoll","Resources","election_data.csv")

#Initialize variables
total_votes = 0
khan = 0
khan_p = 0
correy = 0
correy_p = 0
li = 0
li_p = 0
otooley = 0
otooley_p = 0
winner = 0

#Open csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    first_row = next(csvreader)
    
    #Loop through the rows
    for row in csvreader:
        total_votes += 1
        if row[2] == "Khan":
            khan += 1
        elif row[2] == "Correy":
            correy += 1
        elif row[2] == "Li":
            li += 1
        else: 
            otooley += 1
            
#Calculate the percentages
khan_p = (khan / total_votes) * 100
correy_p = (correy / total_votes) * 100
li_p = (li / total_votes) * 100
otooley_p = (otooley / total_votes) * 100

#There should be a more efficient way to do this, fix later...
if khan > correy and khan > li and khan > otooley:
    winner = "Khan"
elif correy > khan and correy > li and correy > otooley:
    winner = "Correy"
elif li > khan and li > correy and li > otooley:
    winner = "Li"
else:
    winner = "O'Tooley"


#Format data before final output
#For the votes
khan = '({:})'.format(khan)
li = '({:})'.format(li)
correy = '({:})'.format(correy)
otooley = '({:})'.format(otooley)
#For the percentages
khan_p = '{:.3f}%'.format(khan_p)
li_p = '{:.3f}%'.format(li_p)
correy_p = '{:.3f}%'.format(correy_p)
otooley_p = '{:.3f}%'.format(otooley_p)

#Print Result
print("Election Results\n"\
     + "-------------------------\n"\
     + "Total Votes: " + str(total_votes) + "\n"\
     + "-------------------------\n"\
     + "Khan: " + str(khan_p) + " " + str(khan) + "\n"\
     + "Correy: " + str(correy_p) + " " + str(correy) + "\n"\
     + "Li: " + str(li_p) + " " + str(li) + "\n"\
     + "O'Tooley: " + str(otooley_p) + " " + str(otooley) + "\n"\
     + "-------------------------\n"\
     + "Winner: " + winner + "\n"\
     + "-------------------------")

# Export Analysis to text file
f = open("PyPoll_Analysis.txt","w")
# Write inside
f.write("Election Results\n"\
     + "-------------------------\n"\
     + "Total Votes: " + str(total_votes) + "\n"\
     + "-------------------------\n"\
     + "Khan: " + str(khan_p) + " " + str(khan) + "\n"\
     + "Correy: " + str(correy_p) + " " + str(correy) + "\n"\
     + "Li: " + str(li_p) + " " + str(li) + "\n"\
     + "O'Tooley: " + str(otooley_p) + " " + str(otooley) + "\n"\
     + "-------------------------\n"\
     + "Winner: " + winner + "\n"\
     + "-------------------------")
f.close()