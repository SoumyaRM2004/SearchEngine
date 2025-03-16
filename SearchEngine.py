
# import streamlit as st
# import requests
# from bs4 import BeautifulSoup
# import google.generativeai as genai  # Gemini API
# import speech_recognition as sr  # Voice Search
# import json
# import os

# # Streamlit UI
# st.set_page_config(page_title="AI Search", layout="wide")
# st.title("🔍 AI-Powered SearchEngine")

# # API Keys (Replace with your actual keys)
# GEMINI_API_KEY = "AIzaSyDJMyOJn4SGA08JHx-bRhnrSq16KShTdmE"
# SERPAPI_KEY = "2e51cef540ab0344835f29d26b699bf5e732cfd2f3241f3ba51729b64ee568cb"

# # Initialize Google Gemini API
# genai.configure(api_key=GEMINI_API_KEY)

# # Load search history file
# SEARCH_HISTORY_FILE = "search_history.json"
# if not os.path.exists(SEARCH_HISTORY_FILE):
#     with open(SEARCH_HISTORY_FILE, "w") as f:
#         json.dump([], f)

# def save_search_history(history):
#     """Save search history to file."""
#     with open(SEARCH_HISTORY_FILE, "w") as f:
#         json.dump(history, f)

# def load_search_history():
#     """Load past search queries."""
#     with open(SEARCH_HISTORY_FILE, "r") as f:
#         return json.load(f)

# def google_search(query):
#     """Fetch latest search results using SerpAPI dynamically."""
#     url = "https://serpapi.com/search"
#     params = {
#         "q": query,
#         "api_key": SERPAPI_KEY,
#         "num": 10,
#         "tbs": "qdr:d"  # Prioritize recent results
#     }
    
#     try:
#         response = requests.get(url, params=params, timeout=20)  # Increased timeout
#         response.raise_for_status()
#         return response.json().get("organic_results", []), response.json().get("images_results", [])
#     except requests.exceptions.Timeout:
#         return [], []
#     except requests.exceptions.RequestException:
#         return [], []

# def generate_ai_summary(query):
#     """Generate an AI-powered summary using Gemini API with real-time data."""
#     try:
#         search_results, _ = google_search(query)
#         context = "\n".join([res.get("title", "") + ": " + res.get("snippet", "") for res in search_results[:3]])
        
#         if not context.strip():  # Check if the context is empty
#             return "No reliable information available at the moment."

#         model = genai.GenerativeModel("gemini-1.5-flash")
#         response = model.generate_content(f"Latest update on {query}:\n{context}")
        
#         return response.text if hasattr(response, "text") else "No confirmed information yet."
#     except Exception as e:
#         return "❌ AI summary unavailable due to API limits or errors."

# def voice_search():
#     """Use microphone for voice search."""
#     recognizer = sr.Recognizer()
#     try:
#         with sr.Microphone() as source:
#             st.info("🎙 Speak now...")
#             recognizer.adjust_for_ambient_noise(source, duration=1)
#             audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
#             st.success("✅ Voice detected, processing...")
#             return recognizer.recognize_google(audio)
#     except sr.WaitTimeoutError:
#         st.warning("⏳ No speech detected, please try again.")
#     except sr.UnknownValueError:
#         st.warning("🤷 Could not understand, please speak clearly.")
#     except sr.RequestError:
#         st.error("❌ Voice recognition service is unavailable.")
#     except OSError:
#         st.error("🚫 Microphone not detected. Please check your device.")
#     return ""

# if "search_query" not in st.session_state:
#     st.session_state["search_query"] = ""
#     st.session_state["search_trigger"] = False
#     st.session_state["page"] = 1

# def trigger_search():
#     st.session_state.search_trigger = True
#     st.session_state["page"] = 1  # Reset to first page on new search

# query = st.text_input("Type your query or use voice search:", key="search_query", on_change=trigger_search)

# if st.button("🎙 Voice Search"):
#     voice_query = voice_search()
#     if voice_query:
#         st.session_state["search_query"] = voice_query
#         st.session_state["search_trigger"] = True
#         st.rerun()

# if st.session_state.search_trigger and st.session_state["search_query"].strip():
#     query = st.session_state["search_query"]
#     history = load_search_history()
#     if query not in history:
#         history.append(query)
#         save_search_history(history)
    
#     with st.spinner("✨ Fetching AI summary..."):
#         summary = generate_ai_summary(query)
#     st.subheader("📌 AI Summary")
#     st.write(summary)
#     st.write("---")

#     with st.spinner("🔎 Searching the latest web results..."):
#         results, _ = google_search(query)

#     if not results:
#         st.warning("⚠ No results found. Try a different query.")
#     else:
#         results_per_page = 5
#         total_pages = (len(results) + results_per_page - 1) // results_per_page
#         page = st.session_state["page"]
        
#         for i, result in enumerate(results[(page-1)*results_per_page: page*results_per_page], start=(page-1)*results_per_page + 1):
#             st.markdown(f"{i}. [{result.get('title', 'No Title')}]({result.get('link', '#')})")
#             st.write(result.get("snippet", "No snippet available."))
#             st.write("---")
        
