import streamlit as st
import requests

st.set_page_config(page_title="Career Guidance Bot", page_icon="🎓")
st.title("🎓 Career Guidance Chatbot")
st.markdown("Ask me about different careers like *doctor*, *gaming*, *science*, *law*, *arts*, and more!")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("You:", key="user_input")

if user_input:
    st.session_state.messages.append(("user", user_input))

    try:
        response = requests.post(
            "https://de74-27-59-61-58.ngrok-free.app/webhooks/rest/webhook",  # Use your ngrok public URL here
            json={"sender": "user", "message": user_input}
        )
        bot_response = response.json()[0].get("text", "Sorry, I didn’t get that.")
    except Exception as e:
        bot_response = f"Error: {e}"

    st.session_state.messages.append(("bot", bot_response))

# Show the chat
for role, message in st.session_state.messages:
    if role == "user":
        st.markdown(f"**You:** {message}")
    else:
        st.markdown(f"**Bot:** {message}")
