#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
import pandas as pd
import numpy as np



st.set_page_config(layout="wide")
st.markdown('''
<style>
        div.stSelectbox > label {
        font-size: 20px;font-family: "IBM Plex Sans", sans-serif;font-weight: 600;
        }
        div.stMarkdown > div > p > strong {
        word-wrap : break-word
        }
        div.streamlit-expanderHeader {
        word-wrap : break-word
        }
 </style>
''', unsafe_allow_html=True)
### background-color: #00cc00;
###### div.stButton > button:first-child {{ border: 5px solid {primaryColor}; border-radius:20px 20px 20px 20px; }}

def get_Complication(df , family) :
    return df.loc[df['ComplicationFamily_Name'] == family ].reset_index()

def get_ComplicationFamily(df , family ) :
       return df.loc[df['ComplicationFamily_Name'] == family ].reset_index().iloc[0]

def get_WatchFace(df , family, watchface = '') :
  #st.write(type(watchface))
  if watchface == '' :
    return df.loc[df['ComplicationFamily_Name'] == family ].reset_index()
  else :
    return df.loc[(df['ComplicationFamily_Name'] == family) & (df['WatchFace_Name'] == watchface)  ].reset_index()

ComplicationTemplate = pd.read_csv('ComplicationTemplate.csv')
ComplicationTemplate.rename(columns={"Name":"ComplicationTemplate_Name" , "Name.1":"ComplicationFamily_Name"} , inplace=True)
ComplicationTemplate['ComplicationTemplate_Picture_URL'].fillna('', inplace = True)

##CLKComplicationFamily,ComplicationFamily_Name,ComplicationFamily_Picture_URL,ComplicationFamily_URL,WatchFace_Name,WatchFace_Picture_URL,
##ComplicationFamily_Group,ComplicationFamily_Group_URL,ComplicationFamily_Templates_Picture_URL,ComplicationFamily_Templates_URL
WatchFace = pd.read_csv('WatchFace.csv')
WatchFace.rename(columns={"Name":"ComplicationFamily_Name" , "Name.1":"WatchFace_Name"
  , "Picture_URL" : "ComplicationFamily_Picture_URL", "URL" : "ComplicationFamily_URL" , "Picture_URL.1" : "WatchFace_Picture_URL"} , inplace=True)
WatchFace['ComplicationFamily_Group'].fillna('', inplace = True)
WatchFace['ComplicationFamily_Group_URL'].fillna('', inplace = True)
WatchFace['ComplicationFamily_Templates_Picture_URL'].fillna('', inplace = True)
WatchFace['ComplicationFamily_Templates_URL'].fillna('', inplace = True)
#WatchFace['Picture_URL'].fillna('', inplace = True)
#all_checked = st.sidebar.checkbox('(All)' , value = True)
#st.sidebar.header('WatchFace')
st.markdown('''
<style>
    section.main div.stButton > button:first-child {
                    font-size:30px;border: 0px;
                    position: fixed;
                    top: -20px;
                    left:  50px;
                    z-index : 10000;
                    outline:none;
                    width: 50px;
                    background-color: Transparent;
                    }
 </style>
''', unsafe_allow_html=True)
home_btn = st.button("🏚")

if home_btn and 'selected_menu'   in st.session_state :
      st.session_state['selected_menu'] = ''

selected_watch_face =  st.sidebar.selectbox('WatchFace' , ('' , ) + (*(WatchFace.WatchFace_Name.unique().tolist()),)   )
#st.sidebar.write(selector_watch_face)
#st.sidebar.markdown(f"<hr>"  , unsafe_allow_html=True )

st.sidebar.header('ComplicationTemplate components')

filter = dict()
filter['View'] = st.sidebar.checkbox('View' , value = True)
filter['CLKTextProvider'] = st.sidebar.checkbox('CLKTextProvider', value = True)
filter['CLKImageProvider'] = st.sidebar.checkbox('CLKImageProvider', value = True)
filter['CLKGauageProvider'] = st.sidebar.checkbox('CLKGauageProvider', value = True)
filter['CLKComplicationRingStyle'] = st.sidebar.checkbox('CLKComplicationRingStyle', value = True)

