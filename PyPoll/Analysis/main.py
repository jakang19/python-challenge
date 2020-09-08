import os
import csv

election_csv = os.path.join("..", "Resources", "election_data.csv")

with open(election_csv) as csv_file
	csv_reader = csv.reader(csv_file, delimiter=",")
	header = next(csv_reader)