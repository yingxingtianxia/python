import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = '../source_data/death_valley_2014.csv'
with open(filename, 'r') as fobj:
    reader = csv.reader(fobj)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(date, 'missing data')
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)

    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    plt.title('Daily high and low temperatures of death_valley, - 2014', fontsize='24')
    plt.xlabel('', fontsize=14)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (F)', fontsize=14)

    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

