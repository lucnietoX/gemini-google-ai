import google.generativeai as genai
import os
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import pandas as pd
import io
import base64
from PIL import Image
import PIL.Image

#Configure the Google AI Vertex
key=open("key.txt","r").readlines()[0]
genai.configure(api_key=key)
model = genai.GenerativeModel('gemini-1.5-flash')

#Import the data from NVIDIA Stock dataset
data=pd.read_csv("dataset_nvidia_stocks.csv")
data['Date'] = pd.to_datetime(data['Date'])
data2 = data[data['Date'] >= '2020-01-01']

#Generate the trend chart
plt.figure(figsize=(10, 5))
plt.plot(data2['Date'], data2['Close'], marker='.', linestyle='-', color='#76b900')
plt.title("NVIDIA Stocks Close price - since 2020 - daily")
plt.xlabel("Dates")
plt.ylabel("Price")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
p = 'nvidia_chart_trend.png'
plt.savefig(p)
#Convert Image

img = PIL.Image.open(p)
#Ask to Gemini

text = "Please, analyze and see what happened in the last 3 months? What was the contribution to increase NVIDIA price?"
response = model.generate_content([text ,img])
print(response.text)