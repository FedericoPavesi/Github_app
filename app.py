import streamlit as st
import ee
from geemap import foliumap

    

Map = foliumap.Map()


lazio_TCI = ee.Image('users/federicopavesiwork/Lazio_2018_TCI')
mlp11 = ee.Image('users/federicopavesiwork/MLP_1x1')
mlp33 = ee.Image('users/federicopavesiwork/MLP_3x3')
rf11 = ee.Image('users/federicopavesiwork/RF_1x1')
rf33 = ee.Image('users/federicopavesiwork/RF_3x3')

viz_params = {'min' : 0, 
              'max' : 8,
             'palette' : ['#000000', '#ff0101', '#ffff01', '#336601', '#ff8001',
                         '#01ff01', '#808080', '#0101ff', '#99ffff']}

rgb_params = {'min' : 1, 'max' : 255}

color_dict = {'Artificial Land' : '#ff0101',
             'Cropland' : '#ffff01',
             'Woodland' : '#336601',
             'Shrubland' : '#ff8001',
             'Greenland' : '#01ff01',
             'Bareland' : '#808080',
             'Water' : '#0101ff',
             'Wetlands' : '#99ffff'}

Map.addLayer(lazio_TCI, rgb_params, name = 'Lazio TCI')
Map.addLayer(mlp11, viz_params, name = 'MLP 1x1', shown = False)
Map.addLayer(mlp33, viz_params, name = 'MLP 3x3', shown = False)
Map.addLayer(rf11, viz_params, name = 'RF 1x1', shown = False)
Map.addLayer(rf33, viz_params, name = 'RF 3x3', shown = False)
Map.add_legend(legend_title="NLCD Land Cover Classification", legend_dict=color_dict)


Map.to_streamlit()