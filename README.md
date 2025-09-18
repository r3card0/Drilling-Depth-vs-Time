# Drilling Depth vs Time Chart Generator
![image](/img/Wildcat-1_depthTimeChart.png)

## 📋Description

A data visualization tool designed to support drilling project closure by documenting and comparing drilling execution performance.

## What does it do?
* 📊 Visualizes drilling data (planned vs. actual)
* 📈 Generates professional charts of depth vs. time
* ⚙️ Automates PDF creation with the generated plots
* 🎯 Compares performance between planned and actual execution


## 🚀 Usage Options
#### Option 1: Google Colab (Recommended for quick start)
📲 [Open in Google Colab](https://colab.research.google.com/drive/1nw6L8S8iY4pXfiIabYhHdPhxkk0z9X9E?usp=share_link)

1. Click the link above
2. Execute cells sequentially
3. Modify data according to your project
4. Visualize the Depth vs. Time Chart

In this option you just can modified the data and create the chart. Is not an automate process.

The best option is the second one.

#### Option 2: Local Installation
1. Define a local directory  
2. Create a virtual environment ```python3 -m venv name```
3. Activate the virtual environment
4. Install python libraries: ```pip install pandas matplotlib```
5. Download the repo
6. Open and modify the [singlewell.py](/main/singlewell.py) file and set the planned/actual data from line ```6``` to line ```12``` and set the name of the well on line ```53```
7. Run script [singlewell.py](/main/singlewell.py) and look the pdf file created on local directory.

## Use Cases
## Troubleshooting
## Contributing
## Support
## Acknowledgements

⭐  If this tool is useful to you, consider giving the project a star
