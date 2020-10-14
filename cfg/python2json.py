import json

data = {}
data['no_of_colors']=[]
data['Grayscale_threshold'] = []
data['color_to_apply']=[]
data['no_of_colors'].append(5)#to be set according to the image
data['Grayscale_threshold'].append(2)
data['color_to_apply'].append([1,0,0])#red 

# print(data['no_of_colors'][0])
with open('cfg/config.txt','w') as file:
    json.dump(data, file)

