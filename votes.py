from tabulate import tabulate
class Votes:
  def __init__(self, candidate_votes, total_votes):
    self.candidate_votes = candidate_votes
    self.total_votes = total_votes
  def __str__(self):
    return f"candidate_votes: {self.candidate_votes}, total votes: {self.total_votes}"
  
  def percentage_votes(self):  
    percent = (sum(self.candidate_votes)/sum(self.total_votes)) * 100
    return percent

no_polling_stations = int(input("Enter the number of polling stations: "))
candidate1 = input("Enter the name of the first candidate: ")
candidate2 = input("Enter the name of the second candidate: ")
polling_stations = []
candidate1_votes = []
candidate2_votes = []
polling_station_totals = []

try:
  
  i = 1
  while i <= no_polling_stations:
    
    polling_station = input("Enter the polling station name: ")
    polling_stations.append(polling_station)
    votes1 = int(input(f"Enter the votes for {candidate1} at {polling_station}: "))
    candidate1_votes.append(votes1)
    votes2 = int(input(f"Enter the votes for {candidate2} at {polling_station}: "))
    candidate2_votes.append(votes2)
    total_votes = int(input(f"Enter the total votes cast at {polling_station}: "))
    polling_station_totals.append(total_votes)
    i = i+1
  
  row1 = ["Candidate"]
  row1.extend(polling_stations)
  row2 = [candidate1]
  row2.extend(candidate1_votes)
  row3 = [candidate2]
  row3.extend(candidate2_votes)
  
  result = [row1, row2, row3]
  print(tabulate(result))
  
  votes_attained1 = Votes(candidate1_votes, polling_station_totals)
  votes_attained2 = Votes(candidate2_votes, polling_station_totals)
  votes1 = votes_attained1.percentage_votes()
  votes2 = votes_attained2.percentage_votes()
  print("Total votes per polling station are:", votes_attained1.total_votes, "respectively")
  
  candidate1_totals = sum(candidate1_votes)
  print(f"{candidate1}'s total votes are {candidate1_totals}")
  candidate2_totals = sum(candidate2_votes)
  print(f"{candidate2}'s total votes are {candidate2_totals}")
  print(f"{candidate1}'s total percentage vote is {votes1}%")
  print(f"{candidate2}'s total percentage vote is {votes2}%")

except:
  print("Please enter numeric values")
  
  
  


  
    
  