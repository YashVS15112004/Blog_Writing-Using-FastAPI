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
<pre> 📂 <b>Blog_Writing-Using-FastAPI/</b> <br>
  ├── 📄 <b>main.py</b> → App entry point <br>
  ├── 📄 <b>database.py</b> → DB connection and session management <br>
  ├── 📄 <b>models.py</b> → SQLAlchemy ORM models <br>
  ├── 📄 <b>schemas.py</b> → Pydantic data validation models <br>
  ├── 📄 <b>hashing.py</b> → Password hashing using bcrypt <br>
  ├── 📄 <b>jwt_token.py</b> → JWT access token generation <br>
  ├── 📄 <b>oauth2.py</b> → Authentication and user verification <br>
  ├── 📁 <b>routers/</b> → FastAPI route definitions <br>
  ├── 📁 <b>repository/</b> → DB access and business logic <br>
  ├── 📄 <b>blog.db</b> → SQLite database file <br>
  ├── 📄 <b>requirements.txt</b> → List of Python dependencies <br>
  └── 📄 <b>.gitignore</b> → Ignored files and folders for Git </pre> <br>

## 🛠️ Setup Instructions
### 1. Clone the Repository
```
git clone https://github.com/YashVS15112004/Blog_Writing-Using-FastAPI.git
cd Blog_Writing-Using-FastAPI
```
### 2. Create and Activate Virtual Environment
You can use a shared .venv outside this folder, or create one here: <br>
python -m venv .venv <br>
.venv\Scripts\activate  # On Windows <br>
# or
source .venv/bin/activate  # On macOS/Linux

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Running the Application
Start the FastAPI server using Uvicorn: <br>
uvicorn main:app --reload <br>
Now, open your browser and visit: <br>
Swagger UI: http://127.0.0.1:8000/docs <br>
ReDoc: http://127.0.0.1:8000/redoc
