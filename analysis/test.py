import numpy as np
import matplotlib.pyplot as plt
def test():
    dict = {x:0.5 for x in range(1000)}
    for x,y in dict.items():
        a = np.random.rand()
        if(a>0.5):
            state = 1
        else:
            state = 0



        b = np.random.rand()
        if(b>0.7):
            predict = 1-abs(state)
        else:
            predict = state

        if(state == 1 and predict == 1):
            result = 1
        elif(state == 1 and predict == 0 ):
            result = 0
        elif(state == 0 and predict == 1):
            result = 0
        else:
            result = 1
        dict[x] = result
        print (state,predict)
        print(x,result)
    x1 = np.arange(0,1000,1)
    y1 =[]
    cnt = 0
    for i in dict.values():
        y1.append(i)
        if(i==0):
            cnt=cnt+1
    print(cnt)
    plt.figure(figsize=(8, 6))

    plt.xlim(0,1000)
    plt.ylim(-0.5,1.5)
    plt.xlabel("time(t)",fontsize = 20)
    plt.ylabel("interrupt or not",fontsize = 20)
    plt.plot(x1,y1)
    plt.title("probability of interrupt", fontsize=30)
    plt.savefig("/ccr-submission-code/figures/a.png")
    plt.show()

if __name__ == "__main__":
    test()




