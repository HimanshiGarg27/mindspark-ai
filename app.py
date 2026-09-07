import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="MindSparkAI", page_icon="💡")
st.title("💡 MindSparkAI: Your Learning Copilot")

# Sidebar for API key input
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

topic = st.text_input("What topic do you want to learn today?")
mode = st.selectbox("Choose Mode", ["Explain Simply", "Generate Quiz", "Key Takeaways"])

if st.button("Generate"):
    if not api_key:
        st.error("Please enter a valid Gemini API Key in the sidebar.")
    elif not topic:
        st.warning("Please enter a topic.")
    else:
        try:
            genai.configure(api_key=api_key.strip())
            model = genai.GenerativeModel("gemini-1.5-flash")
            prompt = f"Act as an AI tutor. Topic: {topic}. Task: {mode}."
            
            with st.spinner("Thinking..."):
                response = model.generate_content(prompt)
                st.write(response.text)
        except Exception as e:
            st.error(f"Error generating content: {e}")
