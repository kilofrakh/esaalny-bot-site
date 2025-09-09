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
st.subheader("Your Brand’s AI Chat Assistant")
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
    st.subheader("Starter")
    st.write("💵 900 EGP / month")
    st.write("✅ 1 Website Integration\n✅ Smart Recommendations\n✅ Email Support")
    st.link_button("Get Started", "https://forms.gle/hHViV4U4hmpPY69L6")

with col2:
    st.subheader("Pro")
    st.write("💵 1,800 EGP / month")
    st.write("✅ Up to 3 Websites\n✅ Advanced Personalization\n✅ Priority Support")
    st.link_button("Get Started", "https://forms.gle/hHViV4U4hmpPY69L6")

with col3:
    st.subheader("Enterprise")
    st.write("📞 Custom Pricing")
    st.write("✅ Unlimited Integrations\n✅ White-label Branding\n✅ Dedicated Support Manager")
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

st.write("---")
st.caption("© 2025 Esaalny Bot. Built with ❤️ in Egypt.")
