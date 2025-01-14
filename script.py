import json
with open('precipitation.json') as file:
    contents = json.load(file)
# print(contents)
Seattle_data = []
for entry in contents:
    if entry['station'] =='GHCND:US1WAKG0038':
        Seattle_data.append(entry)
 
monthly_precipitation = {
    1 : [],
    2 : [],
    3 : [],
    4 : [],
    5 : [], 
    6 : [],
    7 : [],
    8 : [],
    9 : [],
    10 : [],
    11 : [],
    12 : []
}

for entry in Seattle_data:
    date = entry['date'].split('-')
    month = int((date[1]))
    monthly_precipitation[month].append(entry['value'])

# print(monthly_precipitation)

monthly_precipitation_total = {
    1 : [],
    2 : [],
    3 : [],
    4 : [],
    5 : [], 
    6 : [],
    7 : [],
    8 : [],
    9 : [],
    10 : [],
    11 : [],
    12 : []
}
for month in monthly_precipitation:
    monthly_precipitation_total[month].append(sum(monthly_precipitation[month]))

print(monthly_precipitation_total)

with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(monthly_precipitation_total, file, indent=4, ensure_ascii=False)