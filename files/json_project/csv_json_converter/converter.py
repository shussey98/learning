import json

teams = open('csv_file.txt','r')
data = [lines.strip() for lines in teams]
teams.close()

dict_list=[]
for line in data:
    team_dict = {}
    team_data = line.split(',')
    team_dict['club'] = team_data[0]
    team_dict['country'] = team_data[2]
    team_dict['city'] = team_data[1]

    dict_list.append(team_dict)

json_teams = open('json_file.txt','w')
json.dump(dict_list,json_teams)
json_teams.close()


print(dict_list)