import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="MindSparkAI", page_icon="💡")
st.title("💡 MindSparkAI: Your Learning Copilot")

# Configure API Key via sidebar
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    
    topic = st.text_input("What topic do you want to learn today?")
    mode = st.selectbox("Choose Mode", ["Explain Simply", "Generate Quiz", "Key Takeaways"])

    if st.button("Generate"):
        if topic:
            model = genai.GenerativeModel("gemini-1.5-flash")
            prompt = f"Act as an AI tutor. Topic: {topic}. Task: {mode}."
            
            with st.spinner("Thinking..."):
                response = model.generate_content(prompt)
                st.write(response.text)
        else:
            st.warning("Please enter a topic.")
else:
    st.info("Please enter your Gemini API Key in the sidebar to start.")
