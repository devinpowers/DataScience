#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 19:10:59 2020

@author: devinpowers
"""
import math

'''openig/reading the csv file'''
import csv
with open("nba_2013.csv", "r") as f:
    reader = csv.reader(f, delimiter=',')
    nba = list(reader)
    


# Creating the Team Class

class Team():
    
    def __init__(self, team_name):
        self.team_name = team_name
        self.roster = []
        for row in nba:
            if row[3] == self.team_name:
                self.roster.append(Player(row))
    
    def num_players(self):
        count = 0
        for player in self.roster:
            count += 1
        return count
    
    def average_age(self):
        total_age = 0
        for player in self.roster:
            total_age += player.age
        
        return total_age / self.num_players()


class Player():
    def __init__(self, data_row):
        self.player_name = data_row[0]
        self.position = data_row[1]
        self.age = int(data_row[2])
        self.team = data_row[3]

class Team():
    def __init__(self, team_name):
        self.team_name = team_name
        self.roster = []
        for row in nba:
            if row[3] == self.team_name:
                self.roster.append(Player(row))
    
    def num_players(self):
        count = 0
        for player in self.roster:
            count += 1
        return count
   
    def average_age(self):
        return math.fsum([player.age for player in self.roster]) / self.num_players()
    
    @classmethod
    def older_team(self, team1, team2):
        if team1.average_age() > team2.average_age():
            return team1
        else:
            return team2
        
        
old_team = Team.older_team(Team("TOT"), Team("UTA"))

older_team = old_team.team_name
print("older_team:", older_team)