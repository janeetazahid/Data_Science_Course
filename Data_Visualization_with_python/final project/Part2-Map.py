import matplotlib as mp1
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 
import folium
df_incidents=pd.read_csv(r"Police_Department_Incidents.csv")
df_incidents.drop(['Category', 'DayOfWeek', 'Date', 'Resolution','Time', 'Address','Location','PdId','Descript','X','Y'], axis=1, inplace=True)
df_incidents.rename(columns={'IncidntNum':'Count','PdDistrict':'Neighbourhood'},inplace=True)
df_areas=df_incidents.groupby('Neighbourhood', axis=0).count()
df_areas.reset_index(inplace=True)
sanFan_geo=r'san-francisco.geojson'
SanFan_Map=folium.Map(location=[37.7749, -122.4194],zoom_start=12)
SanFan_Map.choropleth(
    geo_data=sanFan_geo,
    data=df_areas,
    columns=['Neighbourhood','Count'],
    key_on='feature.properties.DISTRICT',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Crime Rate in San Francisco'
)
SanFan_Map
