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

# After processing the `rushing.csv` file
print(runners['26-S.BARKLEY'].yards)

#TASK 2: Finish this QB class:
class Quarterback:
    def __init__(self, name, team):
        self.name = name
        self.team = team
        self.pass_att = 0
        self.completions = 0
        self.passing_yards = 0
        self.conversions = 0
        self.touchdowns_thrown = 0

    def __repr__(self):
        return (f"Team: {self.team}, Name: {self.name}, Pass Attempts: {self.pass_att}, "
                f"Completions: {self.completions}, Passing Yards: {self.passing_yards}, "
                f"Conversions: {self.conversions}, Touchdowns Thrown: {self.touchdowns_thrown}")

    def add_pass(self, play):
        self.pass_att += 1
        if play['IsIncomplete'] == 'False':
            self.completions += 1
            self.passing_yards += int(play['Yards'])
            if int(play['Yards']) >= int(play['ToGo']):
                self.conversions += 1
            if play['IsTouchdown'] == 'True':
                self.touchdowns_thrown += 1

    def calculate_completion_rate(self):
        return self.completions / self.pass_att if self.pass_att > 0 else 0


quarterbacks = {}

with open('passing.csv', newline='') as csvfile:
    passing_plays = csv.DictReader(csvfile)
    for play in passing_plays:
        qb = play['Qb']
        team = play['Offense']
        
        if qb not in quarterbacks:
            quarterbacks[qb] = Quarterback(qb, team)
        
        quarterbacks[qb].add_pass(play)

#TASK 4: Add functionality for counting touchdowns and fumbles. How many rushing touchdowns does Jalen Hurts have? How many has he thrown? (1-J.HURTS)

# Rushing Touchdowns
rushing_touchdowns = 0
with open('rushing.csv', newline='') as csvfile:
    rushing_plays = csv.DictReader(csvfile)
    for play in rushing_plays:
        if play['Runner'] == '1-J.HURTS' and play['IsTouchdown'] == 'True':
            rushing_touchdowns += 1

print(f"Jalen Hurts Rushing Touchdowns: {rushing_touchdowns}")

# Passing Touchdowns
print(f"Jalen Hurts Passing Touchdowns: {quarterbacks['1-J.HURTS'].touchdowns_thrown}")

#TASK 5: Calculate Jalen hurt's pass completion rate

completion_rate = quarterbacks['1-J.HURTS'].calculate_completion_rate()
print(f"Jalen Hurts Completion Rate: {completion_rate:.2%}")

#TASK 6: Make receiver class

class Receiver:
    def __init__(self, name, team):
        self.name = name
        self.team = team
        self.targets = 0
        self.catches = 0
        self.touchdowns = 0
        self.yards = 0

    def __repr__(self):
        return (f"Team: {self.team}, Name: {self.name}, Targets: {self.targets}, "
                f"Catches: {self.catches}, Yards: {self.yards}, Touchdowns: {self.touchdowns}")

    def add_catch(self, play):
        self.targets += 1
        if play['IsIncomplete'] == 'False':
            self.catches += 1
            if play['IsTouchdown'] == 'True':
                self.touchdowns += 1

        yards = int(play['Yards'])  # Converts rushing yards from string to integer
        
        if yards > 0:  
            self.yards += yards  # Adds positive rushing yards to total

    def calculate_catch_rate(self):
        return self.catches / self.targets if self.targets > 0 else 0

#Task 7: Calculate AJ Brown's "catch rate" (11-A.BROWN)

receivers = {}

with open('passing.csv', newline='') as csvfile:
    passing_plays = csv.DictReader(csvfile)
    for play in passing_plays:
        receiver_name = play['Receiver']
        if receiver_name[-1]=='.':
            receiver_name.pop(-1)
            
        team = play['Offense']
        
        if receiver_name not in receivers:
            receivers[receiver_name] = Receiver(receiver_name, team)
        
        receivers[receiver_name].add_catch(play)

catch_rate = receivers['11-A.BROWN'].calculate_catch_rate()
print(f"AJ Brown's Catch Rate: {catch_rate:.2%}")

#CHALLENGE: Calculate the conversion rate for all plays of the philadelphia eagles, broken into 1st, 2nd, 3rd, and 4th down.
#SUPER CHALLENGE: Read in Description collumn and look for players in parentheses, those players tackled the offensive player. Players in brackets were covering the receiver. use this data and make new classes for defensive positions 

class DefensivePlayer:
    def __init__(self, name):
        self.name = name
        self.tackles = 0
        self.coverages = 0

    def __repr__(self):
        return f"Name: {self.name}, Tackles: {self.tackles}, Coverages: {self.coverages}"

    def add_tackle(self):
        self.tackles += 1

    def add_coverage(self):
        self.coverages += 1


def process_description(description, defensive_players):
    """Process the description to extract tacklers (in `()`) and coverage players (in `[]`)."""
    # Process tacklers in parentheses `()`
    nonowords = ['(NO','HUDDLE)','(SHOTGUN)']
    splitted = description.split(' ')
    for nono in nonowords:
        splitted.append(nono)

    for word in splitted:
        if ':' in word and '(' in word and ')' in word:
            splitted.remove(word)

    splitted.remove('(NO')
    splitted.remove('HUDDLE)')
    splitted.remove('(SHOTGUN)')
    description = ' '.join(splitted)
    

    if '(' in description and ')' in description:
        tacklers = description[description.index('(') + 1:description.index(')')].split('; ')
        for group in tacklers:
            individual_tacklers = group.split(', ')
            for player_name in individual_tacklers:
                if player_name not in defensive_players:
                    defensive_players[player_name] = DefensivePlayer(player_name)
                defensive_players[player_name].add_tackle()

    # Process coverage player in brackets `[]`
    if '[' in description and ']' in description:
        coverage_player = description[description.index('[') + 1:description.index(']')].strip()
        if coverage_player not in defensive_players:
            defensive_players[coverage_player] = DefensivePlayer(coverage_player)
        defensive_players[coverage_player].add_coverage()


defensive_players = {}

# Process Rushing Plays
with open('rushing.csv', newline='') as csvfile:
    rushing_plays = csv.DictReader(csvfile)
    for play in rushing_plays:
        description = play['Description']
        process_description(description, defensive_players)

# Process Passing Plays
with open('passing.csv', newline='') as csvfile:
    passing_plays = csv.DictReader(csvfile)
    for play in passing_plays:
        description = play['Description']
        process_description(description, defensive_players)

'''
# Print out the defensive players with their stats
for player in defensive_players.values():
    print(player)
'''

# Sort receivers by yards in descending order

sorted_receivers = sorted(receivers.items(), key=lambda x: x[1].yards, reverse=True)

# Write to CSV
with open('receivers.csv', 'w', newline='') as csvfile:
    fieldnames = ['Receiver', 'Yards']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for receiver, data in sorted_receivers:
        writer.writerow({'Receiver': receiver, 'Yards': data})
