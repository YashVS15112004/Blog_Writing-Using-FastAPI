# 📝 Blog Writing API using FastAPI
A lightweight and secure blog writing backend built using **FastAPI**, with JWT-based authentication, SQLite database, and modular routing.
## 🚀 Features
- ✅ CRUD operations for blog posts
- 🔐 User registration and login with JWT authentication
- 🔑 Password hashing using bcrypt (`passlib`)
- 📦 SQLite database using SQLAlchemy ORM
- 📁 Clean project structure with modular routers and repository pattern
- 🧪 Auto-generated Swagger UI for API testing
---
## 📁 Project Structure
Blog_Writing-Using-FastAPI/
│
├── main.py # App entry point
├── database.py # DB connection and session
├── models.py # SQLAlchemy models
├── schemas.py # Pydantic models
├── hashing.py # Password hashing
├── jwt_token.py # JWT generation
├── oauth2.py # Authentication logic
├── routers/ # API route handlers
├── repository/ # DB query functions
├── blog.db # SQLite database file
├── requirements.txt # Project dependencies
└── .gitignore # Git ignore rules

## 🛠️ Setup Instructions
### 1. Clone the Repository
```
git clone https://github.com/YashVS15112004/Blog_Writing-Using-FastAPI.git
cd Blog_Writing-Using-FastAPI
```
### 2. Create and Activate Virtual Environment
You can use a shared .venv outside this folder, or create one here:
python -m venv .venv
.venv\Scripts\activate  # On Windows
# or
source .venv/bin/activate  # On macOS/Linux

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Running the Application
Start the FastAPI server using Uvicorn:
uvicorn main:app --reload
Now, open your browser and visit:
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
