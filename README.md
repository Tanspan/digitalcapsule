# CapsuleConnect - Digital Time Capsule

A simple web application where users can write messages, lock them with a future date, and read them only after that date arrives. Like a letter to your future self.

---

## What it does

- Register and login to your account
- Write a message and set a future unlock date
- Capsule stays locked and blurred until that date
- Once unlocked, click View to read your message
- Countdown timer shows how long until each capsule unlocks

---

## Technologies Used

- HTML, Bootstrap 5
- CSS
- JavaScript, jQuery
- Python, Flask
- MySQL
- Jinja2

---

## Project Structure

- app.py
- requirements.txt
- static/
  - style.css
  - main.js
- templates/
  - login.html
  - register.html
  - home.html

---

## Routes

- / - Redirects to login or home
- /register - Register page
- /login - Login page
- /logout - Logout
- /home - Dashboard with create form and capsules
- /submit - Handles capsule form submission

---

## Setup

**Step 1 - Install requirements**

```
pip install -r requirements.txt
```

**Step 2 - Setup database**

Open MySQL and paste the contents of schema.sql

**Step 3 - Update password**

Open app.py and change yourpassword on line 6 to your MySQL password

**Step 4 - Run**

```
python app.py
```

**Step 5 - Open browser**

```
http://127.0.0.1:5000
```

---

## Developer

- Name - Tanusri
- Branch - CSE 3rd Year
- GitHub - https://github.com/tanspan