#         col1, col2, col3 = st.columns([1, 2, 1])
#         with col1:
#             if page > 1:
#                 if st.button("⬅ Previous", key="prev_page"):
#                     st.session_state["page"] -= 1
#                     st.rerun()
#         with col3:
#             if page < total_pages:
#                 if st.button("Next ➡", key="next_page"):
#                     st.session_state["page"] += 1
#                     st.rerun()


# # Display and manage search history
# st.sidebar.subheader("📜 Search History")
# history = load_search_history()

# def set_search_query(past_query):
#     st.session_state["search_query"] = past_query
#     st.session_state["search_trigger"] = True
#     st.session_state["page"] = 1

# for i, past_query in enumerate(history[::-1], start=1):
#     st.sidebar.button(past_query, key=f"history_{i}", on_click=set_search_query, args=(past_query,))

# if st.sidebar.button("Clear History"):
#     save_search_history([])
#     st.sidebar.success("✅ History cleared!")
#     st.rerun()




# only text based
# import streamlit as st
# import requests
# import google.generativeai as genai  # Gemini API
# import json
# import os

# # Streamlit UI
# st.set_page_config(page_title="AI Search", layout="wide")
# st.title("🔍 AI-Powered SearchEngine")

# # API Keys (Replace with your actual keys)
# GEMINI_API_KEY = "AIzaSyDJMyOJn4SGA08JHx-bRhnrSq16KShTdmE"
# SERPAPI_KEY = "2e51cef540ab0344835f29d26b699bf5e732cfd2f3241f3ba51729b64ee568cb"

# # Initialize Google Gemini API
# genai.configure(api_key=GEMINI_API_KEY)

# # Load search history file
# SEARCH_HISTORY_FILE = "search_history.json"
# if not os.path.exists(SEARCH_HISTORY_FILE):
#     with open(SEARCH_HISTORY_FILE, "w") as f:
#         json.dump([], f)

# def save_search_history(history):
#     """Save search history to file."""
#     with open(SEARCH_HISTORY_FILE, "w") as f:
#         json.dump(history, f)

# def load_search_history():
#     """Load past search queries."""
#     with open(SEARCH_HISTORY_FILE, "r") as f:
#         return json.load(f)

# def google_search(query):
#     """Fetch latest search results using SerpAPI dynamically."""
#     url = "https://serpapi.com/search"
#     params = {
#         "q": query,
#         "api_key": SERPAPI_KEY,
#         "num": 10,
#         "tbs": "qdr:d"  # Prioritize recent results
#     }
    
#     try:
#         response = requests.get(url, params=params, timeout=20)
#         response.raise_for_status()
#         return response.json().get("organic_results", []), response.json().get("images_results", [])
#     except requests.exceptions.RequestException:
#         return [], []

# def generate_ai_summary(query):
#     """Generate an AI-powered summary using Gemini API with real-time data."""
#     try:
#         search_results, _ = google_search(query)
#         context = "\n".join([res.get("title", "") + ": " + res.get("snippet", "") for res in search_results[:3]])
        
#         if not context.strip():
#             return "No reliable information available at the moment."

#         model = genai.GenerativeModel("gemini-1.5-flash")
#         response = model.generate_content(f"Latest update on {query}:\n{context}")
        
#         return response.text if hasattr(response, "text") else "No confirmed information yet."
#     except Exception:
#         return "❌ AI summary unavailable due to API limits or errors."

# if "search_query" not in st.session_state:
#     st.session_state["search_query"] = ""
#     st.session_state["search_trigger"] = False
#     st.session_state["page"] = 1

# def trigger_search():
#     st.session_state.search_trigger = True
#     st.session_state["page"] = 1  # Reset to first page on new search

# query = st.text_input("Type your query:", key="search_query", on_change=trigger_search)

# if st.session_state.search_trigger and st.session_state["search_query"].strip():
#     query = st.session_state["search_query"]
#     history = load_search_history()
#     if query not in history:
#         history.append(query)
#         save_search_history(history)
    
#     with st.spinner("✨ Fetching AI summary..."):
#         summary = generate_ai_summary(query)
#     st.subheader("📌 AI Summary")
#     st.write(summary)
#     st.write("---")

#     with st.spinner("🔎 Searching the latest web results..."):
#         results, _ = google_search(query)

#     if not results:
#         st.warning("⚠ No results found. Try a different query.")
#     else:
#         results_per_page = 5
#         total_pages = (len(results) + results_per_page - 1) // results_per_page
#         page = st.session_state["page"]
        
#         for i, result in enumerate(results[(page-1)*results_per_page: page*results_per_page], start=(page-1)*results_per_page + 1):
#             st.markdown(f"{i}. [{result.get('title', 'No Title')}]({result.get('link', '#')})")
#             st.write(result.get("snippet", "No snippet available."))
#             st.write("---")
        
