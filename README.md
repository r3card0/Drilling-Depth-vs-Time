# Drilling Depth vs Time Chart
![image](/img/Wildcat-1_depthTimeChart.png)

This is a data visualization tool with the objective to support the closing of a drilling project by documenting and comparing the performance of the drilling execution.

The tool plots the data (planned and actual) and automate the creation of a pdf file of the plot.


## Deploy on Google Colab
1. Go to -> [notebook](https://colab.research.google.com/drive/1nw6L8S8iY4pXfiIabYhHdPhxkk0z9X9E?usp=share_link)

## Deploy on local directory
1. Define a local directory  
2. Create a virtual environment ```python3 -m venv name```
3. Activate the virtual environment
4. Install python libraries: ```pip install pandas matplotlib```
5. Download the repo
6. Open and modify the [singlewell.py](/main/singlewell.py) file and set the planned/actual data from line ```6``` to line ```12``` and set the name of the well on line ```53```
7. Run script [singlewell.py](/main/singlewell.py) and look the pdf file created on local directory.
