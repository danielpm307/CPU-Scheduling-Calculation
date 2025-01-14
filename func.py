
#Round Robins   
def rrobin(dict,quantum):
    begHold = 0
    rrdict,pLine = {},[] #{} = dict
    keyP = list(dict.keys()) #keyp => list of process
    at,bt = map(list, zip(*dict.values()))
    atHold,btHold = at.copy(),bt.copy()
    while True:
        flag = True
        for i in range(len(keyP)): 
            if (atHold[i] <= begHold):
                if (atHold[i] <= quantum):
                    if(btHold[i] > 0):
                        flag = False
                        if (btHold[i] > quantum):
                            begHold += quantum
                            btHold[i] -= quantum
                            atHold[i] += quantum
                            pLine.append([keyP[i],begHold])
                        else:
                            begHold += btHold[i]
                            rrdict[keyP[i]] = [begHold-bt[i]-at[i],begHold-at[i]]
                            btHold[i] = 0
                            pLine.append([keyP[i],begHold])
                elif atHold[i] > quantum:
                    for j in range(len(keyP)):
                        if (atHold[j]<atHold[i]):
                            if(btHold[j] > 0):
                                flag = False
                                if(btHold[j] > quantum):
                                    begHold += quantum
                                    btHold[j] -= quantum
                                    atHold[j] += quantum
                                    pLine.append([keyP[j],begHold])
                                else:
                                    begHold += btHold[j]
                                    rrdict[keyP[j]] = [begHold-bt[j]-at[j],begHold-at[j]]
                                    btHold[j] = 0
                                    pLine.append([keyP[j],begHold])
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
def Drrobin(dict,quantum):
    begHold = 0
    rrdict,pLine = {},[]
    keyP = list(dict.keys())
    at,bt = map(list, zip(*dict.values()))
    atHold,btHold = at.copy(),bt.copy()
    while True:
        flag = True
        for i in range(len(keyP)):
            if (atHold[i] <= begHold):
                if (atHold[i] <= quantum):
                    if(btHold[i] > 0):
                        flag = False
                        if (btHold[i] > quantum):
                            begHold += quantum
                            btHold[i] -= quantum
                            atHold[i] += quantum
                            pLine.append([keyP[i],begHold])
                        else:
                            begHold += btHold[i]
                            rrdict[keyP[i]] = [begHold-bt[i]-at[i],begHold-at[i]]
                            btHold[i] = 0
                            pLine.append([keyP[i],begHold])
                elif atHold[i] > quantum:
                    for j in range(len(keyP)):
                        if (atHold[j]<atHold[i]):
                            if(btHold[j] > 0):
                                flag = False
                                if(btHold[j] > quantum):
                                    begHold += quantum
                                    btHold[j] -= quantum
                                    atHold[j] += quantum
                                    pLine.append([keyP[j],begHold])
                                else:
                                    begHold += btHold[j]
                                    rrdict[keyP[j]] = [begHold-bt[j]-at[j],begHold-at[j]]
                                    btHold[j] = 0
                                    pLine.append([keyP[j],begHold])
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
#Print Function + Calculation
def printData(gData, cData, pLine, Name):
    avgWT,avgTT =0,0
    plinestr= "0 -> "
    print(Name.upper())
    print('| KEY | ARRIVAL | BURST | WAIT | TURNAROUND |')
    for key,value in sorted(cData.items()):
        print('{:>4}{:>8}{:>9}{:>8}{:>10}'.format(key,gData[key][0],gData[key][1],value[0],value[1]))
        avgWT += value[0]
        avgTT += value[1]
    print('Average Wait Time = {}    Average Turnaround Time = {}\n'.format(avgWT/len(cData),avgTT/len(cData)))
    for x in pLine:
        plinestr += ('{} -> {} -> '.format(x[0],x[1]))
    print('{}\n'.format(plinestr[:-3]))