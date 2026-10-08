import streamlit as st

# Title and styling
st.set_page_config(page_title="My Calculator", page_icon="🧮")
st.title("🧮 Simple Calculator")

# Input fields
col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("Enter first number", value=0.0)
with col2:
    num2 = st.number_input("Enter second number", value=0.0)

# Operation selection
operation = st.selectbox("Choose operation", ["Add (+)", "Subtract (-)", "Multiply (*)", "Divide (/)"])

# Calculate button
if st.button("Calculate", type="primary"):
    if operation == "Add (+)":
        result = num1 + num2
    elif operation == "Subtract (-)":
        result = num1 - num2
    elif operation == "Multiply (*)":
        result = num1 * num2
    elif operation == "Divide (/)":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Cannot divide by zero!"

    st.divider()
    if isinstance(result, str):
        st.error(result)
    else:
        st.success(f"Result: **{result}**")