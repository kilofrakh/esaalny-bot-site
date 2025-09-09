import streamlit as st

# ----------------------------
# Page config
# ----------------------------
st.set_page_config(
    page_title="Esaalny Bot - Smart AI Chatbot",
    page_icon="💬",
    layout="wide"
)

# ----------------------------
# Custom CSS for Styling
# ----------------------------
st.markdown("""
    <style>
        /* Global background */
        .stApp {
            background-color: #f9fafb;
            font-family: 'Segoe UI', sans-serif;
        }

        /* Hero section */
        .hero-title {
            font-size: 3rem;
            font-weight: 800;
            text-align: center;
            color: #1e40af; /* Strong blue */
        }
        .hero-subtitle {
            text-align: center;
            font-size: 1.4rem;
            color: #2563eb; /* Lighter blue */
            margin-bottom: 1.5em;
        }

        /* Normal text */
        p, li, .stMarkdown, .stText {
            color: #1e3a8a !important; /* Blue text */
        }

        /* Buttons */
        .stButton>button, .stLinkButton>button {
            background: linear-gradient(90deg, #2563eb, #3b82f6);
            color: white !important;
            border-radius: 10px;
            padding: 0.6em 1.2em;
            border: none;
            font-weight: 600;
            transition: all 0.2s ease-in-out;
        }
        .stButton>button:hover, .stLinkButton>button:hover {
            background: linear-gradient(90deg, #1e40af, #2563eb);
            transform: scale(1.05);
        }

        /* Pricing cards */
        .pricing-card {
            background: #ffffff;
            padding: 2em;
            border-radius: 16px;
            box-shadow: 0px 6px 20px rgba(0,0,0,0.05);
            text-align: center;
            transition: transform 0.2s ease-in-out;
        }
        .pricing-card:hover {
            transform: translateY(-5px);
        }
        .pricing-card h3 {
            font-size: 1.5rem;
            color: #1e40af; /* Dark blue headings */
            margin-bottom: 0.5em;
        }
        .pricing-card p {
            color: #2563eb; /* Lighter blue text */
        }

        /* Section headers */
        h2, h3 {
            color: #1e40af !important; /* Strong blue */
            font-weight: 700;
            margin-top: 1.5em;
        }

        /* Footer */
        footer {
            text-align: center;
            padding: 2em 0;
            color: #2563eb;
            font-size: 0.9rem;
        }
    </style>
""", unsafe_allow_html=True)

# ----------------------------
# Hero Section
# ----------------------------
st.markdown("<h1 class='hero-title'>Esaalny Bot</h1>", unsafe_allow_html=True)
st.markdown("<p class='hero-subtitle'>Your Brand’s AI Chat Assistant</p>", unsafe_allow_html=True)

st.write(
    """
    Customers don’t just want to see your products.  
    They want to feel your brand’s **soul and identity**.  

    Esaalny Bot is designed to speak in your brand’s voice, recommend the right products,  
    and make every visitor feel like they’re talking with a real team member.
    """
)

col1, col2 = st.columns(2)
with col1:
    st.link_button("Request a Free Demo", "https://forms.gle/hHViV4U4hmpPY69L6")
with col2:
    st.link_button("Try Live Demo", "#demo")

st.divider()

# ----------------------------
# Features Section
# ----------------------------
st.header("Why Choose Esaalny Bot?")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("Personalized")
    st.write("Understands each customer and recommends products that fit their needs.")

with col2:
    st.subheader("Brand Voice")
    st.write("Adapts to your tone and style, so every reply feels authentic.")

with col3:
    st.subheader("Easy Integration")
    st.write("Works smoothly with websites, Shopify, and custom platforms.")

with col4:
    st.subheader("Boost Sales")
    st.write("Converts visitors into loyal customers with engaging conversations.")

st.divider()

# ----------------------------
# Pricing Section (EGP)
# ----------------------------
st.header("Transparent Pricing (EGP)")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="pricing-card">
            <h3>Starter</h3>
            <p><strong>900 EGP / month</strong></p>
            <p>1 Website Integration<br>Smart Recommendations<br>Email Support</p>
        </div>
        """, unsafe_allow_html=True
    )
    st.link_button("Get Starter", "https://forms.gle/hHViV4U4hmpPY69L6")

with col2:
    st.markdown(
        """
        <div class="pricing-card">
            <h3>Pro</h3>
            <p><strong>1,800 EGP / month</strong></p>
            <p>Up to 3 Websites<br>Advanced Personalization<br>Priority Support</p>
        </div>
        """, unsafe_allow_html=True
    )
    st.link_button("Get Pro", "https://forms.gle/hHViV4U4hmpPY69L6")

with col3:
    st.markdown(
        """
        <div class="pricing-card">
            <h3>Enterprise</h3>
            <p><strong>Custom Pricing</strong></p>
            <p>Unlimited Integrations<br>White-label Branding<br>Dedicated Manager</p>
        </div>
        """, unsafe_allow_html=True
    )
    st.link_button("Contact Us", "https://forms.gle/hHViV4U4hmpPY69L6")

st.divider()

# ----------------------------
# Live Demo Section
# ----------------------------
st.header("Try Esaalny Bot Live")
st.write("See how the chatbot engages with your customers:")

st.components.v1.iframe("https://esaalnybot-production.up.railway.app/chat", height=600)

st.divider()

# ----------------------------
# About Section
# ----------------------------
st.header("About Esaalny Bot")
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
st.header("Contact Us")
st.write("Have questions? Want to see what Esaalny Bot can do for your business?")

st.link_button("Request a Free Demo", "https://forms.gle/hHViV4U4hmpPY69L6")

# ----------------------------
# Footer
# ----------------------------
st.markdown(
    "<footer>© 2025 Esaalny Bot. Built with passion in Egypt.</footer>",
    unsafe_allow_html=True
)
