import streamlit as st

st.set_page_config(
    page_title="ResearchMind",
    page_icon="📚",
    layout="wide"
)

st.title("📚 ResearchMind")
st.subheader("AI-Powered Research Paper Assistant")

st.markdown("""
Welcome to ResearchMind.

Features:
- 📄 Upload Research Papers
- 💬 Chat with Papers
- 📝 Generate Summaries
- 🔍 Semantic Search
- ⚖️ Compare Papers
- 🎯 Find Research Gaps
- 📤 Export Results
""")

st.info("Use the sidebar to navigate between modules.")