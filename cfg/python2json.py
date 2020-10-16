import json

data = {}
data['Grayscale_threshold'] = []
data['Grayscale_threshold'].append(2.5)

# print(data['no_of_colors'][0])
with open('cfg/threshold.txt','w') as file:
    json.dump(data, file)

