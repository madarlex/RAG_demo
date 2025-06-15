# AIJ Vector Database & RAG Demo

This project demonstrates how to create and use a vector database for document retrieval and Retrieval-Augmented Generation (RAG) using Python notebooks and a Django web demo. It uses lightweight models from HuggingFace for demonstration.

---

## Project Structure

```
chat_demo/                    # Django web demo for live chat with RAG backend
```

---

## Getting Started

### 1. Prepare the Environment

- Install Python 3.12.
- (Recommended) Create a virtual environment:
  ```sh
  python -m venv .venv
  source .venv/bin/activate
  ```
- Install dependencies:
  ```sh
  pip install -r requirements.txt
  ```

### 2. Run the Django Web Demo

- Navigate to the Django project directory:
  ```sh
  cd chat_demo
  ```
- Apply migrations:
  ```sh
  python manage.py migrate
  ```
- Start the development server:
  ```sh
  python manage.py runserver
  ```
- Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access the live chat demo.