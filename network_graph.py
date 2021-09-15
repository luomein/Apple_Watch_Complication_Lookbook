from pyvis import network as net
import streamlit as st
from stvis import pv_static
import pandas as pd

import datapane as dp

WatchFace = pd.read_csv('WatchFace.csv')

merged_df = pd.merge(WatchFace.loc[:,["WatchFace_Name" , "ComplicationFamily_Name"]] , WatchFace.loc[:,["WatchFace_Name" , "ComplicationFamily_Name"]]
                  ,on='WatchFace_Name',how='inner', suffixes=('_1', '_2'))
merged_df['connection_counts'] = merged_df.groupby('WatchFace_Name')['ComplicationFamily_Name_1'].transform('count')
merged_df = merged_df[(merged_df['ComplicationFamily_Name_1'] < merged_df['ComplicationFamily_Name_2']) | (merged_df['connection_counts'] == 1) ]
#st.dataframe(merged_df)
##df.groupby(['col1', 'col2']).size().reset_index(name='counts')
merged_df_grouped = merged_df.groupby(['ComplicationFamily_Name_1','ComplicationFamily_Name_2']).size().reset_index(name='counts')

g=net.Network(width="450px" , height="350px" ,  heading='')

for cf in WatchFace.ComplicationFamily_Name.dropna().unique() :
  g.add_node(cf , value= 3 , color = '#00221eaa')

for idx , row in merged_df_grouped.iterrows():
    filtered_watch_face = merged_df.loc[(merged_df.ComplicationFamily_Name_1 == row['ComplicationFamily_Name_1']) & (merged_df.ComplicationFamily_Name_2 == row['ComplicationFamily_Name_2'])  , 'WatchFace_Name' ].values.tolist()
    g.add_edge(row['ComplicationFamily_Name_1'], row['ComplicationFamily_Name_2']
    , color = '#22001eaa'
    , title = ','.join(filtered_watch_face) , value = row['counts'])


#g.add_edge(1,2)
#g.add_edge(2,3)
g.force_atlas_2based()
#g.barnes_hut()
g.show("network_graph.html")
#report.append(dp.HTML(read_html('list_of_nodes.html'), name='list_of_nodes'))

def read_html(name: str):
    import codecs
    f = codecs.open(name, 'r')
    return f.read()

dp.Report(
  dp.HTML(read_html('network_graph.html'), name='network_graph')
    #dp.Plot(plot1),
    #dp.DataTable(source)
).upload(name="network_graph")
#g.barnes_hut()
pv_static(g)