#         col1, col2, col3 = st.columns([1, 2, 1])
#         with col1:
#             if page > 1:
#                 if st.button("⬅ Previous", key="prev_page"):
#                     st.session_state["page"] -= 1
#                     st.rerun()
#         with col3:
#             if page < total_pages:
#                 if st.button("Next ➡", key="next_page"):
#                     st.session_state["page"] += 1
#                     st.rerun()

# # Display and manage search history
# st.sidebar.subheader("📜 Search History")
# history = load_search_history()

# def set_search_query(past_query):
#     st.session_state["search_query"] = past_query
#     st.session_state["search_trigger"] = True
#     st.session_state["page"] = 1

# for i, past_query in enumerate(history[::-1], start=1):
#     st.sidebar.button(past_query, key=f"history_{i}", on_click=set_search_query, args=(past_query,))

# if st.sidebar.button("Clear History"):
#     save_search_history([])
#     st.sidebar.success("✅ History cleared!")
#     st.rerun()




import streamlit as st
import requests
import google.generativeai as genai  # Gemini API
import json
import os
import uuid

# Streamlit UI
st.set_page_config(page_title="AI Search", layout="wide")
st.title("🔍 AI-Powered SearchEngine")

# API Keys (Replace with your actual keys)
GEMINI_API_KEY = "AIzaSyDJMyOJn4SGA08JHx-bRhnrSq16KShTdmE"
SERPAPI_KEY = "2e51cef540ab0344835f29d26b699bf5e732cfd2f3241f3ba51729b64ee568cb"

# Initialize Google Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Function to get user-specific search history file
def get_user_history_file():
    user_id = st.session_state.get("user_id", str(uuid.uuid4()))  # Unique session ID
    st.session_state["user_id"] = user_id  # Store it in session
    return f"search_history_{user_id}.json"

# Load search history file
SEARCH_HISTORY_FILE = get_user_history_file()
if not os.path.exists(SEARCH_HISTORY_FILE):
    with open(SEARCH_HISTORY_FILE, "w") as f:
        json.dump([], f)

def save_search_history(history):
    """Save user-specific search history to file."""
    with open(SEARCH_HISTORY_FILE, "w") as f:
        json.dump(history, f)

def load_search_history():
    """Load user-specific past search queries."""
    with open(SEARCH_HISTORY_FILE, "r") as f:
        return json.load(f)

def google_search(query):
    """Fetch latest search results using SerpAPI dynamically."""
    url = "https://serpapi.com/search"
    params = {
        "q": query,
        "api_key": SERPAPI_KEY,
        "num": 10,
        "tbs": "qdr:d"  # Prioritize recent results
    }
    try:
        response = requests.get(url, params=params, timeout=20)
        response.raise_for_status()
        return response.json().get("organic_results", []), response.json().get("images_results", [])
    except requests.exceptions.RequestException:
        return [], []

def generate_ai_summary(query):
    """Generate an AI-powered summary using Gemini API with real-time data."""
    try:
        search_results, _ = google_search(query)
        context = "\n".join([res.get("title", "") + ": " + res.get("snippet", "") for res in search_results[:3]])
        if not context.strip():
            return "No reliable information available at the moment."
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(f"Latest update on {query}:\n{context}")
        return response.text if hasattr(response, "text") else "No confirmed information yet."
    except Exception:
        return "❌ AI summary unavailable due to API limits or errors."

if "search_query" not in st.session_state:
    st.session_state["search_query"] = ""
    st.session_state["search_trigger"] = False
    st.session_state["page"] = 1

def trigger_search():
    st.session_state["search_trigger"] = True
    st.session_state["page"] = 1  # Reset to first page on new search

query = st.text_input("Type your query:", key="search_query", on_change=trigger_search)

if st.session_state["search_trigger"] and st.session_state["search_query"].strip():
    query = st.session_state["search_query"]
    history = load_search_history()
    if query not in history:
        history.append(query)
        save_search_history(history)
    
    with st.spinner("✨ Fetching AI summary..."):
        summary = generate_ai_summary(query)
    st.subheader("📌 AI Summary")
    st.write(summary)
    st.write("---")

    with st.spinner("🔎 Searching the latest web results..."):
        results, _ = google_search(query)

    if not results:
        st.warning("⚠ No results found. Try a different query.")
    else:
        for i, result in enumerate(results[:5], start=1):
            st.markdown(f"{i}. [{result.get('title', 'No Title')}]({result.get('link', '#')})")
            st.write(result.get("snippet", "No snippet available."))
            st.write("---")

# Display user-specific search history
st.sidebar.subheader("📜 Your Search History")
history = load_search_history()

def set_search_query(past_query):
    st.session_state["search_query"] = past_query
    st.session_state["search_trigger"] = True
    st.session_state["page"] = 1

for i, past_query in enumerate(history[::-1], start=1):
    st.sidebar.button(past_query, key=f"history_{i}", on_click=set_search_query, args=(past_query,))

if st.sidebar.button("Clear History"):
    save_search_history([])
    st.sidebar.success("✅ History cleared!")
    st.rerun()
