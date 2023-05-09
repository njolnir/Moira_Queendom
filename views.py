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
        st.write("""<p style="font-size:20px; color:#8A3324;">
            Whether you are feeling happy, sad or somewhere in between, Moira Dela Torre's music has the
            power to hit you right in the feels. Here, you’ll get an exclusive backstage pass to the world 
            of one of the most talented and beloved singer-songwriters in the Philippines. From her heart-wrenching 
            ballads to her upbeat hits, Moira’s music has captured the hearts of fans all over the world. Get ready as 
            we explore her queendom journey towards conquering the US music scene.
        </p>""", unsafe_allow_html=True)


    def Artist_Overview():
        # Write the title
        st.title("Who is Moira?")
        st.write("""<p style="font-size:24px; color:#8A3324;">
            The journey to becoming a multi-platinum recording artist.
        </p>""", unsafe_allow_html=True)
        st.subheader(" ")
        st.image('Slides/2.png')
        st.markdown("""
            **Moira Dela Torre** first made her TV appearance joining The Voice Philippines in 2013 and made it all the way to the semi-finals. \n
            Fast forward a few years, Moira had become a household name in the Philippines. Her emotional ballads
            like **Malaya** and catchy pop tunes like **Titibo-Tibo** had won the hearts of audiences by selling out a two-day concert.
            The critically-acclaimed singer also gained awards from **Himig Handog** twice, **PMPC Music Awards for Album and Pop
            Artist of the Year** and a lot more. In 2019, she even became a judge in Idol Philippines alongside big names like
            Regine Velasquez, Vice Ganda and James Reid.
        """)
        st.subheader(" ")
        st.image('Slides/3.png')
        st.markdown("""
            Moira also collaborated with some of the biggest names in the industry like **Ben&Ben**, **I Belong to the Zoo** and **Daniel Padilla**. \n
            Back in 2021, the singer songwriter has already experienced working with foreign artists like **Maximillian** and **Pink Sweats**.\
            These collaborations can be stepping stones for her future in the US music industry. \n
            After a year, she signed with Republic Records which has future plans of bringing Filipino Artists in the US.
            The record label is under Universal Music Group (UMG) which houses the likes of Ariana Grande, Taylor Swift and The Weeknd.\n
            This year, Moira is scheduled to go on tour abroad.
        """)
        st.subheader(" ")
        st.image('Slides/4.png')
        st.markdown("""
            Moira has a strong presence in social media as noted by the high number of followers, and high following & monthly
            listeners in streaming apps. As of writing, she has 6.3M followers on Facebook, 4.4M on Instagram,
            and around **4.7M monthly listeners on Spotify**.
        """)


    def Moira_PH():
        st.title("Moira in the PH Music Scene")
        st.subheader("")

        tab_artist, tab_solo = st.tabs(["Top PH Artists", "Top PH Female Solo Artists"])

        with tab_artist:
            st.subheader("Moira's Streams Compared to Top PH Artists")
            st.image('Slides/5.png')
            st.markdown("""
                The line chart above shows the top streamed artists in the Philippines year-on-year.
                Reaching half a billion streams in 2023, Moira is among the top streamed artists in the
                Philippines alongside Ben&Ben and December Avenue.
            """)
        
        with tab_solo:
            st.subheader("Moira's Stream Compared to Top PH Female Artists")
            st.image('Slides/6.png')
            st.markdown("""
                Moira also dominates the streams among top female soloists in the Philippines.
                Among the top female solo artists in the country like KZ, Julia Anne and Yeng, Moira has gained better traction over the past years.
            """)

    def Conquer_US():
        # Write the title
        st.title("How to Conquer the US?")
        st.markdown("""
                    From the previous pages, Moira has already conquered the PH music scene and has collaborated with foreign artists as well.
                    Now, in the next pages, we will walk you through strategies on how she can conquer the US market through machine learning.
                    """)
        st.image('Slides/7.png')


    def Moira_music():
        # Write the title
        st.title("Moira's Music")
        st.subheader("")
        
        tab_moira, tab_acoustic = st.tabs(["Moira's Music Features", "US Acoustic Genre"])

        with tab_moira:
            st.subheader("Moira's Music Features")
            st.image('Slides/8.png')
            st.markdown("""
                Let us take a look at the histograms of her tracks’ audio features. Moira’s songs can be distinctly classified with the following features:
                - Acousticness is the measure of how much a piece of music or recording sounds like it was performed on acoustic instruments
                - Valence is the positive or negative mood a music conveys, and;
                - Instrumentalness is a measure of how much a song or recording predominantly contains instrumental sounds

            """)
        
        with tab_acoustic:
            st.subheader("Moira's Music Features compared to US Acoustic Genre")
            st.image('Slides/9.png')
            st.markdown("""
                Plotting the features of her tracks over most charting acoustic songs in the US,
                we can see that they have several similarities especially with liveness, energy, speechiness, valence, acousticness and loudness.
            """)
    
    def recom_engine():
        st.title("Pipeline and ML Engine")
        st.image('Slides/11.png')
        st.markdown("""
        The machine learning pipeline has three parts. \n
        A multi-classification model is built which predicts the genre of a track. From the tracks obtained from US playlists per genre,
        the data was cleaned up via outlier detection, scaling, and genre label encoding before using the data for model training.\n
        After training various multi-classification models, Random Forest emerged as the best model based on accuracy, with a score of 60.25%.
        The model was used to predict the genres of top songs in the US.\n
        The Recommender Engine was built by comparing Moira’s songs with tracks from charting songs in the US. US tracks having the most
        similarity with Moira in terms of audio features were chosen and considered as recommended tracks to listen to.
        """)

        #show recomm_pool
        st.subheader("Recommendation Pool")
        st.write("Click below to show recommended tracks")
        expander = st.expander("Show Recommender Pool")
        expander.dataframe(df)

    def us_market():
        st.title("US Music Market")
        st.subheader("")

        tab_us_artist, tab_us_genre, tab_rnb, tab_us_release = st.tabs(["Similar Artist", "US Top Genre", "Moira and R&B", "US Top Tracks Release"])

        with tab_us_artist:
            st.subheader("Artists with Similar Music Features with Moira")
            st.markdown("""
            Based on the recommender pool (built from US playlists), Olivia Rodrigo, Adele, Lana Del Rey and Sam Smith are
            among the top artists (see audience traction presented in the image) with most similar audio features as Moira.\n
            Moira could collaborate with these artists to serve as her initial exposure in the US. Since she has similar audio
            features as them, it is also a chance for her to boost her strengths musically.
            """)
            st.image('Slides/12.png')
        
        with tab_us_genre:
            st.subheader("Popular US Genres")
            st.markdown("""
            From the US top charts, hip-hop, pop, and r&b are the most popular genres (in terms of streams) in the US.\n
            Moira could collaborate with artists popular in this genre or try and venture into any of these genres.
            """)
            st.image('Slides/13.png')

        with tab_rnb:
            st.subheader("Moira and R&B")
            st.markdown("""
            Among the popular genres in the US mentioned in the previous slide, Moira has most similar features with R&B
            as shown by the audio features graph namely key, speechiness, and liveness. For R&B, HER and Charlie Puth
            are among the top artists with similar audio features as Moira hence, collaborating with them could also be an option.
            """)
            st.image('Slides/15.png')

        with tab_us_release:
            st.subheader("US Top Tracks Release")
            st.markdown("""
            This chart shows the streams of tracks based on their release date. March, May, and October are the top months with the
            highest frequency of releases. And most of these albums are from well-known artists. As a debut strategy, Moira should 
            avoid releasing during the said months.
            """)
            st.image('Slides/17.png')
    
    def collab():
        st.title("Collaborations")
        st.subheader("")

        tab_lana, tab_sam, tab_release = st.tabs(["Lana Del Rey", "Sam Smith", "Release Dates"])

        with tab_lana:
            st.subheader("Moira and Lana")
            st.markdown("""
            A collaboration with Lana Del Rey, who shares some similar audio features with Moira Dela Torre can help her conquer the US music market.\n
            By leveraging Lana Del Rey's fan base, Moira can expand her reach and introduce her unique sound to a wider audience, enhancing her chances of success.\n
            Additionally, Lana had several collaborations with not-so well-known artists in the US before.
            """)
            st.image('Slides/18.png')

        with tab_sam:
            st.subheader("Moira and Sam")
            st.markdown("""
            Another potential collaboration opportunity is with Sam Smith. Combining their emotional music styles can solidify Moira's presence in the US Music Market.\n
            Moreover, Sam Smith has a long list of collaborations over the past year including one asian artist, RM of BTS.
            """)
            st.image('Slides/19.png')
        
        with tab_release:
            st.subheader("Release Dates of Lana Del Rey and Sam Smith")
            st.markdown("""
            Shown are the historical release dates of songs and latest albums of Lana Del Rey and Sam Smith in 2022.\n
            While collaborating with these artists is a beneficial move, it is important for Moira to plan the release of her tracks.
            Releasing her songs or albums simultaneously with her collaborating artist could potentially hurt her chances and create competition.
            """)
            st.image('Slides/20.png')

    def moira_us():
        st.title("How can MOIRA Conquer US?")
        st.subheader("")
        st.markdown("""
        Below are several strategic approaches based on the results of the models utilized:
        """)
        st.image('Slides/21.png')
        st.markdown("""
        The management can look for artists who have similar audio characteristics and collaborate with them.
        She can tap into their existing fan base and expand her reach in the US market.
        This will allow her to introduce her unique sound to a wider audience.\n
        Considering also artists who are popular in the most streamed genres can help her align with the current music trends,
        gain exposure to a larger audience and creep into the US music scene.\n
        Timing also plays a crucial role in maximizing visibility and impact. For Moira's music to gain presence and traction,
        a strategic approach would involve releasing her music during periods when fewer artists  in the USA and artists
        (with similar audio features) are not promoting nor releasing their own work. By capitalizing on these  moments,
        there is less competition, which is definitely more advantageous for her. This allows her tracks to stand out and
        capture the attention of potential listeners more effectively.
        """)

    def sp_playlist():
        st.title("Moira Recommender Playlist")
        st.write("""<p style="font-size:20px; color:#8A3324;">
            Have a listen at the US tracks generated by our Recommender Engine with Moira's song 'Tagpuan' as the seed track!
        </p>""", unsafe_allow_html=True)        
        embed_code = '<iframe src="https://open.spotify.com/embed/playlist/3HEz1cLUsSndXTGQ0h5WN8?utm_source=generator" width="100%" height="640" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>'
        st.write(embed_code, unsafe_allow_html=True)



                        





            
            
