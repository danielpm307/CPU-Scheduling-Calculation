
gData = {'P1': [0,10], 'P2': [1,2], 'P3': [4,4], 'P4':[5,1], 'P5': [10,3], 'P6':[21,12]}


TQuant = 4

begHold = 0
rrdict,pLine = {},[]
TasksName = list(gData.keys())
ArriveTime,BurstTime = map(list, zip(*dict.values()))
ArriveTimeHold,BurstTimeHold = ArriveTime.copy(),BurstTime.copy()
for TaskNum in range(len(TasksName)) :
    if (ArriveTimeHold[TaskNum] <= begHold):
        if (ArriveTimeHold[TaskNum] <= TQuant):
            if(BurstTimeHold[TaskNum] > 0):
                if (BurstTimeHold[TaskNum] > TQuant):
                    begHold += TQuant
                    BurstTimeHold[TaskNum] -= TQuant
                    ArriveTimeHold[TaskNum] += TQuant
                    pLine.append([TasksName[TaskNum],begHold])
                else:
                    begHold += BurstTimeHold[TaskNum]
                    rrdict[TasksName[TaskNum]] = [begHold-BurstTime[TaskNum]-ArriveTime[TaskNum],begHold-ArriveTime[TaskNum]]
                    BurstTimeHold[TaskNum] = 0
                    pLine.append([TasksName[TaskNum],begHold])
            elif ArriveTimeHold[TaskNum] > TQuant:
                    for NewTaskNum in range(len(TasksName)):
                        if (ArriveTimeHold[NewTaskNum]<ArriveTimeHold[TaskNum]):
                            if(BurstTimeHold[NewTaskNum] > 0):
                                flag = False
                                if(BurstTimeHold[NewTaskNum] > TQuant):
                                    begHold += TQuant
                                    BurstTimeHold[NewTaskNum] -= TQuant
                                    ArriveTimeHold[NewTaskNum] += TQuant
                                    pLine.append([TasksName[NewTaskNum],begHold])
                                else:
                                    begHold += BurstTimeHold[NewTaskNum]
                                    rrdict[TasksName[NewTaskNum]] = [begHold-BurstTime[NewTaskNum]-ArriveTime[NewTaskNum],begHold-ArriveTime[NewTaskNum]]
                                    BurstTimeHold[NewTaskNum] = 0
                                    pLine.append([TasksName[NewTaskNum],begHold])
                    if(btHold[i]>0):
                        flag = False
                        if(btHold[i]>quantum):
                            begHold += quantum
                            btHold[i] -= quantum
                            atHold[i] += quantum
                            pLine.append([keyP[i],begHold])
                        else:
                            begHold += btHold[i]
                            rrdict[keyP[i]] = [begHold-bt[i]-at[i],begHold-at[i]]
                            btHold[i] = 0
                            pLine.append([keyP[i],begHold])
            elif(atHold[i]>begHold):
                begHold += 1
                i -= 1
        if(flag):
            break
    return rrdict,pLine