#def save_menu_selected() :
#st.sidebar.markdown(f"<hr>"  , unsafe_allow_html=True )
st.markdown('''
<style>
        div.stButton > button:first-child {
                    font-size:20px;height:3em;width:15em;border-radius:10px 10px 10px 10px;border: 0px;
                    }
 </style>
''', unsafe_allow_html=True)
st.sidebar.header('ComplicationFamily')
side_menu = dict()
for f in sorted( ComplicationTemplate['ComplicationFamily_Name'].dropna().unique() ) :
    sub_df = get_Complication(ComplicationTemplate , f)
    filtered_watch_face = get_WatchFace(WatchFace , f , watchface = selected_watch_face)
    has_filtered_element = False
    for ele in filter :
        if filter[ele] and  sub_df['Components'].str.contains(ele).any() :
            has_filtered_element = True
            break
    if has_filtered_element and  len(filtered_watch_face) > 0  :
      side_menu[f] = st.sidebar.button(f)
      if side_menu[f] :
           st.session_state['selected_menu'] = f
    else :
      ###st.markdown("<h1 style='text-align: center; color: red;'>Some title</h1>", unsafe_allow_html=True)
      st.sidebar.markdown(f"<p style='text-align: center;'>{f}</p>", unsafe_allow_html=True)
st.sidebar.markdown(f"<br><br><br>"  , unsafe_allow_html=True )
### agree = st.checkbox('I agree')
any_selected_menu = False
for f in side_menu:
    if side_menu[f]:
        any_selected_menu = True
if not any_selected_menu and 'selected_menu'   in st.session_state and  st.session_state['selected_menu'] != '' :
    side_menu[st.session_state['selected_menu'] ] = True

column_count = 2
cols = st.columns(column_count)

#st.dataframe(data=WatchFace)
for f in side_menu :
    if side_menu[f]:
        sub_watch_face = get_WatchFace(WatchFace , f)
        st.markdown(f"# [{f}]({get_ComplicationFamily(WatchFace , f)['ComplicationFamily_URL']})"  , unsafe_allow_html=True )
        st.write(f'CLKComplicationFamily = {get_ComplicationFamily(WatchFace , f)["CLKComplicationFamily"]}')
        ##WatchFace['ComplicationFamily_Group'].fillna('', inplace = True)
        ##WatchFace['ComplicationFamily_Group_URL'].fillna('', inplace = True)
        if sub_watch_face['ComplicationFamily_Group'].unique()[0] != '' :
            st.markdown(f"Group: [{sub_watch_face['ComplicationFamily_Group'].unique()[0]}]({sub_watch_face['ComplicationFamily_Group_URL'].unique()[0]})" , unsafe_allow_html=True )

        #st.dataframe(data=sub_watch_face)
        watchface_cols = st.columns(len(sub_watch_face) + 1 )
        watchface_cols[0].image(get_ComplicationFamily(WatchFace , f)['ComplicationFamily_Picture_URL'] , use_column_width = 'auto')
        for i in range(len(sub_watch_face) ) :
            #watchface_cols[i+1].write(sub_watch_face.loc[i , 'WatchFace_Picture_URL'])
            watchface_cols[i+1].image(sub_watch_face.loc[i , 'WatchFace_Picture_URL'] , use_column_width = 'auto')
            watchface_cols[i+1].write(sub_watch_face.loc[i , 'WatchFace_Name'])
        #st.markdown(f"#[{f}]({get_ComplicationFamily(WatchFace , f)['ComplicationFamily_URL']})#"  , unsafe_allow_html=True )
        st.markdown(f"<br><br><br><br><br>"  , unsafe_allow_html=True )
        #st.header('ComplicationTemplate')
        df = get_Complication(ComplicationTemplate , f)
        df['has_filtered_element'] = False
        checked_filter = []
        for ele in filter :
            if filter[ele]  :
                checked_filter = checked_filter + [ele]
                df[ele] = df['Components'].str.contains(ele , na = False ).astype('string')
                df['has_filtered_element'] = df['has_filtered_element'] +  df['Components'].str.contains(ele , na = False ).astype('int32')

        df = df[df['has_filtered_element'] > 0 ].reset_index()
        dt_cols = st.columns([5] + [1] *  len(checked_filter)  )
        ##WatchFace['ComplicationFamily_Templates_Picture_URL'].fillna('', inplace = True)
        ##WatchFace['ComplicationFamily_Templates_URL'].fillna('', inplace = True)
        if sub_watch_face['ComplicationFamily_Templates_URL'].unique()[0] != '' :
           dt_cols[0].markdown( f"**[ComplicationTemplates]({sub_watch_face['ComplicationFamily_Templates_URL'].unique()[0]})**" , unsafe_allow_html=True)
           dt_cols[0].image(sub_watch_face['ComplicationFamily_Templates_Picture_URL'].unique()[0] , use_column_width = 'auto')
        else :
           dt_cols[0].markdown( f"**ComplicationTemplates**" , unsafe_allow_html=True)
        for ch in range(len(checked_filter)) :
            dt_cols[ch + 1 ].markdown( f"**{checked_filter[ch]}**" , unsafe_allow_html=True)
        for idx , row in df.iterrows():
           dt_cols = st.columns([5] + [1] * len(checked_filter)  )
           #dt_cols[0].write(row['ComplicationTemplate'])
           with dt_cols[0].expander(row['ComplicationTemplate_Name']) :
               #st.markdown(f"[{row['URL']}]({row['URL']})", unsafe_allow_html=True)
               st.markdown(f"<a href='{row['ComplicationTemplate_URL']}' target='_blank'><img src='{row['ComplicationTemplate_Picture_URL']}'></a>", unsafe_allow_html=True)
               #if row['Picture_URL'] != np.nan and  row['Picture_URL']!= '' :
               #        st.image(row['Picture_URL'] )
           for ch in range(len(checked_filter)) :
               if row[checked_filter[ch]] == "True" :
                 dt_cols[ch + 1 ].write('✓')
               else :
                 dt_cols[ch + 1 ].write(' ')
        #dt_cols[0].write( df[['ComplicationTemplate'] + checked_filter ].replace(['True','False'],['✓','']).to_html(escape=False , index=False)  , unsafe_allow_html=True  )
        #dt_cols[1].write('test')
        #streamlit.expander(label, expanded=False)
