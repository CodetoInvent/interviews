# Given an array of meeting time intervals consisting of start and end times 
# [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.


times = [[0,10],[1,10]]

def meeting_calc(intervals):
  intervals = sorted(intervals, key=lambda x: x[0])
        
  for i in range(len(intervals)-1):
    current_meeting_end, next_meeting_start = intervals[i][1], intervals[i+1][0]
    
    if current_meeting_end > next_meeting_start: 
      print current_meeting_end,  next_meeting_start
      
      return False
        
  return True

print meeting_calc(times)