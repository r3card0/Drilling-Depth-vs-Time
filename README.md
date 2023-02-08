# Drilling - depth vs days Plot

![image](/Wildcat-1_depthTimeChart.png)

This is a data visualization tool with the objective to support the closing of a drilling project by documenting the performance and use it into exploration and development phases of a oil & gas field.

The tool plots the data (planned and actual) and automate the creation of a pdf file of the plot.


## Deployment
Steps

1. Define a local directory  
2. Create a virtual environment ```python3 -m venv name```
3. Activate the virtual environment
4. Install python libraries: ```pip install pandas matplotlib```
5. Download the repo
5. Modify the [singlewell.py](https://github.com/r3card0/Drilling-Depth-vs-Time/blob/main/singlewell.py) file and set the planned/actual data from line ```6``` to line ```12``` and set the name of the well on line ```48```
6. Run script [singlewell.py](https://github.com/r3card0/Drilling-Depth-vs-Time/blob/main/singlewell.py), review the pdf file created of, and attach it into the final drilling report.
