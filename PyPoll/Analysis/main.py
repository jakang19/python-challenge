import os
import csv

election_csv = os.path.join("..", "Resources", "election_data.csv")

with open(election_csv) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=",")
	header = next(csv_reader)
	
	# Assign variables
	total_votes = 0
	candidates = []
	candidate_votes = []

	for row in csv_reader:
		# Calculate total number of votes cast
		total_votes += 1
		
		# Tally votes if candidate is in candidates[]
		if row[2] in candidates:
			unique_candidate = candidates.index(row[2])
			candidate_votes[unique_candidate] = candidate_votes[unique_candidate] + 1
		# Else, add unique candidate to candidates[] and make a spot for them to tally their votes
		else:
			candidate_votes.append(1)
			candidates.append(row[2])

	# Assign variables to find winner
	percentages = []
	max_index = 0

	# Calculate percentages and add to percentages[]
	for i in range(len(candidates)):
		vote_percentage = round((candidate_votes[i]/total_votes*100), 3)
		percentages.append(vote_percentage)
		# Find winner
		if percentages[i] > percentages[0]:
			percentages[0] = percentages[i]
			max_index = i
	winner = candidates[max_index]

# Print results
results = (
"Election Results\n"
"--------------------------\n"
f"Total Votes: {total_votes}\n"
"--------------------------")

results_cont = (
"--------------------------\n"
f"Winner:  {winner}\n"
"--------------------------")

print(results)
for i in range(len(candidates)):
	print(f"{candidates[i]}: {percentages[i]}% ({candidate_votes[i]})")
print(results_cont)

# output path
output = os.path.join(".","election results.txt")
with open(output,"w") as text_file:
	text_file.write(results)
	for i in range(len(candidates)):
		text_file.write(f"{candidates[i]}: {percentages[i]}% ({candidate_votes[i]})")
	text_file.write(results_cont)
		