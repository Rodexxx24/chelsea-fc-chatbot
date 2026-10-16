import streamlit as st
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# 1. Load API Key dari file .env
load_dotenv()

# 2. Setup Tampilan Halaman Web Streamlit
st.set_page_config(page_title="Chelsea FC Chatbot", page_icon="🔵")
st.title("🔵 Stamford Bridge AI")
st.caption("Asisten AI khusus fans sejati Chelsea. KTBFFH!")

# 3. Inisialisasi Otak AI (Gemini 1.5 Flash)
if "chat_model" not in st.session_state:
    st.session_state.chat_model = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro", 
        temperature=0.7
    )

# 4. Injeksi Persona (System Prompt)
system_prompt = SystemMessage(
    content="""Kamu adalah asisten AI pendukung setia Chelsea FC bernama 'BlueBot'. 
    Gunakan nada bicara yang antusias, selalu dukung Chelsea, 
    dan gunakan jargon seperti 'KTBFFH', 'Pride of London', atau 'Come on Chelsea'. 
    Jika ditanya soal klub rival (seperti Arsenal, Tottenham, atau Man Utd), berikan jawaban yang sedikit menyindir tapi tetap sopan.
    Jika ditanya di luar topik sepak bola, tolak dengan sopan dan kembalikan obrolan ke Chelsea."""
)

# 5. Inisialisasi Memori Percakapan di layars
if "messages" not in st.session_state:
    st.session_state.messages = []

# Tampilkan riwayat chat lama saat layar di-refresh
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 6. Kolom Input User
user_input = st.chat_input("Tanya sesuatu tentang Chelsea FC...")

if user_input:
    # Tampilkan teks user di layar dan simpan ke memori
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Susun riwayat percakapan untuk dibaca oleh LangChain
    langchain_messages = [system_prompt]
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            langchain_messages.append(HumanMessage(content=msg["content"]))
        else:
            langchain_messages.append(AIMessage(content=msg["content"]))
            
    # Minta jawaban dari AI
    try:
        with st.spinner("Mengingat sejarah di Stamford Bridge..."):
            response = st.session_state.chat_model.invoke(langchain_messages)
        
        # Tampilkan jawaban AI di layar dan simpan ke memori
        st.chat_message("assistant").markdown(response.content)
        st.session_state.messages.append({"role": "assistant", "content": response.content})
        
    except Exception as e:
        # Menampilkan pesan error yang ramah pengguna jika API gagal
        st.error("Waduh, server AI sedang penuh! Stamford Bridge lagi ramai nih. Silakan coba kirim pesan lagi dalam beberapa menit.")
