
# 📘 Employee & Book Management API - Django REST Framework

This project is a RESTful web service developed using **Django** and **Django REST Framework (DRF)**.  
It provides APIs for managing **Employee records** and **Books**, including full CRUD operations. The APIs are easily testable via **Postman**.

---

## 🔧 Tech Stack

- **Backend**: Django, Django REST Framework (DRF)
- **Database**: SQLite (default; can be switched to PostgreSQL or MySQL)
- **API Testing**: Postman
- **Language**: Python 3.x

---

## 📁 Project Structure

```
emp_management/
├── emp_management/      # Project settings
│   ├── settings.py
│   └── urls.py
├── employee/            # Employee app (REST API)
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
├── book/                # Book app (REST API)
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
├── manage.py
└── requirements.txt
```

---

## ✨ Features

### ✅ Employee Management
- Create, read, update, delete employee records
- Employee model: `name`, `email`, `position`

### ✅ Book Management
- Create, read, update, delete book records
- Book model: `title`, `author`, `isbn`

### 🔐 Authentication (Optional – extendable)
- Currently open access (ideal for demo)
- Can be extended using DRF Token/Auth/JWT

---

## 🔗 API Endpoints

### 👨‍💼 Employee API
| Method | Endpoint              | Description               |
|--------|-----------------------|---------------------------|
| GET    | `/api/employees/`     | List all employees        |
| POST   | `/api/employees/`     | Add a new employee        |
| GET    | `/api/employees/<id>/`| Retrieve employee details |
| PUT    | `/api/employees/<id>/`| Update employee info      |
| DELETE | `/api/employees/<id>/`| Delete an employee        |

### 📚 Book API
| Method | Endpoint           | Description         |
|--------|--------------------|---------------------|
| GET    | `/api/books/`      | List all books      |
| POST   | `/api/books/`      | Add a new book      |
| GET    | `/api/books/<id>/` | Retrieve book info  |
| PUT    | `/api/books/<id>/` | Update book info    |
| DELETE | `/api/books/<id>/` | Delete a book       |

---

## 📦 Sample JSON Requests

### ➕ Create Employee

```json
{
  "name": "Alice Smith",
  "email": "alice@example.com",
  "position": "HR Manager"
}
```

### ➕ Create Book

```json
{
  "title": "Python Crash Course",
  "author": "Eric Matthes",
  "isbn": "9781593279288"
}
```

---

## ▶️ How to Run Locally

```bash
git clone https://github.com/yourusername/emp-book-api.git
cd emp-book-api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

Access API:
- Employees: `http://127.0.0.1:8000/api/employees/`
- Books: `http://127.0.0.1:8000/api/books/`

---

## 🧪 Postman Usage

- Use Postman to make GET, POST, PUT, DELETE requests.
- Set `Content-Type: application/json` in headers.
- Import `postman_collection.json` (if provided) to simplify testing.

---

## 📌 Future Enhancements

- JWT Authentication
- Pagination and filtering
- Search functionality
- Swagger/OpenAPI documentation
- Frontend integration (React/Vue/Angular)

---

## 🤝 Contributing

1. Fork the repo
2. Create a new branch (`git checkout -b feature/XYZ`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push and create a Pull Request

---

## 📄 License

This project is open-source and free to use under the MIT License.

