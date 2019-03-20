import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = '../source_data/sitka_weather_2014.csv'
with open(filename, 'r') as fobj:
    reader = csv.reader(fobj)
    header_row = next(reader)
    # print(header_row)
    #
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    dates = []
    highs = []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)
        highs.append(int(row[1]))
    # print(highs)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')

plt.title('Daily high temperatures, - 2014',fontsize=24)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)

plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()