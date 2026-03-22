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
## Screenshots

<img width="692" height="643" alt="Screenshot 2026-03-22 204519" src="https://github.com/user-attachments/assets/55e405c7-84c8-4d9c-ae2d-e8ed34742d82" />
<img width="1886" height="1009" alt="Screenshot 2026-03-22 204533" src="https://github.com/user-attachments/assets/68804f56-7649-4ecf-938d-ca3b5f7131e0" />


