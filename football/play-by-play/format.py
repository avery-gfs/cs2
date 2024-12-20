import pandas as pd
import csv
import re

class player:
    def __init__(self, number, firstname, lastname, team):
        self.number = number
        self.team = team
        self.firstname = firstname
        self.lastname = lastname
        self.namenum = str(number)+'-'+firstname[0]+'.'+lastname.upper()
        #self.rushing

def runner(player):
    def __init__(self, number, firstname, lastname, team, rushing_yards = 0):
        super().__init__(number, firstname, lastname, team)

class qb(player):
    def __init__(self, number, firstname, lastname, team, passing_yards = 0, att = 0, complete = 0, td = 0, interceptions = 0):
        super().__init__(number, firstname, lastname, team)
        self.passing_yards = passing_yards
        self.att = att
        self.complete = complete
        self.td= 0
        self.interceptions = 0

    
    def todict(self):
        playerdict = dict(name = self.firstname + ' ' + self.lastname, number = self.number, passing_yards = self.passing_yards, pass_attempts = self.att, complete_passes = self.complete, touchdowns = self.td, interceptions = self.interceptions) 
        return playerdict

    def addpass(self,yards, IsIncomplete, IsInterception, IsTouchdown):
        self.att+=1
        if IsIncomplete == 0:
            self.complete+=1

            if yards>0:
                self.passing_yards+=yards

        if IsInterception == 1:
            self.interceptions+=1
        
        if IsTouchdown == True:
            self.td+=1

    #def adrush

df = pd.read_csv('pbp-2024.csv') 
pass_df= df.loc[df['PlayType'] == 'PASS', ['GameId','GameDate','Quarter','Minute','Second','OffenseTeam','DefenseTeam','Down','ToGo','YardLine','Description','PlayType','Yards','IsIncomplete','IsTouchdown','IsInterception','IsFumble']]
rush_df= df.loc[df['PlayType'] == 'RUSH', ['GameId','GameDate','Quarter','Minute','Second','OffenseTeam','DefenseTeam','Down','ToGo','YardLine','Description','PlayType','Yards','IsIncomplete','IsTouchdown','IsInterception','IsFumble']]

#df['PlayType'] == 'RUSH') | (df['PlayType'] == 'TWO-POINT CONVERSION'), [
tackle = '()'
miss = '[]'

laterals = []
penalties = []
passing_off = []
rushing_off = []

defense = []
rowlines =[['GameDate','QuarterTime', 'Offense', 'Defense', 'Down','ToGo','Qb', 'Receiver', 'Yards','IsIncomplete','IsIntercepted','IsTouchdown', 'Description']]
rushlines = [['GameDate','QuarterTime','Offense','Defense','Down','ToGo','Runner','Yards','IsTouchdown','IsFumble', 'Description']]

for play in rush_df.itertuples():
    description = play.Description
    original = description

    if 'REVERSED' in description:
        description = description.split('REVERSED')[1]

    if 'LATERAL' in description:
        lateral = True
        laterals.append(description)
        continue 

    offensive = []
    fumble = False
    tackled = []
    broken = []
    intercepted = False
    incomplete = False
    lateral = False
    penalty = False
    touchdown = False


    if 'TOUCHDOWN.' in description:
        touchdown = True

    fixed = description.split('INJURED')[0]
    fixed = description.split('INJURY')[0]
    fixed = fixed.split('PENALTY')[0]
    if 'AT QB' in description:
        description = description.split('AT QB')[1]
    splitted = description.split(' ')
    if 'INJURED' in splitted:
        index = splitted.index('INJURED')
        splitted = splitted[:index-2]

    if '**' in splitted:
        index = splitted.index('**')
        splitted = splitted[:index]

    if 'PENALTY' in splitted:
        index = splitted.index('PENALTY')
        splitted = splitted[:index]

    if 'ELIGIBLE.' in splitted:
        index = splitted.index('ELIGIBLE.')
        splitted = splitted[index:]

    if 'INJURY' in splitted:
        index = splitted.index('INJURY')
        splitted = splitted[:index]

    if 'FUMBLES,' in splitted:
        fumble = True
        index = splitted.index('FUMBLES,')
        splitted = splitted[:index]

    if 'FUMBLES' in splitted:
        fumble = True
        index = splitted.index('FUMBLES')
        splitted = splitted[:index]


    if 'PENALTY' in description:
        penalty = True
        penalties.append(description)

    if 'DIRECT SNAP TO' in description:
        splitted.pop(splitted.index('DIRECT')+3)

    for word in splitted:
        if word not in fixed.split(' '):
            splitted.remove(word)
    print(splitted)
    
    for word in splitted:
        if '-' in word and len(word)>4:
            if not any(char in tackle or char in miss for char in word):
                offensive.append(word)
            if any(char in tackle for char in word):
                tackled.append(''.join(char for char in word if char not in tackle))
            if any(char in miss for char in word):
                broken.append(''.join(char for char in word if char not in miss))

    if len(offensive)!=1:
        print(offensive)
        print(description)
        continue

    if play.Minute>=10:
        if play.Second>=10:
            timeformat = 'Q' + str(play.Quarter) + '-'+ str(play.Minute) + ':' + str(play.Second)
        else:
            timeformat = 'Q' + str(play.Quarter) + '-'+ str(play.Minute) + ':0' + str(play.Second)
    else:
        if play.Second>=10:
            timeformat = 'Q' + str(play.Quarter) + '-0'+ str(play.Minute) + ':' + str(play.Second)
        else:
            timeformat = 'Q' + str(play.Quarter) + '-0'+ str(play.Minute) + ':0' + str(play.Second)

    row = [play.GameDate, timeformat, play.OffenseTeam, play.DefenseTeam, play.Down, play.ToGo, offensive[0], play.Yards, touchdown, fumble, original]

    rushlines.append(row)

