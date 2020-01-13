import pandas as pd
import dateutil.parser as parser
from datetime import timedelta, date

url = 'https://en.wikipedia.org/wiki/2019_in_spaceflight'
year = "2019 "
df = pd.read_html(url) #reading the URL using the panda library
d = df[3]
listofdates = list()
result = list() #temporary results
res = list()  #final result list
start_date = date(2019, 1, 1)
end_date = date(2020, 1, 1)


def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

for index,row in d.iterrows():
    if(row[6] =='Successful' or row[6] == 'En route' or row[6] == 'Operational'):
        datetime = year + row[0].split('[')[0]
        parsed = parser.parse(datetime)
        listofdates.append(parsed.isoformat())

for i in listofdates:
    temp = i + "," + str(listofdates.count(i))
    result.append(temp)
final_result = list() #contains all dates with occurences (no duplicates)
for i in result:
    if i not in final_result:
        final_result.append(i)

temp = list() #temporary list
for each in result:
    temp.append(each.split('T')[0])
count = 0

for single_date in daterange(start_date, end_date):
    da = parser.parse(str(single_date))
    date_string = da.isoformat()
    if(date_string.split('T')[0]) in temp:
        try:
            while ((final_result[count].split('T')[0]) == (date_string.split('T')[0])):
                res.append(final_result[count])
                count += 1
        except:
            pass
    else:
        t = date_string +  ",0"
        res.append(t)

#writing into a csv file
f = open("output.csv",'w') 
f.write("date,value\n")
for i in res:
	f.write(i)
	f.write("\n")
f.close()
