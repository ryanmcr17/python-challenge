# define variables for final outputs
total_votes = 0
candidate_list = []
vote_count_list = []
vote_share_list = []
winner = ""


# import CSV module for reading data file

import csv


# read data file

with open('/Users/mcrey/bootcamp/work/challenges/03-Python/python-challenge/PyPoll/Resources/election_data.csv') as vote_file:
    
    data = csv.reader(vote_file)


    # process reader object into list of candidates, adding total votes per candidate

    for row in data:

        if row[2] != 'Candidate':

            total_votes = total_votes + 1
        
            if row[2] in candidate_list:
                
                candidate_index = candidate_list.index(row[2])
                vote_count_list[candidate_index] = vote_count_list[candidate_index] + 1
                vote_share_list[candidate_index] = vote_count_list[candidate_index] / total_votes


            else:

                candidate_list.append(row[2])
                vote_count_list.append(1)
                vote_share_list.append(1 / total_votes)
                

    candidate_count = len(candidate_list)
    
    with open('analysis/results_file.txt', 'w') as results_file:
        print(f"Election Results")
        print(f"Election Results",file=results_file)
        print(f"-------------------------")
        print(f"-------------------------",file=results_file)
        print(f"Total Votes: {total_votes}")
        print(f"Total Votes: {total_votes}",file=results_file)
        print(f"-------------------------")
        print(f"-------------------------",file=results_file)
        
        
        for i in range(candidate_count):
        
            print(f"{candidate_list[i]}: {round(100*vote_count_list[i]/total_votes,3)}% ({vote_count_list[i]})")
            print(f"{candidate_list[i]}: {round(100*vote_count_list[i]/total_votes,3)}% ({vote_count_list[i]})",file=results_file)


        print(f"-------------------------")
        print(f"-------------------------",file=results_file)


        winner = candidate_list[vote_count_list.index(max(vote_count_list))]
        print(f"Winner: {winner}")
        print(f"Winner: {winner}",file=results_file)

        print(f"-------------------------")
        print(f"-------------------------",file=results_file)