for play in pass_df.itertuples():
    description = play.Description
    original = play.Description
    offensive = []
    tackled = []
    broken = []
    intercepted = False
    incomplete = False
    lateral = False
    penalty = False
    touchdown = False


    if 'TOUCHDOWN.' in description:
        touchdown = True

    splitted = description.split(' ')

    if 'INTERCEPTED' in splitted:
        intercepted = True
    
    if 'LATERAL' in splitted:
        lateral = True
        laterals.append(description)
        pass

    if 'PENALTIES' in splitted:
        penalty = True
        penalties.append(description)
        pass

    if 'INCOMPLETE' in splitted:
        incomplete = True

    for word in splitted:
        if '-' in word:
            if not any(char in tackle or char in miss for char in word):
                offensive.append(word)
            if any(char in tackle for char in word):
                tackled.append(''.join(char for char in word if char not in tackle))
            if any(char in miss for char in word):
                broken.append(''.join(char for char in word if char not in miss))

    if intercepted == True:
        offensive.append('INTERCEPTED')
        touchdown = False 

    if incomplete == True:
        offensive.append('INCOMPLETE')

    #print(offensive)

    if play.Minute>=10:
        timeformat = 'Q' + str(play.Quarter) + ' '+ str(play.Minute) + ':' + str(play.Second)
    else:
        timeformat = 'Q' + str(play.Quarter) + ' 0'+ str(play.Minute) + ':' + str(play.Second)

    qbstr = offensive[0]
    receiverstr = offensive[1]
    if receiverstr[-1] == '.':
        receiverstr = receiverstr [:-1]
    if qbstr[-1] == '.':
        qbstr = qbstr[:-1]

    row = [play.GameDate, timeformat, play.OffenseTeam, play.DefenseTeam, play.Down, play.ToGo, qbstr, receiverstr, play.Yards, incomplete, intercepted, touchdown, original]

    rowlines.append(row)


    #print(offensive, tackled, broken, intercepted)
import csv

with open('passing.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rowlines)

with open('rushing.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rushlines)

passing_df = df.loc[(df['OffenseTeam'] == 'PHI') & (df['PlayType'] == 'PASS'), ['Description','Yards','IsIncomplete', 'IsInterception', 'IsTouchdown', 'Description']]
hurts = qb(1, 'Jalen', 'Hurts', 'PHI')
print(hurts.namenum)
for play in passing_df.itertuples():
    description = play.Description
    yards = play.Yards
    IsIncomplete = play.IsIncomplete
    IsInterception = play.IsInterception
    IsTouchdown = play.IsTouchdown

    if hurts.namenum in description.split(' '):
        hurts.addpass(yards, IsIncomplete, IsInterception, IsTouchdown)
    
print(hurts.todict())



'''
        
with open(<path to output_csv>, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)
'''
