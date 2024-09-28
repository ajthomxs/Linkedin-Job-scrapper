import os
from collections import Counter
import dash
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import webbrowser

# get the current working directory
cwd = os.getcwd()
# construct the full path to the CSV file
csv_path = os.path.join(cwd, 'output', 'test.csv')

# read in the CSV file
df = pd.read_csv(csv_path,index_col=0)
# Drop the 'Job link' and 'City' columns
df.drop(columns=['Job link', 'City'], inplace=True)

# Get the top 5 employment
top_employment = df["Employment type"].value_counts().head(4)

# Get the top 5 reoccurring job titles
top_job_titles = df["Job title"].value_counts().head(5)

# Get the top 5 industries
top_industries = df["Industries"].value_counts().head(3)

# Get the top 5 Job Function
top_job_function = df["Job function"].value_counts().head(5)

# Create a new dataframe with the top 5 job titles 
top_jobs_df = df[df["Job title"].isin(top_job_titles.index)]

# Create a new dataframe with the top 5 job Industries
top_industries_df = df[df["Industries"].isin(top_industries.index)]

# Create a new dataframe with the top job function and top industries 
top_jfinind_df = top_industries_df[top_industries_df["Job function"].isin(top_job_function.index)]

# Create the Scatter chart
fig1 = px.scatter(top_jobs_df, x='Job title', y='Seniority level',  color='Seniority level',orientation='h')
fig4 = px.scatter(top_jfinind_df, x='Industries', y='Job function',  color='Seniority level')

# Create the pie chart
fig2 = px.pie(top_job_titles, values='Job title', names=top_job_titles.index,title='Top Job Roles')
fig5 = px.pie(top_employment, values='Employment type', names=top_employment.index,title='Top Employment Type')

# Create the bar chart
fig3 = px.bar(top_industries_df, x='Industries', y='Industries',color='Industries',title='Top 3 Industries')

# Create the Dash app
app = dash.Dash()

# Add all charts to the app
app.layout = html.Div(children=[
    html.H1(children='EDA Dashboard for Linkedin Job Listings',style={'text-align': 'center'}),
    dcc.Tabs(id="tabs", children=[
        dcc.Tab(label='Top Jobs & Seniority level Required', children=[
            dcc.Graph(
                id='Jobs & Seniority level',
                figure=fig1
            )
        ]),
        dcc.Tab(label='Top Job functions in Top Industries', children=[
            dcc.Graph(
                id='Top jni Industries',
                figure=fig4
            )
        ])
    ]),
    html.Div(style={'display': 'flex', 'justify-content': 'space-between'}, children=[
        dcc.Graph(
            id='pie-chart-1',
            figure=fig2
        ),
        dcc.Graph(
            id='pie-chart-2',
            figure=fig5
        )
    ]),
    dcc.Graph(
        id='Top 5 Industries',
        figure=fig3

    )])


# run the app
if __name__ == '__main__':
    url='http://127.0.0.1:8050/'
    webbrowser.open(url)
    app.run_server(port=8050, debug=False)
    
