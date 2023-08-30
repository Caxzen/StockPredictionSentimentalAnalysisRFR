import streamlit as st
import pickle
from streamlit_option_menu import option_menu
import pandas as pd 
import base64
    
    # sidebar for navigation
with st.sidebar:
        
    selected = option_menu('Filtering microblogging post and predicting stock price using sentiment analysis',['Stock Prediction',],
                            icons=['activity','heart','person'],
                            default_index=0)
    # Load the saved models
#stroke_model = pickle.load(open('stroke_model.sav', 'rb'))
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True)
 
        
add_bg_from_local('download.jpg')

if (selected == 'Stock Prediction'):
        
    
    #st.image("download.jpg",width=700)   


    st.title('Select a stock')
    #st.header('My header')
    stock = st.selectbox("",["TSLA","AMZN"])
    if(stock == "TSLA"):
        df = pd.DataFrame(
        [
        {"Adj Close": "160.16", "Volume": "127,015,200", "Positive": True, "Negative": False},
        {"Adj Close": "163.4", "Volume": "109,015,000", "Positive": False, "Negative": True},
        {"Adj Close": "161.83", "Volume": "120,607,259", "Positive": True, "Negative": True},
        {"Adj Close": "160.31", "Volume": "128,259,700", "Positive": False, "Negative": True},
        {"Adj Close": "160.61", "Volume": "119,728,000", "Positive": False, "Negative": True},
        {"Adj Close": "161.20", "Volume": "95,108,500", "Positive": True, "Negative": False},
        {"Adj Close": "170.06", "Volume": "107,607,259", "Positive": False, "Negative": True}
        ]
        )
    else:
        df = pd.DataFrame(
        [
        {"Adj Close": "102.57", "Volume": "149,961,200", "Positive": False, "Negative": True},
        {"Adj Close": "104.72", "Volume": "130,565,000", "Positive": False, "Negative": True},
        {"Adj Close": "109.82", "Volume": "74,728,100", "Positive": True, "Negative": False},
        {"Adj Close": "103.45", "Volume": "73,469,400", "Positive": False, "Negative": True},
        {"Adj Close": "103.11", "Volume": "65,051,900", "Positive": False, "Negative": True},
        {"Adj Close": "104.20", "Volume": "45,345,500", "Positive": True, "Negative": False},
        {"Adj Close": "105.66", "Volume": "56,912,900", "Positive": True, "Negative": False}
        ]
        )
    
    
    edited_df = st.experimental_data_editor(df,width=800,height=280)
    # getting the input data from the user
    
    
  
    
  
    st_diagnosis = ''
    info = ''
    st_prediction = ''
    
    # creating a button for Prediction
    
    if st.button('Predict Trend'):
        if stock=="TSLA":
            st_diagnosis = "Increase"
        else:
            st_diagnosis = "Decrease"

        

        
    st.success(st_diagnosis)
    
    if (info != ''):
        st.info(info)




