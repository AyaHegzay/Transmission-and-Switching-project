from math import factorial 
import numpy as np

def erlang(A, m):
    L = (A ** m) / factorial(m)
    sum_ = 0
    for n in range(m + 1): 
        sum_ += (A ** n) / factorial(n)

    return (L / sum_)

sectoring = [10,60,120,180,360]
n=[]
carriertoInt=8
pb=0.02
nbChannelsPerUser=2
nbUserPerKM2=5000
reuseFactor=[3,4,7,12,9,13]
coChannelInter=[[6,4,3,2],[6,3,2,1],[6,3,2,1],[6,4,3,2],[6,3,2,1],[6,3,2,1]]
cityArea=400
nbCallPerUser=10/(60*24)
avgCallDur=1
nbChannelSP=125
channelMaxPerCell=50
nbSub=cityArea*nbUserPerKM2
aUser=avgCallDur*nbCallPerUser
test=[]
nbOfsectors=0

for i in range (0,len(reuseFactor)):
    reuse=reuseFactor[i]
    for j in range (0,len(coChannelInter[0])):
        cond=(3*reuse)/(coChannelInter[i][j])
        if (cond>carriertoInt):
            if(j==0):
              nbOfsectors=1
            elif(j==1):
              nbOfsectors=2
            elif(j==2):
              nbOfsectors=3
            elif(j==3):
              nbOfsectors=6
            temp=[reuse,nbOfsectors]
            test=test+[temp]
index=0      
channelPerCell=nbChannelSP         
for i in range(len(test)):
    temp=nbChannelSP/(test[i][0]*test[i][1]*2)
    if temp<=channelMaxPerCell and temp>channelPerCell:
        channelPerCell=int(temp)
        index=i
        
flag=False
aCell=0.01
while (flag==False):
  ring=int(erlang(aCell,channelPerCell)*100)/100
  if (ring==pb):
      flag =True
  aCell=aCell+0.01

subPerCell=int(aCell/aUser)
numCells=np.ceil(nbSub/subPerCell)
sectorPerCell=360//(test[index][1])
reuseFactor=test[index][0]
print("reuseFactor ",reuseFactor)
print("subPerCell ",subPerCell)
print("sectorPerCell " ,sectorPerCell)