st.markdown('''
<style>
        table.dataframe  thead {
        vertical-align: bottom;
        }
 </style>
''', unsafe_allow_html=True)

if  ('selected_menu' not  in st.session_state ) or ('selected_menu'   in st.session_state  and st.session_state['selected_menu'] == '') :
        ##df.pivot(index='foo', columns='bar', values='baz')

        WatchFace['value'] = '✓'
        WatchFace.fillna( '' , inplace = True)
        WatchFace['WatchFace'] =  WatchFace['WatchFace_Name'] + '<br><img  width="80" src="' + WatchFace['WatchFace_Picture_URL'] + '" >'
        if selected_watch_face != '' :
            WatchFace = WatchFace[WatchFace['WatchFace_Name'] == selected_watch_face ]
        WatchFace_pivot = WatchFace.pivot(index='WatchFace', columns='ComplicationFamily_Name', values='value' )
        WatchFace_pivot.fillna( '' , inplace = True)
        WatchFace_pivot = WatchFace_pivot.T.reset_index()

        ComplicationTemplate['has_filtered_element'] = 0
        for ele in filter :
            if filter[ele]  :
                ComplicationTemplate['has_filtered_element'] = ComplicationTemplate['has_filtered_element'] +  ComplicationTemplate['Components'].str.contains(ele , na = False ).astype('int32')
        #df[df['A'].isin([3, 6])]
        WatchFace_pivot = WatchFace_pivot[WatchFace_pivot['ComplicationFamily_Name'].isin(ComplicationTemplate.loc[ ComplicationTemplate['has_filtered_element'] > 0 , 'ComplicationFamily_Name'].dropna().unique().tolist()  ) ]
        WatchFace_pivot.rename(columns={"ComplicationFamily_Name":" "  } , inplace = True)
        #WatchFace_pivot.drop(columns=['WatchFace'] , inplace = True)
        #df.drop(columns=['B', 'C'])
        #WatchFace_pivot.replace('<NA>' , '' , inplace = True)
        #st.dataframe(WatchFace_pivot)
        st.title('Apple Watch Complication Lookbook')
        st.write(WatchFace_pivot.to_html(escape=False , index=False , index_names = False ) , unsafe_allow_html=True )
