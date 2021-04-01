maches=[{"iran":0,"spain":0},{"iran":0,"portugal":0},{"iran":0,"morocco":0},{"spain":0,"portugal":0},{"spain":0,"morocco":0},{"portugal":0,"morocco":0},]
scores={'iran':0,'spain':0,'portugal':0,'morocco':0}
wins={'iran':0,'spain':0,'portugal':0,'morocco':0}
loses={'iran':0,'spain':0,'portugal':0,'morocco':0}
draws={'iran':0,'spain':0,'portugal':0,'morocco':0}
goals_difference={'iran':0,'spain':0,'portugal':0,'morocco':0}
teams=[['iran',{'wins':0,'loses':0,'draws':0,'goals_difference':0,'score':0}],['spain',{'wins':0,'loses':0,'draws':0,'goals_difference':0,'score':0}],['portugal',{'wins':0,'loses':0,'draws':0,'goals_difference':0,'score':0}],['morocco',{'wins':0,'loses':0,'draws':0,'goals_difference':0,'score':0}]]
for i in range(len(maches)):
    for j in maches[i]:
        temp=int(input(f"what is {j}'s score ?"))
        maches[i].update({str(j):temp})
    print('\n')

for i in range(len(maches)):
    temp1=-1
    for j in maches[i]:
        if temp1==-1:
            t=j
            temp1=maches[i][j]
        elif temp1<maches[i][j]:
            for k in scores:
                if k==j:
                    scores[k]+=3
                    wins[k]+=1
                if k==t:
                    loses[k]+=1
        elif temp1>maches[i][j]:
            for k in scores:
                if t==k:
                    scores[k]+=3
                    wins[k]+=1
                if k==j:
                    loses[k]+=1
        elif temp1==maches[i][j]:
            for k in scores:
                if k==t:
                    scores[k]+=1
                    draws[k]+=1
                if k==j:
                    scores[k]+=1
                    draws[k]+=1
        

        t2=j
    


for i in range(len(maches)):
    temp=''
    for j in maches[i]:
        goals_difference[j]+=maches[i][j]
        if temp=='':
            temp=j
        if j!=temp:
            goals_difference[temp]-=maches[i][j]
            goals_difference[j]-=maches[i][temp]


for i in range(len(teams)):
    for j in wins:
        if teams[i][0]==j:
            teams[i][1]['wins']=wins[j]
            break
    
    for j in loses:
        if teams[i][0]==j:
            teams[i][1]['loses']=loses[j]
            break
    
    for j in goals_difference:
        if teams[i][0]==j:
            teams[i][1]['goals_difference']=goals_difference[j]
            break
    
    for j in scores:
        if teams[i][0]==j:
            teams[i][1]['score']=scores[j]
            break

    for j in draws:
        if teams[i][0]==j:
            teams[i][1]['draws']=draws[j]
            break

for h in range(len(teams)):
    for i in range(len(teams)):
        if i==0:
            temp=[i,teams[i][1]]
        elif temp[1]['score']<teams[i][1]['score']:
            t_temp=teams[i]
            teams[i]=teams[temp[0]]
            teams[temp[0]]=t_temp
            temp=[i,teams[i][1]]
        elif temp[1]['score']==teams[i][1]['score']:
            if teams[i][1]['wins']<teams[temp[0]][1]['wins']:
                t_temp=teams[i]
                teams[i]=teams[temp[0]]
                teams[temp[0]]=t_temp
            elif teams[i][1]['wins']==teams[temp[0]][1]['wins']:
                if ord(teams[i][0][0])<ord(teams[temp[0]][0][0]):
                    t_temp=teams[i]
                    teams[i]=teams[temp[0]]
                    teams[temp[0]]=t_temp

for i in range(len(teams)):
    print(teams[i])

