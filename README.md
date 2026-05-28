# VISHNU-AI-CHATBOT
Built an AI-powered campus assistant using Python, ChromaDB, GroqCloud APIs, and a RAG pipeline to deliver context-aware answers for campus navigation and timetable queries. Implemented semantic search over CSV/XLSX datasets using vector embeddings and LLM-based response generation.

The chatbot answers student queries using multiple structured college datasets such as:

- Faculty details
- Hostel information
- Clubs and activities
- Placement companies
- EAMCET cutoff ranks
- Publications
- FAQs

---

# 🚀 Features

✅ Multi-file dataset ingestion (`CSV + XLSX`)  
✅ Retrieval-Augmented Generation (RAG) pipeline  
✅ Semantic search using vector embeddings  
✅ Conversational chatbot UI using Streamlit  
✅ Context-aware responses from institutional datasets  
✅ Fast inference using Groq LLM APIs  
✅ Supports multiple student query domains  
✅ ChatGPT-style chat interface  

---

# 🧠 Tech Stack

| Technology | Usage |
|---|---|
| Python | Core development |
| LangChain | RAG pipeline orchestration |
| ChromaDB | Vector database |
| HuggingFace Embeddings | Semantic embeddings |
| Groq API | LLM inference |
| Streamlit | Frontend UI |
| Pandas | Dataset processing |

---

# 🏗️ System Architecture

```text
User Query
    ↓
Retriever (ChromaDB)
    ↓
Relevant Context Retrieval
    ↓
Prompt + Context
    ↓
Groq LLM
    ↓
Final Response
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone YOUR_GITHUB_REPO_LINK
cd rag_chatbot
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

### Windows

```bash
.venv\Scripts\activate
```

### Linux/Mac

```bash
source .venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

# ▶️ Run Application

```bash
streamlit run app.py
```

---

# 💬 Example Queries

- "Who is the HOD of AI Department?"
- "What is the hostel fee?"
- "What are the latest EAMCET cutoff ranks for CSE?"
- "Which clubs are available in college?"
- "Which companies visited for placements?"

---

# 🧩 How RAG Works in This Project

1. Multiple structured datasets are loaded.
2. Documents are chunked using RecursiveCharacterTextSplitter.
3. Embeddings are generated using HuggingFace models.
4. Chunks are stored in ChromaDB vector database.
5. Relevant context is retrieved using semantic similarity.
6. Retrieved context is passed to Groq LLM.
7. Final contextual response is generated.

---

# 🎯 Key Learning Outcomes

- Built a complete end-to-end RAG application
- Implemented semantic search using embeddings
- Worked with vector databases
- Integrated LLM APIs for contextual QA
- Developed interactive AI applications using Streamlit
- Managed structured institutional datasets for AI retrieval

---

# 🔮 Future Improvements

- Persistent ChromaDB storage
- Conversation memory
- Multi-user authentication
- Voice-based interaction
- PDF support
- Hybrid search (keyword + semantic)
- Deployment on Streamlit Cloud / HuggingFace Spaces

---
If you liked this project, feel free to ⭐ the repository.
