

def plan():
    timesA = [[450, 600], [100, 500], [700, 900]]
    timesB = [[850, 1000], [300, 600]]

    duration = 200

    sort = lambda x: x[0]
    timesA = sorted(timesA, key=sort)
    timesB = sorted(timesB, key=sort)
    # [[100, 500], [450, 600], [700, 900]]
    # [[300, 600], [850, 1000]]


    i = j = 0

    while i < len(timesA) and j < len(timesB):
        start = max(timesA[i][0], timesB[j][0])
        end = min(timesA[i][1], timesB[j][1])
        
        if start + duration <= end:
            return [start, start + duration]
        else:
            if timesA[i][1] < timesB[j][1]:
                i += 1
            else:
                j += 1

    return []

print plan()
