# URL Shortener API

A simple URL shortener built with FastAPI and Postgresql for storage.

## Features
- Shorten long URLs.
- Retrieve the original URL using a shortened URL.
- Redirect from a shortened URL to the original URL.

## Technologies Used

- **FastAPI** - For building the web API  
- **PostgreSQL** - For storing URLs  
- **SQLAlchemy** - For database operations  
- **Asynchronous Processing** - Using `async` & `await` for high performance  

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/oreElijah/Task-Manager.git
   cd Task-Manager
   ```

2. Create a virtual environment and activate it:
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Set up the database (PostgreSQL or SQLite).
## URL-shortener
| Method | Endpoint | Description |
|--------|---------|-------------|
| `POST` | `/api/v1/url/shortener` | Shortens original_url |
| `GET` | `/api/v1/url/{short_url}` | Redirects user to original url page |
| `GET`  | `/api/v1/url/get_original/{short_url}` | Get original URL |

## Usage

1. Run the FastAPI server:
   ```sh
   uvicorn main:app --reload
   ```

2. Use the following endpoints:

   - **Shorten URL**
     ```http
     POST /api/v1/shortener
     ```
     **Request Body:**
     ```json
     {
       "original_url": "https://example.com"
     }
     ```

   - **Retrieve Original URL**
     ```http
     GET /api/v1/get_original/{short_url}
     ```

   - **Redirect to Original URL**
     ```http
     GET /api/v1/{short_url}
     ```

## License

This project is licensed under the MIT License.
