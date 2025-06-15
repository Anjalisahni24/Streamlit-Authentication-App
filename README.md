# 🛡️ Streamlit Authentication App

A simple web-based authentication system built with **Streamlit**. Users can **Login**, **Register**, **View**, **Update**, or **Delete** accounts using a sidebar menu. Backend operations are handled via a `database.py` module.

---

## 📸 Features

- 🔐 **Login** with email and password
- 📝 **Register** new users
- 📄 **View** all registered users (displayed as a table)
- ✏️ **Update** user info by ID
- 🗑️ **Delete** users by ID

---

## 🧠 Tech Stack

- [Streamlit](https://streamlit.io/)
- [streamlit-option-menu](https://github.com/victoryhb/streamlit-option-menu)
- [Pandas](https://pandas.pydata.org/)
- SQLite for backend logic

---

## 🛠️ Getting Started

### 1️⃣ Clone the repository

git clone https://github.com/Anjalisahni24/Streamlit-Authentication-App.git
cd Streamlit-Authentication-App

### 2️⃣ Install dependencies

pip install -r requirements.txt

### 3️⃣ Ensure your database.py includes these functions:
check_login(data)
register(data)
view()
single_user(id)
update(data)
delete(id)
 - These functions should handle all database interactions.

### 4️⃣ Run the app
streamlit run auth_app.py

---

### 📂 Project Structure
Streamlit-Authentication-App/
│
├── auth_app.py          # Main Streamlit app
├── database.py          # DB operations (user-defined)
├── requirements.txt     # Python dependencies
└── README.md            # This file

---

### ✅ Example UI
The sidebar menu allows easy navigation:

🔹 Login

🔹 Register

🔹 View Users

🔹 Update User Info

🔹 Delete User

---

## 📬 Contact
📧 24anjalisahni@gmail.com
🔗 https://www.linkedin.com/in/anjali-sahni-481b44238/
🌐 GitHub: https://github.com/Anjalisahni24
