# EDA using web Scrapper by Akil Ajith,Ajay Thomas and Vignesh Ramanathan
# Import Files
import os
import time
import pandas as pd
import webbrowser
from modules import input_user as i
from modules import scrapper as s
from modules import eda as op
from output import *

print("Welcome to AAV's Job Scrapper EDA program")
print("""Choose your Job Title
1.Machine Learning Engineer
2.Data Scientist
3.Data Analyst""")

job=i.get_job()
print("""Choose your Job Location
      1.Banglore
      2.Chennai
      3.Mumbai""")
loc=i.get_loc()

#Scraping Linkedin for Jobs
print("Web Scrapping Now")
# Delay the print statement for 20 seconds
time.sleep(2)
csvf=s.scrap_job(job,loc)
print(" Web Scraping Done and Output Saved")
      

#Performing Data Cleaning 
peda=op.edat(job,loc)
time.sleep(2)

os.system('py modules/dispdata.py')


