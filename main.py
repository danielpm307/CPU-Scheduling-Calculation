

import func

#sample of Tasks[ARRIVAL_Time,BURST_Time]
gData = {'P1': [0,10], 'P2': [1,2], 'P3': [4,4], 'P4':[5,1], 'P5': [10,3], 'P6':[21,12]}
TQuant = 4
#gContSwitch = 0.4


print("***************************** fcfs Scheduling *******************************")
# fcfsScheduling,fcfsLine = func.fcfs(gData)
# sjfScheduling,sjfLine = func.sjf(gData)
# srtfScheduling,srtfLine = func.srtf(gData)
rrobinScheduling,rrLine = func.rrobin(gData,TQuant)
# func.printData(gData,fcfsScheduling,fcfsLine,'First Come First Serve')
# func.printData(gData,sjfScheduling,sjfLine,'Shortest Job First')
# func.printData(gData,srtfScheduling,srtfLine,'Shortest Remaning Time First')
func.printData(gData,rrobinScheduling,rrLine,'Round Robin QT={}'.format(TQuant))
#sum([len(x) for x in my_dict.values()]) summing to make avg answer
