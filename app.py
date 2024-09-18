import streamlit as st

st.title('Basic Calculator')

# Taking inputs from the user
num1 = st.number_input("Enter the first number", step=1e-5)
num2 = st.number_input("Enter the second number", step=1e-5)

operation = st.selectbox("Choose an operation", ['Addition', 'Subtraction', 'Multiplication', 'Division'])

if st.button("Calculate"):
    if operation == 'Addition':
        result = num1 + num2
        st.write(f"The result is {result}")
    elif operation == 'Subtraction':
        result = num1 - num2
        st.write(f"The result is {result}")
    elif operation == 'Multiplication':
        result = num1 * num2
        st.write(f"The result is {result}")
    elif operation == 'Division':
        if num2 != 0:
            result = num1 / num2
            st.write(f"The result is {result}")
        else:
            st.write("Error! Cannot divide by zero.")


