import csv

class Runningback:
    def __init__(self, name, team):
        self.name = name
        self.team = team
        self.att = 0
        self.yards = 0
        self.conversions = 0

    def __repr__(self):
        return str('Team: ' + str(self.team) + ', Name: ' + str(self.name) + ', Rush Attempts: ' + str(self.att) + ', Rushing Yards: ' + str(self.yards) + ', Downs Converted: ' + str(self.conversions)) 

    def add_play(self, play):
        down = int(rush['Down'])
        togo = int(rush['ToGo'])
        yards = int(rush['Yards'])

        self.att+=1

        if yards>0:
            self.yards+=yards

        if yards>togo:
            self.conversions+=1
    
    def calculate_conversion_rate(self, down):
        return #WRITE CODE HERE (part 4)

runners = {}
#lines of this csv file are of the following form: 
with open('rushing.csv', newline='') as csvfile:
    rushing_plays = csv.DictReader(csvfile)
    for rush in rushing_plays:
        runner = rush['Runner']
        team = rush['Offense']
        
        if runner not in runners.keys():
            runners[runner] = Runningback(runner, team)
    
        runners[runner].add_play(rush)

print(runners['26-S.BARKLEY']) #TASK 1


#TASK 1: How many rushing yards does Saquon Barkley have? (26-S.BARKLEY)
#TASK 2: Finish this QB class:

class Quarterback:
    def __init__(self, name, team):
        self.name = name
        self.pass_att = 0
        self.completions = 0
        self.passing_yards = 0
        self.conversions = 0
        self.touchdowns_thrown = 0

    def __repr__(self):
        return #WRITE CODE HERE

    def add_pass(self, play):
        #WRITE CODE HERE
        pass

    def calculate_completion_rate(self):
        return #WRITE CODE HERE


#TASK 3: read in passing data and make dictionary of quarterbacks
with open('passing.csv', newline='') as csvfile:
    passing_plays = csv.DictReader(csvfile)
    for play in passing_plays:
        qb = play['Qb']
        reciever = play['Reciever']
        
        #FINISH CODE HERE

#TASK 4: Add functionality for counting touchdowns and fumbles. How many rushing touchdowns does Jalen Hurts have? How many has he thrown? (1-J.HURTS)
#TASK 5: Make reciver class

class Reciever:
    def __init__(self, name, team):
        self.targets = 0
        self.catches = 0
        self.touchdowns = 0
    
    def __repr__(self):
        #WRITE HERE
    
    def add_catch(self, play):
        #WRITE CODEHERE
        pass

    def calculate_catch_rate(self):
        #WRITE CODE HERE
        return


#TASK 6: Calculate Jalen hurt's 3rd down (passing) conversion rate

#CHALLENGE: Calculate the conversion rate for all plays of the philadelphia eagles, broken down by 1st, 2nd, 3rd, and 4th down.
#SUPER CHALLENGE: Read in Description collumn and look for players in parentheses, those players tackled the offensive player. Players in brackets were covering the reciever. use this data and make new classes for defensive positions 

