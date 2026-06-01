# 🏪 Snap-to-Site AI
### Instant Professional Website Generator for Small Businesses

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://snap-to-site-xxxxxx.streamlit.app)

---

## 📌 Project Overview
Snap-to-Site AI is an intelligent web application that allows small business owners in Pakistan to generate a complete professional website in under 2 minutes. The user simply uploads a photo of their products or menu, enters basic business details, and AI automatically generates a fully designed, mobile-responsive HTML landing page.

---

## 🎯 Problem Statement
In Pakistan, millions of small businesses operate without any online presence because:
- Building a website requires technical knowledge
- Web developers charge PKR 20,000 to 100,000
- Most small business owners are not tech-savvy

**Snap-to-Site AI solves this problem instantly!**

---

## ✨ Key Features
- 📸 Photo upload with AI-powered menu detection
- 🤖 Automatic website generation using LLM API
- 🌐 Urdu and English language support
- 🎨 Multiple color themes and font styles
- 👁️ Live website preview inside the app
- 📥 One-click HTML file download
- 📞 Contact section with phone, email and address
- 📱 Mobile responsive professional design

---

## 🤖 AI Techniques Used
| Technique | Usage |
|---|---|
| Prompt Engineering | Generate professional HTML pages |
| LLM API (Groq + LLaMA 4) | Website code generation |
| Vision AI | Photo analysis and menu detection |
| Agentic AI | Two-step AI workflow |

---

## 🛠️ Technology Stack
| Component | Technology |
|---|---|
| Frontend | Streamlit (Python) |
| AI Model | LLaMA 4 via Groq API |
| Vision AI | Groq Vision API |
| Language | Python 3.12 |
| Deployment | Streamlit Cloud |

---

## ⚙️ Installation Instructions

### Step 1: Clone Repository
```bash
git clone https://github.com/yourusername/snap-to-site.git
cd snap-to-site
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Set API Key
Create a `.env` file:
### Step 4: Run App
```bash
python -m streamlit run app.py
```

---

## 📖 Usage Guide
1. Enter your **Business Name**
2. Select your **Business Type**
3. Fill in **Contact Details** (phone, email, address)
4. Upload your **Product or Menu Photo**
5. Click **"Detect Menu Items"** — AI will analyze photo
6. Review and edit detected items
7. Choose **Color Theme** and **Font Style**
8. Click **"Generate My Website"**
9. Preview your website live
10. Click **"Download"** to save HTML file

---

## ⚠️ Known Limitations
- Groq free tier has rate limits
- Very dark or blurry photos may not detect items accurately
- Generated website requires internet for Google Fonts
- Urdu text may not render perfectly in all browsers

---

## 🔒 Ethical Considerations
- User photos are NOT stored on any server
- All session data is deleted after use
- Content filtering prevents harmful websites
- No personal data shared with third parties

---

## 👩‍💻 Developed By
**Hiba Shaukat | Saba Shahid**
Department of Electrical and Computer Engineering
Hamdard University, Karachi
May 2026

---

## 📄 License
This project is developed for educational purposes as part of AI Capstone Project at Hamdard University.
