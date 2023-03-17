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


class Depth_vs_Days:
    def __init__(self,wellName:str) -> None:
        self.wellName = wellName

    # convertir data a dataframe
    def dataframe(self,data):
        self.data = data
        df = pd.DataFrame(self.data)
        return df

    # Depth vs Time Chart
    def depthTimeChart(self):
        planned = Depth_vs_Days(self.wellName)
        df_plan = planned.dataframe(plan)
        drilled = Depth_vs_Days(self.wellName)
        df_real = drilled.dataframe(real)
        plt.style.use('bmh')
        fig, axes = plt.subplots(figsize=(12,12))
        axes.plot(df_plan['days'],df_plan['md'],'b',linestyle='--',label="Planned Depth")
        axes.plot(df_real['days'],df_real['md'],'r',label="Actual Depth")
        plt.xlabel('Drilling Days')
        plt.ylabel('Measured Depth (m)')
        plt.title(f'{self.wellName} - Drilling Depth vs Time',color='#000000',fontsize=16)
        axes.legend()
        # plt.show()
    

    # send chart to pdf format
    def sendChartPdf(self):
        Depth_vs_Days(self.wellName).depthTimeChart()
        plt.savefig(f'{self.wellName}_depthTimeChart.pdf')
        plt.close()



def run():
     
    well1 = Depth_vs_Days('Wildcat-1')
    well1.sendChartPdf()
    
   

if __name__ == "__main__":
    run()