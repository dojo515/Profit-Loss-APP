
import streamlit as st
import random

st.set_page_config(page_title="Profit & Loss Fun App", layout="centered")

st.title("💰 Profit & Loss Learning App for Kids")
st.subheader("Learn by playing! Simple English, big learning.")

# Level selection
level = st.selectbox("Choose your level:", ["Easy (₹1–₹20)", "Medium (₹10–₹100)", "Hard (₹50–₹500)"])

# Set ranges based on level
ranges = {
    "Easy (₹1–₹20)": (1, 20),
    "Medium (₹10–₹100)": (10, 100),
    "Hard (₹50–₹500)": (50, 500),
}

low, high = ranges[level]

# Generate random cost and selling price
cost_price = random.randint(low, high)
selling_price = random.randint(low, high)

st.write(f"You bought an item for ₹{cost_price}.")
st.write(f"You sold it for ₹{selling_price}.")

# Question to user
user_choice = st.radio("What did you make?", ["Profit", "Loss"])
user_amount = st.number_input("How much?", min_value=0, step=1)

# Check answer
if st.button("Check Answer"):
    if selling_price > cost_price:
        correct_type = "Profit"
        correct_amount = selling_price - cost_price
    elif selling_price < cost_price:
        correct_type = "Loss"
        correct_amount = cost_price - selling_price
    else:
        correct_type = "Neither"
        correct_amount = 0

    if user_choice == correct_type and user_amount == correct_amount:
        st.success(f"✅ Great job! You made a {correct_type} of ₹{correct_amount}!")
    else:
        st.error(f"❌ Oops! It was a {correct_type} of ₹{correct_amount}. Try again!")

st.markdown("---")
st.caption("Made for Grades 4–5 | Simple English | Math is fun! 🎉")
    