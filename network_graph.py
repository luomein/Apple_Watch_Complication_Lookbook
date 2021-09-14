from pyvis import network as net
import streamlit as st
from stvis import pv_static
import pandas as pd

WatchFace = pd.read_csv('WatchFace.csv')

merged_df = pd.merge(WatchFace.loc[:,["WatchFace_Name" , "ComplicationFamily_Name"]] , WatchFace.loc[:,["WatchFace_Name" , "ComplicationFamily_Name"]]
                  ,on='WatchFace_Name',how='inner', suffixes=('_1', '_2'))
merged_df = merged_df[merged_df.ComplicationFamily_Name_1 < merged_df.ComplicationFamily_Name_2]
##df.groupby(['col1', 'col2']).size().reset_index(name='counts')
merged_df_grouped = merged_df.groupby(['ComplicationFamily_Name_1','ComplicationFamily_Name_2']).size().reset_index(name='counts')

g=net.Network(width = "800px" , height="800px" , heading='')

for cf in WatchFace.ComplicationFamily_Name.dropna().unique() :
  g.add_node(cf)

for idx , row in merged_df_grouped.iterrows():
    filtered_watch_face = merged_df.loc[(merged_df.ComplicationFamily_Name_1 == row['ComplicationFamily_Name_1']) & (merged_df.ComplicationFamily_Name_2 == row['ComplicationFamily_Name_2'])  , 'WatchFace_Name' ].values.tolist()
    g.add_edge(row['ComplicationFamily_Name_1'], row['ComplicationFamily_Name_2']
    , title = ','.join(filtered_watch_face) , value = row['counts'])

#g.add_edge(1,2)
#g.add_edge(2,3)
g.force_atlas_2based(overlap=1)
#g.barnes_hut()
pv_static(g)
