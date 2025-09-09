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
# Hero Section
# ----------------------------
st.title("🤖 Esaalny Bot")
st.subheader("The Smart Chatbot for Brands")
st.write("Give your customers a human-like experience with AI that sells, recommends, and represents your brand.")

col1, col2 = st.columns(2)
with col1:
    st.link_button("🚀 Request Demo", "https://forms.gle/hHViV4U4hmpPY69L6")
with col2:
    st.link_button("👀 Try Live Demo", "#demo")

st.divider()

# ----------------------------
# Features Section
# ----------------------------
st.header("✨ Why Choose Esaalny Bot?")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("🎯 Personalized")
    st.write("Understands customer needs and suggests the right products instantly.")

with col2:
    st.subheader("💡 Brand Identity")
    st.write("Speaks in your brand’s tone & style — not just a generic chatbot.")

with col3:
    st.subheader("⚡ Easy Integration")
    st.write("Works with websites, Shopify stores, and messaging apps.")

with col4:
    st.subheader("📈 Boost Conversions")
    st.write("Turn visitors into loyal customers with smarter interactions.")

st.divider()

# ----------------------------
# Pricing Section
# ----------------------------
st.header("💰 Simple & Transparent Pricing")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Starter")
    st.write("$29 / month")
    st.write("✅ 1 Website Integration\n✅ Product Recommendations\n✅ Basic Support")
    st.link_button("Get Started", "https://forms.gle/hHViV4U4hmpPY69L6")

with col2:
    st.subheader("Pro")
    st.write("$59 / month")
    st.write("✅ Up to 3 Websites\n✅ Advanced AI Personalization\n✅ Priority Support")
    st.link_button("Get Started", "https://forms.gle/hHViV4U4hmpPY69L6")

with col3:
    st.subheader("Enterprise")
    st.write("Custom Pricing")
    st.write("✅ Unlimited Integrations\n✅ White-label Branding\n✅ Dedicated Support")
    st.link_button("Contact Us", "https://forms.gle/hHViV4U4hmpPY69L6")

st.divider()

# ----------------------------
# Live Demo Section
# ----------------------------
st.header("🧪 Try Esaalny Bot Live")
st.write("Test how Esaalny Bot interacts in real time:")

st.components.v1.iframe("https://esaalnybot-production.up.railway.app/chat", height=600)

st.divider()

# ----------------------------
# About Section
# ----------------------------
st.header("📖 About Esaalny Bot")
st.write(
    """
    Customers today want more than just products — they want to feel the *soul* of your brand.  
    Esaalny Bot helps you deliver this by:
    - Recommending products based on customer needs
    - Talking in your brand’s voice
    - Creating engaging conversations that boost loyalty
    """
)

st.divider()

# ----------------------------
# Contact Section
# ----------------------------
st.header("📩 Contact Us")
st.write("Got questions? Want to see Esaalny Bot in action? Reach out below!")

st.link_button("📌 Request Demo", "https://forms.gle/hHViV4U4hmpPY69L6")

st.write("---")
st.caption("© 2025 Esaalny Bot. All rights reserved.")
