# -*- coding: utf-8 -*-
"""
Name: KURRE SAI KRISHNA REDDY 
Student ID: 22073063
Module: 7PAM2000-0901-2023 - Applied Data Science 1
Course: Msc Data Science (SW) with Placement Year
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def barChart(data,df):
    '''
    Parameters
    ----------
    data : dataframe collected which is passeed argument from the main function
    position: It is the dataframe of worldbank data

    Returns
    -------
    The function plots the bar graph over the years 1995-2015 for the countries United states, India, China, Russian Federation
    '''
    data.plot(kind="bar", figsize=(10, 5))
    plt.title("Electricity production from coal sources (% of total)")
    plt.xlabel("Countries")
    plt.ylabel("Electricity production %")
    plt.legend()
    plt.show()
    
    df.plot(kind="bar", figsize=(10, 5))
    plt.title("Electricity production from nuclear sources (% of total)")
    plt.xlabel("Countries")
    plt.ylabel("Electricity production %")
    plt.legend()
    plt.show()
    
def lineChart(fileName,country):
    '''
    Parameters
    ----------
    fileName : fileName is the argument passed from the main function
    country: country is the argument passed from the main function

    Returns
    -------
    The function plots the line graphs over the years 1995-2015 for the countries, over the various sources of Electricity production
    '''
    df = pd.read_csv(fileName,skiprows=3)
    df = df[df['Country Name']==country]
    Indicator = ["EG.ELC.PETR.ZS","EG.ELC.NUCL.ZS","EG.ELC.NGAS.ZS","EG.ELC.HYRO.ZS","EG.ELC.COAL.ZS"]
    year = ["2000","2005","2010","2015"]
    df.set_index('Indicator Code',inplace=True)
    df = df.loc[Indicator,year]
    
    df= df.transpose()
    
    df.plot(kind="line",figsize=(10,5))
    plt.title("Electricity production from coal sources (% of total) " + country)
    plt.xlabel("Indicators")
    plt.ylabel("Electricity Production % total")
    plt.legend()
    plt.show()
    

def heatMap(data,country):
    '''
    Parameters
    ----------
    data : The data is the file name parsed from the main function, for reading csv file and considering indicators.

    Returns
    -------
    The function plots the heatMap over the years 1995-2015 for the countries, over the various sources of Electricity production
    '''
    df = pd.read_csv(data,skiprows=3)
    indicators = ["EG.ELC.PETR.ZS","EG.ELC.NUCL.ZS","EG.ELC.NGAS.ZS","EG.ELC.HYRO.ZS","EG.ELC.COAL.ZS"]
    
    data=df.loc[df['Country Name']==country]
    data = data.loc[data['Indicator Code'].isin(indicators)]
    data = data.loc[:,["Country Name","Indicator Name","2000","2002","2004","2006","2008","2010","2012","2014"]]
    print(data)
    # creating Pivot table for dataframe
    
    df_g = data.pivot_table(data,columns= data['Indicator Name'])

    print(df_g)
    # ploting the heatmap with the correlation between the mentioned indicators
    plt.figure(figsize=(10, 6))
    sns.heatmap(df_g.corr(), annot=True, fmt='.2f', cmap='YlGnBu')
    
    # add title and axis labels
    plt.title(f'{country} Indicators Heatmap')
    plt.xlabel('Year')
    plt.ylabel('Indicator')
    
    # show the plot
    plt.show()

def readCSVFile(file):
    '''
    Parameters
    ----------
    file: file is the argument passed from the main function
    
    Returns
    -------
    The function returns the datafrane over the years 1995, 2000, 2010, 2015 for the countries, for the production of electricity from coal sources
    '''
    # Read the Csv File
    data = pd.read_csv(fileName,skiprows=3)
    loc = ["United States","India","China","Russian Federation"]
    year = ["1995","2000","2005","2010","2015"]
    data.set_index('Country Name',inplace=True)
    
    #filtering the data with the selected indicator name
    data_elec = data[data["Indicator Name"] == "Electricity production from coal sources (% of total)"]
    data_elec_ng = data[data["Indicator Name"] == "Electricity production from nuclear sources (% of total)"]
    
    data_elec = data_elec.loc[loc,year]
    data_elec_ng = data_elec_ng.loc[loc,year]
    
    #transpose the file
    data_elec_t = data_elec.transpose()
    
    data_elec.info()
    data_elec.describe()
    data_elec_t.describe()
    
    return data_elec,data_elec_t,data_elec_ng

# Main Function

fileName = "API_19_DS2_en_csv_v2_6183479.csv"


# Calling the file to read the csv file 
df,df_t,data_ng = readCSVFile(fileName)

# Calling the barChart function to plot the bar graph
barChart(df,data_ng)

# Calling the lineChart function to plot the line graph
lineChart(fileName,"India")
lineChart(fileName,"United States")

# Calling the heatMap function to plot the heatMap
heatMap(fileName,"India")
heatMap(fileName,"United States")
