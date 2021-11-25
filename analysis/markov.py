import csv
import numpy as np
import random as rm
import sys
import matplotlib.pyplot as plt

np.set_printoptions(threshold=sys.maxsize)

states = ["active","inactive"]
transitionMatrix = [[0.6,0.4],[0.2,0.8]]
transitionName = [["AA","AI"],["IA","II"]]

def state_forecast(time):
    cur = "active"
    # print("start state: "+ cur)
    stateList = [cur]
    i = 0
    prob = 1
    while i != time:
        if cur == "active":
            change = np.random.choice(transitionName[0],replace = True,p = transitionMatrix[0])
            if change == "AA":
                prob = prob * 0.7
                stateList.append("active")
                pass
            else:
                prob = prob * 0.3
                cur = "inactive"
                stateList.append("inactive")
        else:
            change = np.random.choice(transitionName[1], replace=True, p=transitionMatrix[1])
            if change == "IA":
                prob = prob * 0.4
                stateList.append("active")
                pass
            else:
                prob = prob * 0.6
                cur = "inactive"
                stateList.append("inactive")

        i += 1
    return stateList[time]

def ILWC_reader(line):
    with open('ILWC1.csv','r') as csvfile:
        reader = csv.reader(csvfile)
        for i,rows in enumerate(reader):
            if i == line:
                real_activity = rows
    # print(real_activity)
    cnt = 0
    for index,value in enumerate(real_activity):
        if value == '0':
            real_activity[index] = 'inactive'
            cnt += 1
        else:
            real_activity[index] = 'active'
    inactive_prob = (cnt / len(real_activity)) * 100
    # print(real_activity)
    # print(len(row))
    # print("inactive_prob = " + str(inactive_prob) + "%")
    return real_activity


def experiment_set():
    pred_activity = []
    count = 0
    for t in range(1,600000):
        if t % 600 == 0:
            pred_activity.append(state_forecast(t))

    for smalllist in pred_activity:
        if smalllist == "inactive":
            count += 1

    interrupt_prob = (count/len(pred_activity)) * 100
    print(len(pred_activity))
    print("==========================================")
    print("interrupt probability = " + str(interrupt_prob))
    print("==========================================")
    real_activity = ILWC_reader(1250)
    broken = 0
    waste = 0
    for i in range(0, 999):
        if  pred_activity[i] == 'active' and real_activity[i] == 'inactive':
            broken += 1
        elif pred_activity[i] == 'inactive' and real_activity[i] == 'active':
            waste += 1
        elif pred_activity[i] == 'active' and real_activity[i] == 'active':
            pass
        else:
            pass

    return broken, waste

def markov_exp_run(round):
    wasteList = []
    brokenList = []
    totalList = []
    for i in range(round):
        broken, waste = experiment_set()
        brokenList.append(broken)
        wasteList.append(waste)
    for i in range(len(wasteList)):
        totalList.append(1000)
    print("wasteList = ")
    print("==========================================")
    print(wasteList)
    print("brokenList = ")
    print("==========================================")
    print(brokenList)
    return wasteList, brokenList, totalList

def result_plot(l1,l2,l3):
    plt.figure(figsize=(8, 6))
    total_width, n = 0.9, 3
    width = total_width / n

    x = [0,1,2,3,4,5,6,7,8,9]
    y1 = l1
    y2 = l2
    y3 = l3
    plt.bar(x, y1, width=width, color='g', label='waste')
    for a,b in zip(x,y1):
        plt.text(a,b,'%d'%b,ha='center',va='bottom',fontsize=8)
    for i in range(len(x)):
        x[i] = x[i] +width
    plt.bar(x, y2, width=width, color='b', label='interrupt')
    for a,b in zip(x,y2):
        plt.text(a,b,'%d'%b,ha='center',va='bottom',fontsize=8)
    for i in range(len(x)):
        x[i] = x[i] +width
    plt.bar(x, y3, width=width, color='c', label='total')
    for a,b in zip(x,y3):
        plt.text(a,b,'%d'%b,ha='center',va='bottom',fontsize=8)

    plt.xlabel('experiment rounds (times/1)')
    plt.ylabel('interrupted or wasted laser links(times/1)')
    plt.title('interrupted or wasted')
    plt.legend()
    plt.show()
    plt.savefig("./markov.png")



if __name__ == "__main__":
    wasteList, brokenList, totalList = markov_exp_run(10)
    result_plot(wasteList, brokenList, totalList)
    '''
    l1 = [77, 84, 71, 76, 75, 65, 71, 79, 79, 75]
    l2 = [0, 1, 1, 1, 1, 1, 3, 1, 0, 0]
    l3 = [100,100,100,100,100,100,100,100,100,100]
    result_plot(l1,l2,l3)
    '''






