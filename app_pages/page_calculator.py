import streamlit as st

def calculator_body():
    st.write("---")
    a = st.number_input("Enter a number", 0)
    b = st.number_input("Enter another number", 0)
    operation = st.selectbox("Operation", ["Add", "Subtract", "Multiply", "Divide"])
    if operation == "Add":
        result = a + b
    elif operation == "Subtract":
        result = a - b
    elif operation == "Multiply":
        result = a * b
    elif operation == "Divide":
        result = a / b
    st.write(f"Result: {result}")
    
