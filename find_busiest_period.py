def find_busiest_period(data):
  
  tracker = max_visitors= max_epoch = 0

  for i in data:
    epoch, visitors, entered = i
    
    if entered == 1:
      tracker += visitors
    else:
      tracker -= visitors
    
    if tracker > max_visitors:
      max_visitors = tracker
      max_epoch = epoch
    
  return max_epoch
    
    
print find_busiest_period([[1487799425,14,1],[1487799425,4,0],[1487799425,2,0],[1487800378,10,1],[1487801478,18,0],[1487801478,18,1],[1487901013,1,0],[1487901211,7,1],[1487901211,7,0]])