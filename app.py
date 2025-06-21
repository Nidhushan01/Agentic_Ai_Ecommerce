import streamlit as st
from utils.openai_agent import parse_user_input
from utils.amazon_scraper import get_product_data_amazon

st.set_page_config(page_title="Agentic Price Tracker", page_icon="🛍️")

st.title("🛒 Agentic AI: E-commerce Price Tracker")
st.markdown("Enter your shopping rule and product URL. The agent will decide whether to buy or not.")

# --- Input fields ---
user_command = st.text_input("🧠 Your Command", placeholder="Track iPhone. Buy if under $800 and rating > 4")
product_url = st.text_input("🔗 Product URL (Amazon)", placeholder="https://www.amazon.com/...")

if st.button("🔍 Analyze"):
    if not user_command or not product_url:
        st.warning("Please provide both command and product URL.")
    else:
        with st.spinner("🤖 Parsing your command..."):
            try:
                rules = parse_user_input(user_command)
                st.success("✅ Rules Parsed")
                st.json(rules)
            except Exception as e:
                st.error(f"Error parsing input: {e}")
                st.stop()

        with st.spinner("🕵️ Scraping product info..."):
            product_data = get_product_data_amazon(product_url)
            st.success("✅ Product Data Retrieved")
            st.write(f"**Current Price:** ${product_data['price']}")
            st.write(f"**Seller Rating:** {product_data['rating']} ⭐")

        # --- Decision logic ---
        # ✅ Safely handle cases where price or rating is None
        if (
            product_data.get("price") is not None and
            product_data.get("rating") is not None and
            rules.get("target_price") is not None and
            rules.get("min_seller_rating") is not None
        ):
            if (
                product_data["price"] <= rules["target_price"] and
                product_data["rating"] >= rules["min_seller_rating"]
            ):
                st.success("🎉 ✅ Decision: BUY")
            else:
                st.warning("⚠️ ❌ Decision: DO NOT BUY")
        else:
            st.error("❌ Incomplete product data or rule values – cannot make a decision.")
            st.json({"rules": rules, "product_data": product_data})  # 🧠 Debug info
