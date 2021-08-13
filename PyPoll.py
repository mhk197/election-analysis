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

# Print the total votes
print()
print(f"Total vote count: {total_votes:,}")
print()

# Initialize winning count variable
winning_count = 0
winner = ""
winning_percentage = 0

for candidate_name in candidate_dict:

    # Calculate and print percentage of votes for each candidate
    votes = candidate_dict[candidate_name]
    vote_percentage = float(votes)/float(total_votes) * 100
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})")

    # Determine the winning candidate
    if votes > winning_count:
        winning_count = votes
        winner = candidate_name
        winning_percentage = vote_percentage
print()

# Print the winning candidate
print(
    f"----------------------\n"
    f"Winner: {winner}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
)