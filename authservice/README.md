# Authentication Service

This is a Django-based authentication service that uses JSON Web Tokens (JWT) for user authentication. The service includes endpoints for obtaining and refreshing tokens, as well as a schema view for API documentation.

## Features

- User authentication using JWT.
- Admin interface for managing users.
- API schema documentation with Swagger.
- Automatic creation of a superuser if it does not exist.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/opielapatryk/hydroponic-systems
    cd authservice
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    Create a `.env` file in the project root and add the following:
    ```plaintext
    DJANGO_SUPERUSER_USERNAME=<your-superuser-username>
    DJANGO_SUPERUSER_EMAIL=<your-superuser-email>
    DJANGO_SUPERUSER_PASSWORD=<your-superuser-password>
    ```

5. Apply the migrations:
    ```bash
    python src/manage.py migrate
    ```

6. Create the superuser:
    ```bash
    python src/manage.py create_superuser
    ```

## Running the Service

To run the development server:
```bash
python src/manage.py runserver
```

## API Endpoints

### Authentication Endpoints

- **Login**: Obtain a JWT token.
  ```
  {
    "username": "user",
    "password": "password"
  }
  POST /api/v1/auth/login/
  ```

- **Token Refresh**: Refresh the JWT token.
  ```
  POST /api/v1/auth/refresh/
  ```

### Admin Endpoints

- **Admin Interface**: Access the Django admin interface.
  ```
  GET /api/v1/auth/admin/
  ```

### Schema Documentation

- **Swagger UI**: View the API schema and interact with the endpoints.
  ```
  GET /api/v1/schema/auth
  ```