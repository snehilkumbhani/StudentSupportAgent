import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agent.support_agent import query_agent
from agent.tools import load_json

st.set_page_config(page_title="Student Support Agent", page_icon="🎓")

st.title("🎓 Student Support Assistant")
st.markdown("Ask any question about your course below.")

question = st.text_input("Enter your question")

if st.button("Submit") and question:
    with st.spinner("Getting answer..."):
        course_info = load_json("data/course_info.json")
        answer = query_agent(question, course_info)
        st.success(answer)
