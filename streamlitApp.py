# Import Streamlit for building the web-based user interface
import streamlit as st
# Import requests for making HTTP requests to the FastAPI backend
import requests

# Set the title of the Streamlit app to "Chatbot Interface"
st.title("Chatbot Interface")

# Create a text input field for the user to enter their query
query = st.text_input("Enter your query:")

# Create a button labeled "Send" that triggers query submission
if st.button("Send"):
    # Check if the query input is not empty
    if query:
        # Try to send the query to the FastAPI backend
        try:
            # Send a POST request to the /api/chat endpoint on port 8001
            response = requests.post("http://127.0.0.1:8001/api/chat", json={"query": query}, timeout=30)
            # Raise an exception if the HTTP request fails (e.g., 4xx, 5xx status)
            response.raise_for_status()
            # Display the chatbot's response from the JSON payload
            st.write(response.json()["response"])
        # Catch HTTP-related errors
        except requests.RequestException as e:
            # Display a detailed error message
            st.error(f"Failed to connect to the backend: {str(e)}. Please ensure the FastAPI server is running on http://127.0.0.1:8001/api/chat.")
    # Handle case where the query input is empty
    else:
        st.warning("Please enter a query.")