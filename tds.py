!pip install streamlit
import streamlit as st

def find_largest(num1, num2, num3):
    largest = max(num1, num2, num3)
    return largest

st.title("Find the largest among 3 numbers")
st.write("Enter three numbers and click the button to find the largest among them")

num1 = st.number_input("Enter the first number", value=0, step=1)
num2 = st.number_input("Enter the second number", value=0, step=1)
num3 = st.number_input("Enter the third number", value=0, step=1)

if st.button("Find largest"):
    result = find_largest(num1, num2, num3)
    st.write(f"The largest among {num1}, {num2}, {num3} is {result}")
