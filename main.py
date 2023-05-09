import streamlit as st
from views import pages



list_of_pages = [
    "Moira Queendom",
    "Who is MOIRA?",
    "Moira in PH Music Scene",
    "Conquering US",
    "Moira's Music",
    "Recommender Engine",
    "US Market",
    "Collaborations",
    "How can MOIRA Conquer US?",
    "Spotify Playlist"
    
]

st.sidebar.title(':crown: MOIRA Queendom')
st.sidebar.markdown("Team One-Derers | DSFC11")
selection = st.sidebar.radio("Go to: ", list_of_pages)

if selection == "Moira Queendom":
    pages.Moira_Queendom()

elif selection == "Who is MOIRA?":
    pages.Artist_Overview()

elif selection == "Moira in PH Music Scene":
    pages.Moira_PH()

elif selection == "Conquering US":
    pages.Conquer_US()
    
elif selection == "Moira's Music":
    pages.Moira_music()

elif selection == "Recommender Engine":
    pages.recom_engine()

elif selection == "US Market":
    pages.us_market()

elif selection == "Collaborations":
    pages.collab()

elif selection == "How can MOIRA Conquer US?":
    pages.moira_us()

elif selection == "Spotify Playlist":
    pages.sp_playlist()
