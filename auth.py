import streamlit as st
from streamlit_option_menu import option_menu
import database
import pandas as pd
st.title("Authentication")
with st.sidebar:
    selected = option_menu("Main Menu",options = ['Login','Register','View','update','Delete'], icons = ['person','person','list-task','feather','feather'])
    st.write(selected)

#conditions for login
if selected== 'Login':
    with st.form('form'):
        email = st.text_input("Email")
        password = st.text_input("Password", type='password')
        btn = st.form_submit_button("Login")
        if btn:
            if email == "" or password == "":  #if blank then throw warning
                st.warning("All Entry field must be filled !!")
            else:
                data = (email, password) 
                #st.write(data)
                response = database.check_login(data) 
                if response :
                    st.success("User Logged in Sucessfully !!")
                else:
                    st.error('Invalid Credentials')
            

if selected== 'Register':
    with st.form('register_form'):
        username = st.text_input("Username")
        email = st.text_input("Email")
        password = st.text_input("Password", type='password')
        btn = st.form_submit_button("Login")
        if btn:
            if username == "" or email == "" or password == "":
                st.warning("All entry must be filled")
            else:
                data=(username,email,password)
                #st.write(data)
                response = database.register(data)
                if response : 
                    st.success("user register successfully")
                else :
                    st.error("Invalid credential")  

if selected  == 'View':
    response = database.view()
    # st.write(response)
    data = pd.DataFrame(response, columns=['ID','Username','Email','Password']) #for table
    st.dataframe(data)

if selected == 'update':
    num1 = st.number_input("Enter number to Update :")
    single_user = database.single_user(num1)
    st.write(single_user)
    if single_user:
        username = st.text_input("Username", value=single_user[1]) #index for username is one
        email = st.text_input("Email", value=single_user[2]) #index for email is 2
        password = st.text_input("Password", value=single_user[3]) #index for password is 3
        btn = st.button("Update")
        if btn :
            data = (username, email, password, single_user[0]) #index for id is 0
            response = database.update(data)
            if response:
                st.success("User Updated Successfully !!")
            else :
                st.error("Check Data Base")

if selected == 'Delete':
    num1 = st.number_input("Enter Number :")
    btn = st.button("Delete")
    if btn :
        response = database.delete(num1)
        if response :
            st.success("User Delete Successfully !!")
        else:
            st.error("Check Database")