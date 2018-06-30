## PyPoll

# ![Vote-Counting](Images/Vote_counting.jpg)

# * In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. 
# (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, 
# his concentration isn't what it used to be.)

# * You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). 
# The dataset is composed of three columns: 
# `Voter ID`, `County`, and `Candidate`. 
# Your task is to create a Python script that analyzes the votes and calculates each of the following:

#   * The total number of votes cast
#   * A complete list of candidates who received votes
#   * The percentage of votes each candidate won
#   * The total number of votes each candidate won
#   * The winner of the election based on popular vote.

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
#   ```

# * In addition, your final script should both print the analysis to the terminal and export a 
# text file with the results.
#-------------------------------------------------------------------

## Import Modules
import os
import csv

## Use the os module to read file path
csv_Path = os.path.join("Resources", "election_data.csv")
# print(csv_Path)

# Total Votes counter
TotalVotes = 0
WinningVoteCount = 0
WinningCandidate = ""
WinningPercent = 0.00

# Create lists 
CandidatesWithVotes = []
CandidateVotes = {}


## Open the CSV
with open(csv_Path, newline = "") as csv_File:

  # Initiate csv reader
  csv_Reader = csv.reader(csv_File, delimiter = ",")
  # print(csv_Reader)

  # Read Header row
  csv_Header = next(csv_File)
  # print(f'\nHeader: {csv_Header}')

  # Read each row of data
  for x in csv_Reader:

    # Add to the total votes
    TotalVotes = TotalVotes + 1

    # Extract candidate name 
    CandidateName = x[2]
   
    # If Candidate not in existing Candidate With Votes list...
    if CandidateName not in CandidatesWithVotes:

      # Add Candidate to the list
      CandidatesWithVotes.append(CandidateName)

      # Track Candidate votes
      CandidateVotes[CandidateName] = 0
    
    # Add a vote to the Candidates count
    CandidateVotes[CandidateName] = CandidateVotes[CandidateName] + 1


    # Loop through the candidates to determine winner
    for y in CandidateVotes:
      
      # Determine vote counts and percentages
      Votes = CandidateVotes.get(CandidateName)
      VotePercent = (float(Votes) / float(TotalVotes)) * 100

      # Determine the Winner
      if Votes > WinningVoteCount:
        WinningVoteCount = Votes
        WinningCandidate = CandidateName
        WinningPercent = round((WinningVoteCount / TotalVotes) * 100 , 2)

  # Loop through candidates and print votes and percentage
  for k, v in CandidateVotes.items():
    Percent = (v / TotalVotes) * 100
    print(k , v , str(round(Percent,2)) + "%")
    

# Print Output  
print(f'\nTotal Votes: {TotalVotes}')
print(f'\nWinner: {WinningCandidate} with {WinningVoteCount} votes ({WinningPercent}%).')


# Use os module to specify output file to WRITE to
csv_Output_Path = os.path.join("bpina_PyPoll_Output.txt")

# Open the output file using WRITE mode
with open(csv_Output_Path, "w", newline = "") as csv_File_Out:

    # Initialize csv.writer
    csv_Writer = csv.writer(csv_File_Out)

    # Write results to text file
    csv_Writer.writerow(["Results"])
    csv_Writer.writerow(["----------"])
    csv_Writer.writerow(["Total Votes: " + str(TotalVotes)])
    csv_Writer.writerow(["----------"])

    # Loop through candidates and print votes and percentage
    for k, v in CandidateVotes.items():
      Percent = (v / TotalVotes) * 100
      csv_Writer.writerow([k , v, str(round(Percent,2)) + "%"]) 

    # Output winner
    csv_Writer.writerow(["----------"])
    csv_Writer.writerow(["Winner: " + WinningCandidate + " with " + 
                          str(WinningVoteCount) + " votes (" + str(WinningPercent) + "%)."])
