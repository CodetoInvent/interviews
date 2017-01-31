import random
import json

timestamps = [{"time": 1000000 + (i * random.randint(0, 2)),
               "count": random.randint(0, 100),
               "type": "exit" if random.choice([True, False]) else "enter"}
              for i in range(10)]
print json.dumps(timestamps, indent=4)

def busiest_time(data):
    if (not data) or not len(data): return None

    current = maxi = maxi_timestamp = 0
    data = sorted(data, key=lambda x: x['time'])
    
    for i, entry in enumerate(data):
        if entry['type'] == 'enter':
            current += entry['count']
        elif entry['type'] == 'exit':
            current -= entry['count']

        if i < len(data) - 1:
            if data[i+1]['time'] == entry['time']: continue

        if current > maxi:
            maxi, maxi_timestamp = current, entry['time']

    return maxi, maxi_timestamp

# print timestamps
print busiest_time(timestamps)

timestamps = [
    {
        "count": 11, 
        "type": "enter", 
        "time": 1000000
    }, 
    {
        "count": 13, 
        "type": "exit", 
        "time": 1000001
    }, 
    {
        "count": 1, 
        "type": "exit", 
        "time": 1000004
    }, 
    {
        "count": 35, 
        "type": "enter", 
        "time": 1000000
    }, 
    {
        "count": 75, 
        "type": "exit", 
        "time": 1000004
    }, 
    {
        "count": 43, 
        "type": "enter", 
        "time": 1000000
    }, 
    {
        "count": 100, 
        "type": "exit", 
        "time": 1000006
    }, 
    {
        "count": 2, 
        "type": "exit", 
        "time": 1000000
    }, 
    {
        "count": 2, 
        "type": "enter", 
        "time": 1000000
    }, 
    {
        "count": 24, 
        "type": "enter", 
        "time": 1000000
    }
]

timestamps = sorted(timestamps, key=lambda x: x['time'])