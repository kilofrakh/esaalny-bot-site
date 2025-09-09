import streamlit as st

# ----------------------------
# Page config
# ----------------------------
st.set_page_config(
    page_title="Esaalny Bot - Smart AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

# ----------------------------
# Custom CSS for Styling
# ----------------------------
st.markdown("""
    <style>
        /* Global background */
        body {
            background-color: #f9fafb;
        }

        /* Title and headers */
        .stApp h1 {
            font-size: 3rem;
            font-weight: 800;
            color: #1f2937;
        }
        .stApp h2, .stApp h3 {
            color: #111827;
            font-weight: 700;
        }

        /* Buttons */
        .stButton>button, .stLinkButton>button {
            background: linear-gradient(90deg, #2563eb, #3b82f6);
            color: white !important;
            border-radius: 12px;
            padding: 0.6em 1.2em;
            border: none;
            font-weight: 600;
            transition: 0.2s;
        }
        .stButton>button:hover, .stLinkButton>button:hover {
            background: linear-gradient(90deg, #1d4ed8, #2563eb);
            transform: scale(1.05);
        }

        /* Pricing cards */
        .pricing-card {
            background: white;
            padding: 2em;
            border-radius: 16px;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.05);
            text-align: center;
        }
        .pricing-card h3 {
            font-size: 1.5rem;
            margin-bottom: 0.5em;
        }
        .pricing-card p {
            color: #4b5563;
        }

        /* Footer */
        footer {
            text-align: center;
            padding: 2em 0;
            color: #6b7280;
            font-size: 0.9rem;
        }
    </style>
""", unsafe_allow_html=True)

# ----------------------------
# Hero Section
# ----------------------------
st.markdown("<h1 style='text-align: center;'>🤖 Esaalny Bot</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Your Brand’s AI Chat Assistant</h2>", unsafe_allow_html=True)

st.write(
    """
    Customers don’t just want to see your products.  
    They want to feel your brand’s **soul and identity**.  

    Esaalny Bot is built to talk like your brand, recommend the right products,  
    and make every visitor feel like they’re chatting with a real team member.
    """
)

col1, col2 = st.columns(2)
with col1:
    st.link_button("🚀 Request a Free Demo", "https://forms.gle/hHViV4U4hmpPY69L6")
with col2:
    st.link_button("👀 Try Live Demo", "#demo")

st.divider()

# ----------------------------
# Features Section
# ----------------------------
st.header("✨ What Makes Esaalny Bot Different?")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("🎯 Personalized")
    st.write("Understands each customer and recommends what fits their needs.")

with col2:
    st.subheader("💡 Brand Voice")
    st.write("Trains to speak like your brand — no boring, generic chatbot replies.")

with col3:
    st.subheader("⚡ Plug & Play")
    st.write("Easy to add to your website, Shopify, or even custom platforms.")

with col4:
    st.subheader("📈 Sales Growth")
    st.write("Turns visitors into paying customers with engaging conversations.")

st.divider()

# ----------------------------
# Pricing Section (EGP)
# ----------------------------
st.header("💰 Simple & Transparent Pricing (in EGP)")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="pricing-card">
            <h3>Starter</h3>
            <p>💵 900 EGP / month</p>
            <p>✅ 1 Website Integration<br>✅ Smart Recommendations<br>✅ Email Support</p>
        </div>
        """, unsafe_allow_html=True
    )
    st.link_button("Get Started", "https://forms.gle/hHViV4U4hmpPY69L6")

with col2:
    st.markdown(
        """
        <div class="pricing-card">
            <h3>Pro</h3>
            <p>💵 1,800 EGP / month</p>
            <p>✅ Up to 3 Websites<br>✅ Advanced Personalization<br>✅ Priority Support</p>
        </div>
        """, unsafe_allow_html=True
    )
    st.link_button("Get Started", "https://forms.gle/hHViV4U4hmpPY69L6")

with col3:
    st.markdown(
        """
        <div class="pricing-card">
            <h3>Enterprise</h3>
            <p>📞 Custom Pricing</p>
            <p>✅ Unlimited Integrations<br>✅ White-label Branding<br>✅ Dedicated Support Manager</p>
        </div>
        """, unsafe_allow_html=True
    )
    st.link_button("Contact Us", "https://forms.gle/hHViV4U4hmpPY69L6")

st.divider()

# ----------------------------
# Live Demo Section
# ----------------------------
st.header("🧪 Try Esaalny Bot Right Now")
st.write("See how the chatbot talks with your customers in real time:")

st.components.v1.iframe("https://esaalnybot-production.up.railway.app/chat", height=600)

st.divider()

# ----------------------------
# About Section
# ----------------------------
st.header("📖 Our Story")
st.write(
    """
    I built Esaalny Bot after seeing how most brands struggle to connect  
    with customers online. People don’t want *just answers* — they want  
    conversations that feel natural and **true to your brand**.  

    Esaalny Bot gives your business that edge.  
    It’s not just a chatbot — it’s your **brand ambassador** online.
    """
)

st.divider()

# ----------------------------
# Contact Section
# ----------------------------
st.header("📩 Let’s Talk")
st.write("Have questions? Want to see what Esaalny Bot can do for your business?")

st.link_button("📌 Request a Free Demo", "https://forms.gle/hHViV4U4hmpPY69L6")

# ----------------------------
# Footer
# ----------------------------
st.markdown(
    "<footer>© 2025 Esaalny Bot. Built with ❤️ in Egypt.</footer>",
    unsafe_allow_html=True
)
