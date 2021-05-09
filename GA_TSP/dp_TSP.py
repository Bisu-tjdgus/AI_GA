#In this assignment you will implement one or more algorithms for the traveling salesman problem,
#such as the dynamic programming algorithm covered in the video lectures. Here is a data file describing a TSP instance.
#z-city.txt
#The first line indicates the number of cities. Each city is a point in the plane, and each subsequent
#line indicates the x- and y-coordinates of a single city.
#The distance between two cities is defined as the Euclidean distance --- that is,
#two cities at locations (x,y)(x,y) and (z,w)(z,w) have distance \sqrt{(x-z)^2 + (y-w)^2} between them.
#In the box below, type in the minimum cost of a traveling salesman tour for this instance, rounded down to the nearest integer.

import math
import csv
import numpy as np



class TSP:
    def __init__(self,filename):
        self.G={}
        self.dist={}
        self.prev_setS=set()
        self.curr_setS=set()
        self.prev_A={}
        self.curr_A={}
        self.inputfile=filename
        self.min_dist=float("inf")
    def readinput(self):
        with open(self.inputfile) as f:
            c=0
            for line in f:
                v=line.split()
                v=[float(i) for i in v]
                if len(v)>1:
                    self.G[c]={}
                    self.G[c]['x']=v[0]
                    self.G[c]['y']=v[1]
                    c+=1
    def evalaute_distace(self):
        num_of_cities=len(self.G.keys())
        for city1 in range(0,num_of_cities-1):
            for city2 in range(city1+1,num_of_cities):
                dist=math.sqrt((self.G[city1]['x']-self.G[city2]['x'])**2 +\
                        (self.G[city1]['y']-self.G[city2]['y'])**2)
                self.dist[(city1,city2)]=self.dist[(city2,city1)]=dist

    def setS(self,cardinatlity):
        if self.prev_setS==set():
            self.prev_setS={1<<x for x in self.G.keys()}
        else:
            self.prev_setS=self.curr_setS
        self.curr_setS=set()
        for seta in self.prev_setS:
            for i in range(0,len(self.G.keys())):
                    setb=seta|(1<<i)
                    if bin(setb).count('1') == cardinatlity:
                        self.curr_setS.add(setb)
        return self.curr_setS

    def tsp_dist(self):
        #base case
        for m in range(2,len(self.G.keys())+1):
            self.prev_A=self.curr_A
            self.prev_A[(1,0)]=0
            self.curr_A={}
            print('current cardinality :',m)
            for S in self.setS(m):
                for j in self.G.keys():
                    temp=float("inf")
                    if 1<<j & S:
                        #A[s,j]=min(A[s-j,k]+dist_kj
                        for k in self.G.keys():
                            if (1<<k & S) and (k!=j):
                                S_j=S^(1<<j)
                                temp=min(self.prev_A.get((S_j,k),float("inf")) + self.dist[(k,j)],temp)
                        self.curr_A[S,j]=temp
        #last hop

        S=2**(len(self.G.keys()))-1
        for j in range(1,len(self.G.keys())):
            self.min_dist=min(self.curr_A[S,j]+self.dist[(j,0)],self.min_dist)
        print(self.min_dist)

s=TSP('TSP.txt')
s.readinput()
s.evalaute_distace()
s.tsp_dist()

