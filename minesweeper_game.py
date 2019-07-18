# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random

class Tableau():
    def __init__(self,longueur,largeur,pourcentage):
        self.tab = init(longueur,largeur,pourcentage)
        self.longueur = longueur
        self.largeur = largeur
        self.pourcentage = pourcentage
        self.game_over = "Game over"
        self.victory = "Victory!"
        self.cases_liberees = 0
    def open_cases(self,i,j):
        if 0<i<=self.longueur and 0<j<=self.largeur and self.tab[i][j].open == False and self.tab[i][j].flag == False :
            if self.tab[i][j].bombe == True  :
                return self.game_over
            else :
                self.tab[i][j].open_case()
                self.cases_liberees += 1
                if self.cases_liberees >= ((self.longueur*self.largeur)-int(self.pourcentage*self.longueur*self.largeur)):
                        return self.victory
                elif self.tab[i][j].n_bombe == 0 :
                    for k in [0,1,2]:
                        for l in [0,1,2]:
                            if 0<i+k-1<=self.longueur and 0<j+l-1<=self.largeur+1 and self.tab[i+k-1][j+l-1].open == False:
                                self.open_cases(i+k-1,j+l-1)

    def display(self):
        return self.tab
    def free_cases(self,i,j):
        if self.tab[i][j].open == True :
            flags = 0
            coord = []
            for k in [0,1,2]:
                for l in [0,1,2]:
                    if self.tab[i+k-1][j+l-1].flag == True :
                        flags += 1 
                        coord.append([i+k-1,j+l-1])
            if flags == self.tab[i][j].n_bombe :
                for m in range(len(coord)):
                    if self.tab[coord[m][0]][coord[m][1]].bombe != True:
                        return self.game_over
                for k in [0,1,2]:
                    for l in [0,1,2]:
                        if self.tab[i+k-1][j+l-1].flag == False and self.tab[i+k-1][j+l-1].open == False :
                            self.open_cases(i+k-1,j+l-1)
                
class Case():
    def __init__(self,bombe,n_bombe,x,y):
        self.bombe = bombe
        self.n_bombe = n_bombe
        self.open = False
        self.x = x
        self.y = y
        self.flag = False
    def open_case(self):
            self.open = True
            self.flag = False
    def flag_case(self):
        self.flag = True
    def __repr__(self):
        if self.open == True and self.bombe!= True :
            return str(self.n_bombe)
        elif self.bombe == True and self.open == True :
            return "B"
        elif self.flag == True and self.open == False :
            return "F"
        return "X"
    def get_bombe(self):
        return self.bombe
        
        
    
def tableau(m,n):
    tab = []
    for i in range(m+2):
        tab.append([])
        for j in range(n+2):
            case = Case(False,0,i,j)
            tab[i].append(case)
    return tab

def set_bombs(tab,percentage):
    n_bombs = int(percentage*len(tab)*len(tab[0]))
    bombes = []
    compteur = 0
    while compteur < n_bombs :
        a = random.randint(1,4)
        b = random.randint(1,5)
        c = [a,b]
        if c not in bombes :
            bombes.append(c)
            compteur +=1
            for d in bombes:
                tab[d[0]][d[1]].bombe = True
                compteur +=1
    '''compteur = 0
    while compteur < n_bombs :
        for i in range(1,len(tab)-1):
            if compteur < n_bombs:
                for j in range(1,len(tab[0])-1):
                    if rd() < percentage and tab[i][j].bombe !=True and compteur<n_bombs:
                        tab[i][j].bombe = True
                        compteur += 1'''
    return tab

def how_many_bombs(tab):
    for i in range(1, len(tab)-1):
        for j in range(1, len(tab[0])-1):
            if tab[i][j].bombe!=True:
                for k in [0,1,2]:
                    for l in [0,1,2]:
                        if tab[i+k-1][j+l-1].bombe == True :
                            tab[i][j].n_bombe += 1
    return tab

def init(m,n,percentage):
    tab = tableau(m,n)
    set_bombs(tab,percentage)
    how_many_bombs(tab)
    return tab