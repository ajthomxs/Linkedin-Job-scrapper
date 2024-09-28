# Import dependancies
import os
import time
import pandas as pd

# get the current working directory
cwd = os.getcwd()
# construct the full path to the CSV file
op = os.path.join(cwd, 'output', 'output.csv')


def edat(job,loc):

    jobdata= pd.read_csv(op,index_col=0)    

    # Fill NA Data
    jobdata["Seniority level"] = jobdata["Seniority level"].replace(['Not Applicable'], 'Freelance/Other')
    jobdata['Employment type']=jobdata['Employment type'].fillna("Other")
    jobdata['Job function']=jobdata['Job function'].fillna(job)
    jobdata['Industries']=jobdata['Industries'].fillna("IT Services and IT Consulting")
    jobdata['Seniority level']=jobdata['Seniority level'].fillna("Freelance/Other")

    # Clean Data a little bit
    # Clean the Jobs
    jobm = job.split()
    jobdata['Job title'] = jobdata['Job title'].apply(lambda x: job if any(word in x for word in jobm) else x)
    #Clean location
    jobdata['City'] = jobdata['City'].apply(lambda x: loc)

    print("Processing Data Now")
    time.sleep(2)
    jobdata.to_csv('output/test.csv')
    print("Data Cleaning done")
    time.sleep(2)
    
