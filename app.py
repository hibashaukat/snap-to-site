import streamlit as st
from groq import Groq
import base64
from PIL import Image
import io

# Configure Groq Client
import os
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
# Page Config
st.set_page_config(
    page_title="Snap-to-Site AI",
    page_icon="🏪",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    * { font-family: 'Poppins', sans-serif; }
    
    .main { background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); }
    
    .hero-title {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 52px;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0;
    }
    
    .hero-sub {
        text-align: center;
        color: #666;
        font-size: 18px;
        margin-bottom: 30px;
    }
    
    .card {
        background: white;
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    
    .section-title {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 10px 20px;
        border-radius: 10px;
        font-weight: 700;
        margin-bottom: 15px;
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 15px 30px;
        border-radius: 25px;
        font-size: 20px;
        font-weight: bold;
        width: 100%;
        transition: all 0.3s;
    }
    
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 20px rgba(102,126,234,0.5);
    }

    .detected-item {
        background: #f0f7ff;
        border-left: 4px solid #667eea;
        padding: 8px 15px;
        margin: 5px 0;
        border-radius: 5px;
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="hero-title">🏪 Snap-to-Site AI</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-sub">✨ Upload Photo → AI Detects Menu → Beautiful Website Ready in Seconds!</p>', unsafe_allow_html=True)
st.markdown("---")

# Language Selection
lang = st.radio("🌐 Select Language / زبان منتخب کریں:", 
                ["English", "اردو"], 
                horizontal=True)

st.markdown("---")

# ============ STEP 1: Business Details ============
st.markdown('<div class="section-title">📝 Step 1: Business Information</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if lang == "English":
        business_name = st.text_input("🏪 Business Name:", placeholder="e.g. Ahmed's Cafe")
        contact_number = st.text_input("📞 Contact Number:", placeholder="e.g. 0300-1234567")
        email = st.text_input("📧 Email Address:", placeholder="e.g. ahmed@gmail.com")
    else:
        business_name = st.text_input("🏪 کاروبار کا نام:", placeholder="مثال: احمد کیفے")
        contact_number = st.text_input("📞 رابطہ نمبر:", placeholder="مثال: 0300-1234567")
        email = st.text_input("📧 ای میل:", placeholder="مثال: ahmed@gmail.com")

with col2:
    if lang == "English":
        business_type = st.selectbox("🏢 Business Type:", [
            "Cafe / Restaurant",
            "Clothing Shop",
            "Bakery",
            "Grocery Store",
            "Beauty Salon",
            "Gym / Fitness",
            "Freelancer / Services",
            "Other"
        ])
        address = st.text_input("📍 Address:", placeholder="e.g. Block 5, Gulshan, Karachi")
        tagline = st.text_input("💬 Business Tagline:", placeholder="e.g. Best Coffee in Town!")
    else:
        business_type = st.selectbox("🏢 کاروبار کی قسم:", [
            "کیفے / ریستوران",
            "کپڑوں کی دکان",
            "بیکری",
            "گروسری اسٹور",
            "بیوٹی سیلون",
            "جم / فٹنس",
            "فری لانسر / خدمات",
            "دیگر"
        ])
        address = st.text_input("📍 پتہ:", placeholder="مثال: بلاک 5، گلشن، کراچی")
        tagline = st.text_input("💬 کاروبار کا نعرہ:", placeholder="مثال: شہر کی بہترین کافی!")

st.markdown("---")

# ============ STEP 2: Photo Upload & AI Detection ============
st.markdown('<div class="section-title">📸 Step 2: Upload Photo — AI Will Detect Menu Items!</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader(
        "Upload Your Product / Menu Photo:",
        type=["jpg", "jpeg", "png", "jfif"]
    )
    
    if uploaded_file:
        st.image(uploaded_file, caption="✅ Photo Uploaded!", use_column_width=True)

with col2:
    st.markdown("#### 🤖 AI Detected Items:")
    
    detected_items_placeholder = st.empty()
    
    if uploaded_file:
        if st.button("🔍 Detect Menu Items from Photo!"):
            with st.spinner("🤖 AI is analyzing your photo..."):
                try:
                    image = Image.open(uploaded_file)
                    buffered = io.BytesIO()
                    image.save(buffered, format="PNG")
                    img_base64 = base64.b64encode(buffered.getvalue()).decode()
                    
                    detect_response = client.chat.completions.create(
                        model="meta-llama/llama-4-scout-17b-16e-instruct",
                        messages=[
                            {
                                "role": "user",
                                "content": [
                                    {
                                        "type": "image_url",
                                        "image_url": {"url": f"data:image/png;base64,{img_base64}"}
                                    },
                                    {
                                        "type": "text",
                                        "text": f"""Analyze this image for a {business_type} business.
List all products, food items, or services you can see.
Format each item as: Item Name - Rs. Price
If you cannot determine price, write Rs. 0
List maximum 10 items.
Return ONLY the list, one item per line, nothing else.
{"Write item names in Urdu if possible." if lang == "اردو" else "Write item names in English."}"""
                                    }
                                ]
                            }
                        ],
                        max_tokens=500
                    )
                    
                    detected_text = detect_response.choices[0].message.content
                    st.session_state['detected_items'] = detected_text
                    st.success("✅ Items detected! You can edit them below.")
                    
                except Exception as e:
                    st.error(f"Detection Error: {str(e)}")

st.markdown("---")

# ============ STEP 3: Menu Items Edit ============
st.markdown('<div class="section-title">🍽️ Step 3: Review & Edit Menu Items</div>', unsafe_allow_html=True)

default_menu = st.session_state.get('detected_items', 
    "Cappuccino - Rs. 250\nCheese Burger - Rs. 450\nChocolate Cake - Rs. 350")

if lang == "اردو":
    menu_items = st.text_area(
        "اپنی مصنوعات / مینو آئٹمز ترمیم کریں (ہر لائن میں ایک):",
        value=default_menu,
        height=200,
        placeholder="مثال:\nکیپوچینو - Rs. 250\nچاکلیٹ کیک - Rs. 350"
    )
else:
    menu_items = st.text_area(
        "✏️ Review & Edit Your Menu Items (one per line):",
        value=default_menu,
        height=200,
        placeholder="e.g.\nCappuccino - Rs. 250\nChocolate Cake - Rs. 350"
    )

st.markdown("---")

# ============ STEP 4: Design ============
st.markdown('<div class="section-title">🎨 Step 4: Choose Your Website Design</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    color_theme = st.selectbox("🎨 Color Theme:", [
        "🌊 Modern Blue & White",
        "🌿 Elegant Green & Gold",
        "🌸 Luxury Purple & Pink",
        "🔥 Bold Red & Black",
        "☕ Warm Brown & Cream",
        "🌙 Dark & Premium"
    ])

with col2:
    font_style = st.selectbox("✍️ Font Style:", [
        "Poppins (Modern)",
        "Playfair Display (Elegant)",
        "Roboto (Clean)",
        "Montserrat (Bold)"
    ])

st.markdown("---")

# ============ GENERATE BUTTON ============
if st.button("🚀 Generate My Professional Website Now!"):
    if not business_name:
        st.error("⚠️ Please enter your business name!")
    elif not uploaded_file:
        st.error("⚠️ Please upload a photo!")
    elif not menu_items:
        st.error("⚠️ Please add menu items!")
    else:
        with st.spinner("✨ Creating your stunning website... Please wait 30 seconds!"):
            try:
                image = Image.open(uploaded_file)
                buffered = io.BytesIO()
                image.save(buffered, format="PNG")
                img_base64 = base64.b64encode(buffered.getvalue()).decode()

                theme_colors = {
                    "🌊 Modern Blue & White": {"primary": "#1a73e8", "secondary": "#ffffff", "accent": "#0d47a1", "text": "#333333", "bg": "#f8f9ff", "card": "#ffffff"},
                    "🌿 Elegant Green & Gold": {"primary": "#2e7d32", "secondary": "#f9f3e3", "accent": "#ffd700", "text": "#1a1a1a", "bg": "#f1f8e9", "card": "#ffffff"},
                    "🌸 Luxury Purple & Pink": {"primary": "#7b1fa2", "secondary": "#fce4ec", "accent": "#e91e63", "text": "#1a1a1a", "bg": "#f9f0ff", "card": "#ffffff"},
                    "🔥 Bold Red & Black": {"primary": "#c62828", "secondary": "#212121", "accent": "#ff5722", "text": "#ffffff", "bg": "#1a1a1a", "card": "#2d2d2d"},
                    "☕ Warm Brown & Cream": {"primary": "#5d4037", "secondary": "#fff8e1", "accent": "#ff8f00", "text": "#3e2723", "bg": "#fdf6e3", "card": "#ffffff"},
                    "🌙 Dark & Premium": {"primary": "#00bcd4", "secondary": "#263238", "accent": "#00bcd4", "text": "#ffffff", "bg": "#1c2833", "card": "#263238"}
                }

                colors = theme_colors[color_theme]
                font = font_style.split(" ")[0]

                response = client.chat.completions.create(
                    model="meta-llama/llama-4-scout-17b-16e-instruct",
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "image_url",
                                    "image_url": {"url": f"data:image/png;base64,{img_base64}"}
                                },
                                {
                                    "type": "text",
                                    "text": f"""You are a world-class web designer. Create a stunning, eye-catching, professional HTML landing page.

BUSINESS DETAILS:
- Name: {business_name}
- Type: {business_type}
- Tagline: {tagline if tagline else f'Best {business_type} in Town!'}
- Phone: {contact_number if contact_number else 'Not provided'}
- Email: {email if email else 'Not provided'}
- Address: {address if address else 'Not provided'}
- Language: {lang}

MENU ITEMS (USE EXACTLY THESE):
{menu_items}

DESIGN:
- Primary: {colors['primary']}
- Background: {colors['bg']}
- Accent: {colors['accent']}
- Text: {colors['text']}
- Card Background: {colors['card']}
- Font: {font} from Google Fonts

STRICT REQUIREMENTS:
1. Import {font} from Google Fonts
2. Sticky navigation bar — business name + emoji logo + nav links
3. HERO section — full width, gradient background, large business name, tagline, "Order Now" button with animation
4. MENU/PRODUCTS section — beautiful grid cards (3 columns), each card has:
   - Colorful emoji icon
   - Item name (EXACT from menu items above)
   - Price (EXACT from menu items above)  
   - Short mouth-watering description
   - Hover animation effect
   - "Add to Cart" button
5. ABOUT US section — beautiful description of the business
6. CONTACT section — phone, email, address with icons (use font awesome icons)
7. FOOTER — business name, copyright 2026, social media icons
8. CSS animations — fadeIn, slideUp effects
9. Fully mobile responsive
10. {"Add Urdu text support with proper RTL where needed" if lang == "اردو" else ""}
11. Make it look like a Rs. 100,000 professionally designed website
12. Add Font Awesome icons: <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
13. Return ONLY pure HTML — no explanation, no markdown, no backticks"""
                                }
                            ]
                        }
                    ],
                    max_tokens=8000
                )

                generated_html = response.choices[0].message.content

                if "```html" in generated_html:
                    generated_html = generated_html.split("```html")[1].split("```")[0]
                elif "```" in generated_html:
                    generated_html = generated_html.split("```")[1].split("```")[0]

                st.success("🎉 Your Stunning Website is Ready!")
                st.balloons()

                tab1, tab2 = st.tabs(["🌐 Live Preview", "💻 HTML Code"])

                with tab1:
                    st.components.v1.html(generated_html, height=700, scrolling=True)

                with tab2:
                    st.code(generated_html, language="html")

                st.markdown("### 📥 Download Your Website:")
                b64 = base64.b64encode(generated_html.encode()).decode()
                href = f'''<a href="data:text/html;base64,{b64}" 
                   download="{business_name}_website.html"
                   style="display:inline-block;background:linear-gradient(135deg,#667eea,#764ba2);
                   color:white;padding:15px 40px;border-radius:25px;text-decoration:none;
                   font-size:18px;font-weight:bold;margin-top:10px;
                   box-shadow:0 5px 20px rgba(102,126,234,0.5);">
                   📥 Download Your Professional Website
                </a>'''
                st.markdown(href, unsafe_allow_html=True)

            except Exception as e:
                st.error(f"Error: {str(e)}")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align:center; color:#666; padding:20px;'>
    <strong>🏪 Snap-to-Site AI</strong> — Powered by Groq AI & LLaMA 4 | © 2026
</div>
""", unsafe_allow_html=True)