import datetime

def get_departures():
    departures = []
    with open('amtrak-data.txt') as f:
        for line in f.readlines():
            departure = get_departure(line)
            if departure:
                departures.append(departure)
    return departures

def get_departure(line):
    '''Return a tuple containing two datetime.datetime objects.'''

    return (planned_departure, actual_departure)

def main():
    departures = get_departures()
    ontime_departures = [d for d in departures if d[1] == d[0]]
    late_departures = [d for d in departures if d[1] > d[0]]
    next_day_departures = [d for d in departures if
                           d[0].day != d[1].day]
            
    print('''Total Departures: {}
Ontime Departures: {}
Late Departures: {}
Next Day Departures: {}'''.format(len(departures),
                                   len(ontime_departures),
                                   len(late_departures),
                                   len(next_day_departures)))

main()