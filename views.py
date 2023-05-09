import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import data
import plotly.express as px

# Load the data
df = data.ProcessData.load_recom_pool()


# Setting general format to the graphs
#sns.set_theme(style="white", font="sans-serif")

class pages:
    #Page1 - Overview
    def Moira_Queendom():
        # Write the title and the subheader
        st.image('Slides/1.png')


    def Artist_Overview():
        # Write the title
        st.title("Whos is Moira?")
        st.subheader("")
        st.image('Slides/2.png')
        st.subheader(" ")
        st.image('Slides/3.png')
        st.subheader(" ")
        st.image('Slides/4.png ')


    def Moira_PH():
        st.title("Moira in PH Music Scene")
        st.subheader("")

        tab_artist, tab_solo = st.tabs(["Top PH Artist", "Top PH Female Solo Artist"])

        with tab_artist:
            st.subheader("Moira's Stream Compared to Top PH Artists")
            st.markdown("")
            st.image('Slides/5.png')
        
        with tab_solo:
            st.subheader("Moira's Stream Compared to Top PH Female Artists")
            st.markdown("")
            st.image('Slides/6.png')

    def Conquer_US():
        # Write the title
        st.title("Conquering US")
        st.subheader("chuchuchu")
        st.image('Slides/7.png')

    def Moira_music():
        # Write the title
        st.title("Moira's Music")
        st.subheader("")
        
        tab_moira, tab_acoustic = st.tabs(["Moira's Music Features", "US Acoustic Genre"])

        with tab_moira:
            st.subheader("Moira's Music Features")
            st.markdown("")
            st.image('Slides/8.png')
        
        with tab_acoustic:
            st.subheader("Moira's Music Features compared to US Acoustic Genre")
            st.markdown("")
            st.image('Slides/9.png')
    
    def recom_engine():
        st.title("Pipeline and ML Engine")
        st.subheader("Explain Methodology")
        st.image('Slides/11.png')

        #show recomm_pool
        st.subheader("Recommendation Pool")
        expander = st.expander("Show Recommender Pool")
        expander.dataframe(df)

    def us_market():
        st.title("US Music Market")
        st.subheader("")

        tab_us_artist, tab_us_genre, tab_rnb, tab_us_release = st.tabs(["Similar Artist", "US Top Genre", "Moira and R&B", "US Top Tracks Release"])

        with tab_us_artist:
            st.subheader("Artist w/ Similar Music Features to Moira")
            st.markdown("")
            st.image('Slides/12.png')
        
        with tab_us_genre:
            st.subheader("Popular US Genres")
            st.markdown("")
            st.image('Slides/13.png')

        with tab_rnb:
            st.subheader("Moira and R&B")
            st.markdown("")
            st.image('Slides/15.png')

        with tab_us_release:
            st.subheader("US Top Tracks Release")
            st.markdown("")
            st.image('Slides/17.png')
    
    def collab():
        st.title("Collaboration")
        st.subheader("")

        tab_lana, tab_sam, tab_release = st.tabs(["Lana Del Rey", "Sam Smith", "Release Dates"])

        with tab_lana:
            st.subheader("Moira and Lana")
            st.markdown("")
            st.image('Slides/18.png')

        with tab_sam:
            st.subheader("Moira and Sam")
            st.markdown("")
            st.image('Slides/19.png')
        
        with tab_release:
            st.subheader("Release Dates of Lana Del Rey and Sam Smith")
            st.markdown("")
            st.image('Slides/20.png')

    def moira_us():
        st.title("How can MOIRA Conquer US?")
        st.subheader("")
        st.image('Slides/21.png')

    def sp_playlist():
        st.title("Moira Recommender Playlist")
        st.components.v1.html('<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/65zxFtHsH7juLMTepFiD9x?utm_source=generator" width="100%" height="100%" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>')



                        





            
            