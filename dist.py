import pandas as pd
import plotly.graph_objects as go
import random
import statistics
import plotly.figure_factory as ff

df=pd.read_csv('data.csv')
data=df["reading_time"]
mean=statistics.mean(data)
print("Population mean of data is :",mean)

def mean_of_rand_samples(counter):
    dataset=[]
    for i in range(0,counter):
        randIndex=random.randint(0,len(data))
        val=data[randIndex]
        dataset.append(val)
    mean=statistics.mean(dataset)
    return mean 

def plotGraph(meanlist):
    df=meanlist
    fig=ff.create_distplot([df],["Reading Time"])
    fig.show()

def setup():
    meanlist=[]
    for i in range(0,100):
        setOfMeans=mean_of_rand_samples(30)
        meanlist.append(setOfMeans)
    plotGraph(meanlist)
    mean=statistics.mean(meanlist)
    print("Sampling mean of data is :",mean)

setup()

