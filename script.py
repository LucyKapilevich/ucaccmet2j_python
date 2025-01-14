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
    value = sum(monthly_precipitation[month])
    monthly_precipitation_total[month].append(value)



with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(monthly_precipitation_total, file, indent=4, ensure_ascii=False)

yearly_precipitation = []

for month in monthly_precipitation_total:
    value = sum(monthly_precipitation[month])
    yearly_precipitation.append(value)

sums = sum(yearly_precipitation)

relative_monthly_precipitation = {
}
for month in monthly_precipitation:
    value = sum(monthly_precipitation[month])
    relative_monthly_precipitation[month] = value/sums *100


# print(monthly_precipitation_total)
# print(sums)
# print(relative_monthly_precipitation)

with open('resultss.json', 'w', encoding='utf-8') as file:
    json.dump(relative_monthly_precipitation, file, indent=4, ensure_ascii=False)