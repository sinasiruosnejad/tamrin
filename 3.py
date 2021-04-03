number_of_people=int(input("how many people are there for this survey? "))
survey={}
geners={"Horror":0 , "Romance":0 , "Comedy":0 , "History":0 , "Adventure":0 , "Action":0 }
geners_list=[]
for i in range(number_of_people):
    temp_name=input('\nplease enter your name: ')
    for j in survey:
        if j==temp_name:
            temp_name=input("please enter another name this name has been used before: ")
    temp_geners=input('please enter your favorite geners of movie among these:\nHorror  Romance  Comedy  History  Adventure  Action\n')
    survey.update({str(temp_name):temp_geners})

for i in survey:
    temp=''
    for j in range(len(survey[i])+1):
        if len(temp)==6 or len(temp)==7 or len(temp)==9:
            for k in geners:
                if k==temp:
                    geners[k]+=1
                    temp=''
                    break
            else:
                temp+=survey[i][j]
        else:
            temp+=survey[i][j]


for i in geners:
    geners_list.append([i,geners[i]])



for i in range(len(geners_list)):
    t=i
    for j in range(i,len(geners_list)):
        if j!=i:
            if geners_list[i][1]<geners_list[j][1]:
                temp=geners_list[j]
                geners_list.pop(j)
                geners_list.insert(i,temp)
            elif geners_list[i][1]==geners_list[j][1]:
                for k in range(9):
                    ok=ord(geners_list[j][0][k])
                    oi=ord(geners_list[i][0][k])
                    if ok!=oi:
                        if oi>ok:
                            temp=geners_list[j]
                            geners_list.pop(j)
                            geners_list.insert(i,temp)
                            break
                        else:
                            break

for i in range(len(geners_list)):
    print(f"{geners_list[i][0]}: {geners_list[i][1]}")