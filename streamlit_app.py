import streamlit as st
import requests

st.set_page_config(page_title="Job Finder Chatbot", layout="centered")
st.title("🧠 Conversational Job Finder")

query = st.text_input("Enter your job query", placeholder="e.g., AI Engineer in San Francisco with salary more than 150K")

if st.button("Search Jobs") and query:
    try:
        with st.spinner("Searching jobs..."):
            response = requests.get("https://chatbot-jobfinder-1.onrender.com/search_jobs", params={"query": query})
            data = response.json()

            st.subheader("🔍 Parsed Query")
            st.json(data["parsed"])

            st.subheader("🧰 Careerjet Jobs")
            for job in data["careerjet_jobs"]:
                st.markdown(f"**{job['title']}**  \n📍 {job['location']}  \n🔗 [View Job]({job['url']})")
                st.markdown("---")

            st.subheader("🌐 Jooble Jobs")
            for job in data["jooble_jobs"]:
                st.markdown(f"**{job['title']}**  \n📍 {job['location']}  \n🔗 [View Job]({job['url']})")
                st.markdown("---")

    except Exception as e:
        st.error(f"Error: {e}")
