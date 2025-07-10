
import streamlit as st
import random

st.set_page_config(page_title="Profit & Loss Fun App", layout="centered")

st.title("💰 Profit & Loss Learning App for Kids")
st.subheader("Learn by playing! Simple English, big learning.")

# Item images and names
items = [
    {"name": "Toy Car", "img": "🚗"},
    {"name": "Ice Cream", "img": "🍦"},
    {"name": "Pencil Box", "img": "✏️"},
    {"name": "Book", "img": "📘"},
    {"name": "Chocolate", "img": "🍫"}
]

# Initialize session state
if 'cost_price' not in st.session_state:
    st.session_state.new_question = True

def generate_question():
    item = random.choice(items)
    level = st.session_state.level
    ranges = {
        "Easy (₹1–₹20)": (1, 20),
        "Medium (₹10–₹100)": (10, 100),
        "Hard (₹50–₹500)": (50, 500),
    }
    low, high = ranges[level]
    cost = random.randint(low, high)
    sell = random.randint(low, high)
    st.session_state.item = item
    st.session_state.cost_price = cost
    st.session_state.selling_price = sell
    st.session_state.new_question = False

# Level selector
st.session_state.level = st.selectbox("Choose your level:", ["Easy (₹1–₹20)", "Medium (₹10–₹100)", "Hard (₹50–₹500)"])

# Button to generate new question
if st.button("🎲 Next Question"):
    generate_question()

# Display question only if generated
if 'item' in st.session_state and not st.session_state.new_question:
    st.markdown(f"### Item: {st.session_state.item['img']} {st.session_state.item['name']}")
    st.write(f"Cost Price: ₹{st.session_state.cost_price}")
    st.write(f"Selling Price: ₹{st.session_state.selling_price}")

    user_choice = st.radio("What did you make?", ["Profit", "Loss"], key="choice")
    user_amount = st.number_input("How much?", min_value=0, step=1, key="amount")

    if st.button("Check Answer"):
        cost_price = st.session_state.cost_price
        selling_price = st.session_state.selling_price

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
    