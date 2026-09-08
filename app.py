import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="MindSparkAI", page_icon="💡")
st.title("💡 MindSparkAI: Your Learning Copilot")

# 1. Automatically grab API key from Streamlit Secrets
api_key = st.secrets.get("GEMINI_API_KEY", "")

# 2. Fallback to sidebar input if secret is missing
if not api_key:
    api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

topic = st.text_input("What topic do you want to learn today?")
mode = st.selectbox("Choose Mode", ["Explain Simply", "Generate Quiz", "Key Takeaways"])

if st.button("Generate"):
    if not api_key:
        st.error("Please configure GEMINI_API_KEY in Streamlit Secrets or enter it in the sidebar.")
    elif not topic:
        st.warning("Please enter a topic.")
    else:
        try:
            genai.configure(api_key=api_key.strip())
            model = genai.GenerativeModel("gemini-3.6-flash")
            prompt = f"Act as an AI tutor. Topic: {topic}. Task: {mode}."
            
            with st.spinner("Thinking..."):
                response = model.generate_content(prompt)
                st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
