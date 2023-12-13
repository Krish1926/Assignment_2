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

def barchart(data,resource):
    '''
    Parameters
    ----------
    data : dataframe collected which is passeed argument from the main function
    position: It is the dataframe of worldbank data

    Returns
    -------
    The function plots the bar graph over the years 1995-2015 for the countries
    United states, India, China, Russian Federation
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

def linechart(filename,country):
    '''
    Parameters
    ----------
    fileName : fileName is the argument passed from the main function
    country: country is the argument passed from the main function

    Returns
    -------
    The function plots the line graphs over the years 1995-2015 for the
    countries, over the various sources of Electricity production
    '''
    df = pd.read_csv(fileName,skiprows=3)
    df = df[df['Country Name']==country]
    Indicator = ["EG.ELC.PETR.ZS","EG.ELC.NUCL.ZS","EG.ELC.NGAS.ZS",\
                 "EG.ELC.HYRO.ZS","EG.ELC.COAL.ZS"]
    year = ["2000","2005","2010","2015"]
    df.set_index('Indicator Code',inplace=True)
    df = df.loc[Indicator,year]

    df= df.transpose()

    df.plot(kind="line",figsize=(10,5))
    plt.title("Electricity production from coal sources (% of total) " \
              + country)
    plt.xlabel("Indicators")
    plt.ylabel("Electricity Production % total")
    plt.legend()
    plt.show()


def heatmap(file, country):
    # Selecting the indicators which could be the correlation to one another
    indicators = ["EG.ELC.PETR.ZS","EG.ELC.NUCL.ZS","EG.ELC.NGAS.ZS",\
                  "EG.ELC.HYRO.ZS","EG.ELC.COAL.ZS"]

    # Get the data from the World Bank dataset
    data = pd.read_csv(file, skiprows=(3))

    # Clean and format the data for the specified country and required indicators
    data = data.loc[data['Country Name'] == country]
    data = data.loc[data['Indicator Code'].isin(indicators)]
    data = data.loc[:, ["Indicator Name", "2000","2002","2004","2006","2008",\
                        "2010","2012","2014"]]

    # Drop non-numeric rows
    data = data.dropna(subset=["2000","2002","2004","2006","2008","2010",\
                               "2012","2014"], how="any", axis=0)

    # Set "Indicator Name" as index
    data.set_index("Indicator Name", inplace=True)

    # Transpose the data for plotting
    data_transposed = data.transpose()

    # Convert data to numeric (excluding the "Country Name" column)
    data_transposed = data_transposed.apply(pd.to_numeric, errors='coerce')

    # Plotting heatmap with the correlation between the mentioned indicators
    plt.figure(figsize=(10, 6))
    sns.heatmap(data_transposed.corr(), annot=True, fmt='.2f', cmap='YlGnBu')

    # Add title and axis labels
    plt.title(f'{country} Indicators Heatmap')
    plt.xlabel('Indicator')
    plt.ylabel('Year')

    # Show the plot
    plt.show()

def read_csvfile(file):
    '''
    Parameters
    ----------
    file: file is the argument passed from the main function

    Returns
    -------
    The function returns the datafrane over the years 1995, 2000, 2010,
    2015 for the countries, for the production of electricity from coal sources
    '''
    # Read the Csv File
    data = pd.read_csv(fileName,skiprows=3)
    loc = ["United States","India","China","Russian Federation"]
    year = ["1995","2000","2005","2010","2015"]
    data.set_index('Country Name',inplace=True)

    #filtering the data with the selected indicator name
    data_elec = data[data["Indicator Name"] == \
                     "Electricity production from coal sources (% of total)"]
    data_elec_ng = data[data["Indicator Name"] == \
                "Electricity production from nuclear sources (% of total)"]

    data_elec = data_elec.loc[loc,year]
    data_elec_ng = data_elec_ng.loc[loc,year]

    #transpose the file
    data_elec_t = data_elec.transpose()

    data_elec.info()
    data_elec.describe()
    data_elec_t.describe()

    return data_elec,data_elec_t,data_elec_ng

# Main Function

fileName = "C:\\Users\\saikr\\Downloads\\API_19_DS2_en_csv_v2_6183479.csv"

df,df_t,data_ng = read_csvfile(fileName)

barchart(df,data_ng)
linechart(fileName,"India")
linechart(fileName,"United States")

heatmap(fileName,'India')
heatmap(fileName,'United States')
