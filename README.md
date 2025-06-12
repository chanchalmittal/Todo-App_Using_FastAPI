# Todo App Using FastAPI

A minimal, full-featured Todo application built with [FastAPI](https://fastapi.tiangolo.com/), designed to demonstrate modern Python API development. This app lets users create, read, update, and delete (CRUD) todo tasks, providing a simple backend service that can be easily extended or used as a learning example.

## Features

- **FastAPI Backend**: High-performance Python API using FastAPI.
- **CRUD Operations**: Create, retrieve, update, and delete todos.
- **Asynchronous Endpoints**: Efficient non-blocking operations.
- **Validation**: Strong request/response validation using Pydantic models.
- **Interactive API Docs**: Built-in Swagger UI and ReDoc documentation.
- **Easy to Extend**: Simple codebase for learning or adding features.

## Getting Started

### Prerequisites

- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/)

### Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/chanchalmittal/Todo-App_Using_FastAPI.git
   cd Todo-App_Using_FastAPI
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the App

```bash
uvicorn main:app --reload
```

- The API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Interactive documentation: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Usage

You can use the built-in documentation to test the endpoints, or use tools like `curl`, [HTTPie](https://httpie.io/), or [Postman](https://www.postman.com/).

### Example Endpoints

- `GET /todos/` – List all todos
- `POST /todos/` – Create a new todo
- `GET /todos/{id}` – Get a todo by ID
- `PUT /todos/{id}` – Update a todo
- `DELETE /todos/{id}` – Delete a todo

## Project Structure

```
.
├── main.py              # FastAPI application entry point
├── models.py            # Pydantic models and DB schemas
├── crud.py              # CRUD utility functions
├── requirements.txt     # Python dependencies
└── README.md
```

## Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repo
2. Create your feature branch: `git checkout -b my-feature`
3. Commit your changes: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin my-feature`
5. Open a pull request

## License

This project is licensed under the [MIT License](LICENSE).

---

Built with ❤️ using FastAPI.
