import re
try:
    file = open('moving Out Bills2.txt')
except:
    print('Failed to open file')

income = int(input('Please enter how much you made this week '))
d1 = {}#Name and date
d2 = {}#Name and cost
dp= {}
total = 0
#List of bill names
b_name = list()
#Dates only
date = list()
#Number Range
l = list()

for x in file :
    if len(x) >= 2:
        s = re.sub("^\s+|\s+$", "", x)
        #Finding all the bills based off the dates & pulling the amount
        f = re.findall('/\d*\s\S.+=\s\$([0-9]+)', s)
        #Pulling the names and dates
        b = re.findall('/(\d*\s\S.+)=\s', s)
        if len(f) == 1 :
            for i in b :
                d = re.split('\s',b[0])
                pint = int(d[0])
                b_name = d[1]
                d1[b_name] = pint
            for we in f :
                d2[f"{b_name}"] = int(f[0])

#Putting the two dictionaries into a nested one
for key,value in d1.items():
    if value not in dp:
        dp[value] = set()
    if key in d2:
        dp[value].add((key,d2[key]))
results = sorted(dp.items(), key=lambda x:x)
d_results = dict(results)


#Date range search
date_range = range(5,26)

for p in date_range :
    l.append(p)
#Filter out only the numbers that match date_range
f_results = {}
for po in d_results:
    if po in l:
        f_results[po] = d_results[po]
        inside_dic = d_results[po]
        for num in inside_dic:
            total += num[1]
print('Date search',date_range, '\n''These are your upcoming bills')
for loop in f_results:
    print(loop, f_results[loop])
print('Total is',(f"${total} \n"))
#Budgeting is assuming we are following the 20/75/5
#20 For me
#75 Debt
#5 Savings
debt = income * 0.75
left_over = debt - total
self = round(income * 0.20)
savings = round(income * 0.05)
print('Debt', (f'${debt}'), '-', (f'${total} ='), (f'${left_over}'))
print('For me', (f'${self}'))
print('Savings', (f'${savings}'))     
file.close()
  