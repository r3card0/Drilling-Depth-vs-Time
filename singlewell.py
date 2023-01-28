import pandas as pd
import matplotlib.pyplot as plt

# Data
plan = {
    'days': [0,10,15,25,35,50,60],
    'md' : [0,-1500,-1500, -2546,-2546, -3890,-3890],    
}

real = {
    'days': [0,8,23,25,26,33,43,55,61],
    'md' : [0,-1501,-1501,-1880,-1880,-2450,-2450,-3887,-3887],
}


# convertir data a dataframe
def dataframe(data):
    df = pd.DataFrame(data)
    return df

df = dataframe(plan)
# avance
dfr = dataframe(real)



# Depth vs Time Chart
def depthTimeChart(wellname):
    plt.style.use('bmh')
    fig, axes = plt.subplots(figsize=(12,12))
    axes.plot(df['days'],df['md'],'b',linestyle='--',label="Planned Depth")
    axes.plot(dfr['days'],dfr['md'],'r',label="Actual Depth")
    plt.xlabel('Drilling Days')
    plt.ylabel('Measured Depth (m)')
    plt.title(f'{wellname} - Drilling Depth vs Time',color='#000000',fontsize=16)
    axes.legend()
    # plt.show()

# send chart to pdf format
def sendChartPdf(wellname):
    depthTimeChart(wellname)
    plt.savefig(f'{wellname}_depthTimeChart.png')
    plt.close()


def run():
    # depthTimeChart('Wildcat-1')
    sendChartPdf('Wildcat-1')
   

if __name__ == "__main__":
    run()