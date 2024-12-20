import csv

class Runningback:
    def __init__(self, name, team):
        self.name = name  # Initializes the player's name
        self.team = team  # Initializes the player's team
        self.att = 0  # Initializes rush attempts to 0
        self.yards = 0  # Initializes rushing yards to 0
        self.conversions = 0  # Initializes downs converted to 0

    def __repr__(self):
        # Creates a string representation of the Runningback object for debugging or display
        return str('Team: ' + str(self.team) + ', Name: ' + str(self.name) + ', Rush Attempts: ' + str(self.att) + ', Rushing Yards: ' + str(self.yards) + ', Downs Converted: ' + str(self.conversions)) 

    def add_play(self, play):
        # Processes a single rushing play
        down = int(rush['Down'])  # Converts down from string to integer
        togo = int(rush['ToGo'])  # Converts yards to go from string to integer
        yards = int(rush['Yards'])  # Converts rushing yards from string to integer

        self.att += 1  # Increments rush attempts

        if yards > 0:  
            self.yards += yards  # Adds positive rushing yards to total

        if yards > togo:  
            self.conversions += 1  # Increments conversions if yards gained exceed yards to go
    
    def calculate_conversion_rate(self, down):
        # Placeholder for calculating the conversion rate for a specific down
        return #WRITE CODE HERE (part 4)

runners = {}  # Dictionary to store Runningback objects by runner name
# Lines of this csv file are of the following form:
with open('rushing.csv', newline='') as csvfile:
    rushing_plays = csv.DictReader(csvfile)  # Reads the CSV as a dictionary
    for rush in rushing_plays:
        runner = rush['Runner']  # Gets the runner's name from the play
        team = rush['Offense']  # Gets the team from the play
        
        if runner not in runners.keys():  
            # Creates a new Runningback object if the runner is not already in the dictionary
            runners[runner] = Runningback(runner, team)
    
        runners[runner].add_play(rush)  # Adds the play to the Runningback object

#TASK 1: How many rushing yards does Saquon Barkley have? (26-S.BARKLEY)
#TASK 2: Finish this QB class:

class Quarterback:
    def __init__(self, name, team):
        self.name = name  # Initializes the quarterback's name
        self.pass_att = 0  # Initializes pass attempts to 0
        self.completions = 0  # Initializes completions to 0
        self.passing_yards = 0  # Initializes passing yards to 0
        self.conversions = 0  # Initializes conversions to 0
        self.touchdowns_thrown = 0  # Initializes touchdowns thrown to 0

    def __repr__(self):
        #WRITE CODE HERE
        return 

    def add_pass(self, play):
        #WRITE CODE HERE
        return 

    def calculate_completion_rate(self):
        #WRITE CODE HERE
        return 

#finish the code to read in information about passing plays

with open('passing.csv', newline='') as csvfile:
    passing_plays = csv.DictReader(csvfile)  # Reads the CSV as a dictionary
    for play in passing_plays:
        qb = play['Qb']  # Gets the quarterback's name from the play
        receiver = play['Receiver']  # Gets the receiver's name from the play
        
        #WRITE CODE HERE

#TASK 4: Add functionality for counting touchdowns and fumbles. How many rushing touchdowns does Jalen Hurts have? How many has he thrown? (1-J.HURTS)
#TASK 5: Calculate Jalen hurt's pass completion rate
#TASK 6: Make receiver class

class Receiver:
    def __init__(self, name, team):
        self.targets = 0  # Initializes the number of targets to 0
        self.catches = 0  # Initializes the number of catches to 0
        self.touchdowns = 0  # Initializes the number of touchdowns to 0
    
    def __repr__(self):
        #WRITE CODE HERE
        return
    
    def add_catch(self, play):
        #WRITE CODE HERE
        return

    def calculate_catch_rate(self):
        # Placeholder for processing a single receiving play
        pass
    
#Task 7: Calculate AJ Brown's "catch rate" (11-A.BROWN)

#CHALLENGE: Calculate the conversion rate for all plays of the philadelphia eagles, broken into 1st, 2nd, 3rd, and 4th down.
#SUPER CHALLENGE: Read in Description collumn and look for players in parentheses, those players tackled the offensive player. Players in brackets were covering the receiver. use this data and make new classes for defensive positions 