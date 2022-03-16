import pandas as pd
import plotly_express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import statistics
import random
import csv

df=pd.read_csv('data2.csv')
data=df['reading_time'].tolist()

mean=statistics.mean(data)
std=statistics.stdev(data)

fig=ff.create_distplot([data],['plot'])
fig.show()

print('population mean is : ',mean)
print('standard deviation is :',std)

def random_st_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        randIndex=random.randint(0,len(data)-1)
        val=data[randIndex]
        dataset.append(val)
    mean1=statistics.mean(dataset)
    print('population mean is :',mean1)
    return mean

meanlist=[]
for i in range(0,100):
    setOfMean=random_st_of_mean(30)
    meanlist.append(setOfMean)

def plot(meanlist):
    df=meanlist
    fig=ff.create_distplot([df],['temp'])
    fig.show()

firstStdStart,firstStdEnd=mean-std,mean+std
secondStdStart,secondStdEnd=mean-(std*2),mean+(std*2)
thirdStdStart,thirdStdEnd=mean-(std*3),mean+(std*3)


fig1=ff.create_distplot([meanlist],["student marks avg"])
fig1.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))

fig1.add_trace(go.Scatter(x=[firstStdStart,firstStdStart],y=[0,0.17],mode="lines",name="std1 start"))
fig1.add_trace(go.Scatter(x=[firstStdEnd,firstStdEnd],y=[0,0.17],mode="lines",name="std 1 end"))
fig1.add_trace(go.Scatter(x=[secondStdStart,secondStdStart],y=[0,0.17],mode="lines",name="std 2 start"))
fig1.add_trace(go.Scatter(x=[secondStdEnd,secondStdEnd],y=[0,0.17],mode="lines",name="std 2 end"))
fig1.add_trace(go.Scatter(x=[thirdStdStart,thirdStdStart],y=[0,0.17],mode="lines",name="std 3 start"))
fig1.add_trace(go.Scatter(x=[thirdStdEnd,thirdStdEnd],y=[0,0.17],mode="lines",name="std 3 end"))

fig1.show()


