import json as js

json_list=[]

with open('csv_file.txt','r') as csv:
    for line in csv.readlines():
        country, club, player = line.strip().split(",")
        data={
            'country':country,
            'club':club,
            'player':player
        }

        json_list.append(data)

with open("json_file.txt","w") as json_file:
    js.dump(json_list,json_file)
