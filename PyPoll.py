# Add dependencies
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_results.txt")

# Initialize total vote counter
total_votes = 0

# Initialize {candidate: vote count} dictionary
candidate_dict = {}

# Initialize winning count variable
winning_count = 0
winner = ""
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)


    for row in file_reader:
        # Add to total vote count
        total_votes += 1

        # Candidate name is column 3 of each row
        candidate_name = row[2]

        # Add candidate name to dict, with vote count of 1, if not in dict
        if candidate_name not in candidate_dict:
            candidate_dict[candidate_name] = 1
        # If candidate name already exists in dict, increment vote count by 1
        else:
            candidate_dict[candidate_name] += 1

with open(file_to_save, "w") as txt_file:

    # Calculate final vote count
    election_results = (
        f"\nElection Results\n"
        f"--------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------------\n"
    )
    # Print final vote count to shell
    print(election_results, end="")

    # Save final vote count to text file
    txt_file.write(election_results)

    for candidate_name in candidate_dict:
        # Calculate and print percentage of votes for each candidate
        votes = candidate_dict[candidate_name]
        vote_percentage = float(votes)/float(total_votes) * 100
        
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print candidate results to shell
        print(candidate_results)
        # Save candidate results to text file
        txt_file.write(candidate_results)

        # Determine the winning candidate
        if votes > winning_count:
            winning_count = votes
            winner = candidate_name
            winning_percentage = vote_percentage

    winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winner}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------\n"
    )

    # Print winning candidate's results to shell
    print(winning_candidate_summary)
    # Save winning candidate's results to text file
    txt_file.write(winning_candidate_summary)