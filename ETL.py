# import libraries 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Extract Process
df_conf_glo = pd.read_csv("csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")
df_conf_us = pd.read_csv("csse_covid_19_time_series/time_series_covid19_confirmed_us.csv")
df_death_glo = pd.read_csv("csse_covid_19_time_series/time_series_covid19_deaths_global.csv")
df_death_us = pd.read_csv("csse_covid_19_time_series/time_series_covid19_deaths_US.csv")
df_recov_glo = pd.read_csv("csse_covid_19_time_series/time_series_covid19_recovered_global.csv")


# Transform the data using padas melt
df_conf_glo_melt = pd.melt(df_conf_glo, id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], 
                           var_name='date', value_name='numcases')
df_conf_us_melt = pd.melt(df_conf_us, id_vars=['UID', 'iso2', 'iso3', 'code3', 'FIPS', 'Admin2', 'Province_State',
       'Country_Region', 'Lat', 'Long_', 'Combined_Key'], var_name='date', value_name='numcases')
df_death_glo_melt = pd.melt(df_death_glo, id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'],
                            var_name='date', value_name='numdeaths')
df_death_us_melt = pd.melt(df_death_us,  id_vars=['UID', 'iso2', 'iso3', 'code3', 'FIPS', 'Admin2', 'Province_State', 'Country_Region', 'Lat', 'Long_', 'Combined_Key'], var_name='date', value_name='numdeaths')
df_recov_glo_melt = pd.melt(df_recov_glo, id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], 
                           var_name='date', value_name='numrecovered')


# Remove irrelevant columns and rename columns
df_conf_us_melt  = df_conf_us_melt[['Country_Region', 'Province_State', 'Admin2', 'date', 'numcases']]
df_conf_us_melt.columns = ['Country/Region', 'Province/State', 'City', 'date', 'numcases']
df_death_us_melt = df_death_us_melt[['Country_Region', 'Province_State', 'Admin2', 'date', 'numdeaths']]
df_death_us_melt.columns = ['Country/Region', 'Province/State', 'City', 'date', 'numdeaths']


# Fill N/As
df_conf_glo_melt.fillna('', inplace=True)
df_conf_glo_melt.fillna('', inplace=True)
df_death_glo_melt.fillna('', inplace=True)
df_death_us_melt.fillna('', inplace=True)

# Load - Export transformed data as CSV
df_conf_glo_melt.to_csv("transformed-data/transformed-global-confirmed-cases.csv", index=False)
df_conf_us_melt.to_csv("transformed-data/transformed-us-confirmed-cases.csv", index=False)
df_death_glo_melt.to_csv("transformed-data/transformed-global-covid19-deaths.csv", index=False)
df_death_us_melt.to_csv("transformed-data/transformed-us-covid19-deaths.csv", index=False)
df_recov_glo_melt.to_csv("transformed-data/transformed-global-covid19-recovered.csv", index=False)