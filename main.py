import streamlit as st
from views import pages



list_of_pages = [
    "Moira Queendom",
    "Who is MOIRA?",
    "Moira in the PH Music Scene",
    "How to Conquer the US?",
    "Moira's Music",
    "Recommender Engine",
    "US Music Market",
    "Collaborations",
    "Conclusion",
    "Spotify Playlist"
]

st.sidebar.title(':crown: MOIRA Queendom')
st.sidebar.markdown("Team One-Derers")
st.sidebar.markdown("Eskwelabs: Data Science Fellowship Cohort 11")
selection = st.sidebar.radio("Go to: ", list_of_pages)

if selection == "Moira Queendom":
    pages.Moira_Queendom()

elif selection == "Who is MOIRA?":
    pages.Artist_Overview()

elif selection == "Moira in the PH Music Scene":
    pages.Moira_PH()

elif selection == "How to Conquer the US?":
    pages.Conquer_US()
    
elif selection == "Moira's Music":
    pages.Moira_music()

elif selection == "Recommender Engine":
    pages.recom_engine()

elif selection == "US Music Market":
    pages.us_market()

elif selection == "Collaborations":
    pages.collab()

elif selection == "Conclusion":
    pages.moira_us()

elif selection == "Spotify Playlist":
    pages.sp_playlist()
