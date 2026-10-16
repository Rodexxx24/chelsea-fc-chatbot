# 🔵 Stamford Bridge AI - Chelsea FC Chatbot

**Stamford Bridge AI** adalah aplikasi chatbot berbasis Artificial Intelligence yang dirancang khusus untuk fans sejati Chelsea FC. Chatbot ini dibangun menggunakan **LangChain**, **Google Gemini API**, dan **Streamlit**, dilengkapi dengan persona pendukung setia Chelsea yang selalu siap menjawab pertanyaan seputar sejarah, pemain, hingga merespons klaim klub rival dengan elegan dan humoris!

---

## ✨ Fitur Utama

- **🔵 Chelsea Fan Persona ("BlueBot"):** Memiliki gaya bicara khas fans Chelsea (jargon: *KTBFFH*, *Pride of London*, *Come on Chelsea*).
- **🧠 Conversational Memory:** Mengingat konteks percakapan dalam satu sesi obrolan.
- **🛡️ Error Handling & Graceful Fallback:** Menangani lonjakan *traffic* server API dengan pesan responsif tanpa memutus pengalaman pengguna.
- **💻 Interactive Web UI:** Antarmuka web interaktif yang simpel dan responsif dibangun menggunakan Streamlit.
- **⚽ Football Guardrails:** Fokus menjawab topik seputar Chelsea FC dan sepak bola, serta menolak topik di luar konteks dengan sopan.

---

## 🛠️ Tech Stack

- **Bahasa Pemrograman:** Python 3.12+
- **Framework & Library:**
  - `Streamlit` - Antarmuka Web (UI)
  - `LangChain` (`langchain-google-genai`, `langchain-core`) - Framework AI & Manajemen Prompt
  - `Google Gemini API` - Model Bahasa (LLM)
  - `python-dotenv` - Manajemen Variabel Lingkungan

---

## 📁 Struktur Proyek

```text
chelsea-chatbot/
├── data/                  # Folder dokumen konteks/sejarah (opsional untuk RAG)
├── .env                   # Variabel lingkungan rahasia (API Key)
├── .gitignore             # Mengabaikan file sensitif agar tidak terunggah
├── app.py                 # Kode utama aplikasi Streamlit & AI
├── requirements.txt       # Daftar pustaka / dependensi Python
└── README.md              # Dokumentasi proyek
