🔐 Django JWT Login System with HTML
A simple Django project using JWT (JSON Web Tokens) for authentication with HTML login form and DRF for API protection. No frontend frameworks needed.

✨ Features
🧾 Username & password login via HTML

🔐 JWT-based token authentication using SimpleJWT

🧠 Authenticated home page

🔒 Protected API endpoint

📦 Pure Django, DRF, and JavaScript (no React/Vue)

📦 Tech Stack
Django

Django REST Framework

djangorestframework-simplejwt

HTML + JavaScript

🚀 Setup Instructions
1️⃣ Clone the repo
bash
Copy
Edit
git clone https://github.com/nav380/jwtlogin
cd django-jwt-login
2️⃣ Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
If you don't have a requirements.txt, install manually:

bash
Copy
Edit
pip install django djangorestframework djangorestframework-simplejwt
3️⃣ Run migrations and create superuser
bash
Copy
Edit
python manage.py migrate
python manage.py createsuperuser
4️⃣ Run the server
bash
Copy
Edit
python manage.py runserver
🧪 How It Works
🔐 Login (HTML)
Open http://localhost:8000

Enter username & password

On success, JWT token is saved in localStorage

Redirects to /home/

🔒 Protected API
Visit /home/ and click the "Call Protected API" button — it calls /api/hello/ using the JWT token.

📁 Project Structure
bash
Copy
Edit
jwtlogin/
├── jwtlogin/        # Project settings
├── accounts/        # App with views and URLs
├── templates/       # login.html and home.html
├── manage.py
🔐 JWT Endpoints
Endpoint	Description
POST /api/token/	Get access & refresh tokens
GET /api/hello/	Protected view (JWT required)

🔧 Token Example
Login Request

json
Copy
Edit
POST /api/token/
{
  "username": "admin",
  "password": "admin123"
}
Authorization Header for Protected APIs

makefile
Copy
Edit
Authorization: Bearer <access_token>
📜 License
MIT License

👨‍💻 Author
Made by [Your Name]

Feel free to contribute, fork, or suggest improvements!

Let me know if you want:

A ready requirements.txt

GitHub repository boilerplate

Token expiration/refresh demo

I’ll generate those instantly.
