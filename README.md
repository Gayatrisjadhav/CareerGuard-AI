# CareerGuard-AI
Your only true friend for career Advice

# 🚀 CareerGuard AI – Animated RAG Career Advisor

CareerGuard AI is an AI-powered, animated web application built using FastAPI, LangChain, and GSAP. It helps users evaluate how risky their job is in the AI era and suggests safe alternatives and skills to future-proof their careers.

<img src="static/screenshot.png" alt="CareerGuard AI Screenshot" width="100%" />

---

## 🌟 Features

- ✨ **Fully animated frontend** using GSAP and 3D tilt
- 🔥 **Gradient background transitions**
- 💬 Real-time career risk analysis using **RAG (Retrieval-Augmented Generation)**
- 🤖 LLMs (LLaMA 3 via Groq) + Tavily Search + FAISS + HuggingFace Embeddings
- 🛠️ Dynamic section breakdown: **Risk**, **Alternatives**, **Skills**
- 🌗 Dark mode toggle
- 🎯 Mobile responsive & scroll-snapping UI

---

## ⚙️ Tech Stack

| Layer        | Technology                     |
|--------------|--------------------------------|
| Backend      | FastAPI, LangChain, FAISS      |
| LLMs         | Groq (LLaMA 3), Tavily Search  |
| Embeddings   | HuggingFace Transformers       |
| Frontend     | HTML, CSS, JS, GSAP, Tilt.js   |
| Deployment   | (Optional) Docker, Render/Vercel/Fly.io |

---

## 🧠 RAG Pipeline (Backend)

1. **User Query** → `get_rag_answer()`
2. Tavily Search fetches relevant context
3. FAISS builds vector store
4. LangChain's RetrievalQA fetches best answers using Groq LLM
5. Answer is split into:
   - **Step 1** – Risk
   - **Step 2** – Alternatives
   - **Step 3** – Skills

---

## 🚀 Getting Started

### 1. Clone the Repository

bash
git clone https://github.com/yourusername/careerguard-ai.git
cd careerguard-ai

### 2. Setup virtual Environment
python -m venv venv
#Activate the virtual environment:
#macOS/Linux:
source venv/bin/activate
#Windows:
venv\Scripts\activate
### 3. Install Requirements
pip install -r requirements.txt
fastapi
uvicorn
langchain
langchain_community
langchain_core
langchain_groq
python-dotenv
tavily
faiss-cpu
jinja2
markdown
huggingface_hub
transformers
### 4. create .env file
TAVILY_API_KEY=your_actual_tavily_api_key
GROQ_API_KEY=your_actual_groq_api_key
GROQ_MODEL=llama3-70b-8192
### 5. Run the App
uvicorn main:app --reload

## Project Structure
career-guard-ai/
-│
-├── main.py
-├── rag.py
-├── .env
-├── requirements.txt
-├── templates/
-│   └── index.html
-├── static/
-│   ├── style.css
-│   ├── script.js
-│   └── screenshot.png
-└── README.md

## ⚙️ Core Technologies
-Backend: FastAPI, LangChain, FAISS

-LLM: Groq LLaMA-3-70B

-Embedding: HuggingFace Embeddings

- Frontend: HTML, CSS, JS (GSAP, Tilt.js), Jinja2

- Data Source: Tavily Search API

## 🌌 UI Features
- Full-page scroll sections (Risk, Alternatives, Skills)

- Typewriter loader animation

- Gradient transitions & particle backgrounds

- GSAP scroll animations

- Responsive & mobile-ready


## 🛠 Future Enhancements
- 🔁 Chat history & feedback loop

- 🧠 Resume-based risk prediction

- 📊 Personalized dashboard with upskilling tracker

- 🎤 Voice input (using Web Speech API)

- 🌐 Deploy on Render or Vercel




