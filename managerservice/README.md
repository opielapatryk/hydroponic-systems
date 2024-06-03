# Manager Service

This Django-based service serves as a system manager, providing APIs for managing systems. It includes endpoints for system management, API schema documentation with Swagger, and listeners for processing system measurement data.

## Features

- **APIs for managing systems.**
- **API schema documentation with Swagger.**
- **Listeners for processing system measurement data from RabbitMQ.**
- **Automatic population of fake data for systems and measurements.**

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/opielapatryk/hydroponic-systems
    cd managerservice
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```


4. **Apply migrations:**
    ```bash
    python src/manage.py makemigrations
    python src/manage.py migrate
    ```

5. **Run the RabbitMQ server:**
    Make sure RabbitMQ server is running and configured properly.

6. **Run the management command to start the RabbitMQ listener:**
    ```bash
    python src/manage.py launch_queue_listener
    ```

## API Endpoints

### Authentication

- **Before using API you need to generate access token using AuthService, then pass access token with "Bearer" prefix**

### System Management Endpoints

- **View systems, create, update, and delete systems:**
  ```
  GET /api/v1/system/
  POST /api/v1/system/
  PUT /api/v1/system/{system_id}/
  DELETE /api/v1/system/{system_id}/
  ```


### Schema Documentation

- **Swagger UI**: View the API schema and interact with the endpoints.
  ```
  GET /api/v1/schema/system
  ```
  
### Filtering, sorting, pagination

- **Filtering**
  ```
  GET /api/v1/system/?system_type=NFT
  ```

- **Sorting**
  ```
  GET /api/v1/system/?ordering=-capacity
  ```

- **Pagination**
  ```
  GET /api/v1/system/?page=1
  ```

## Management Commands

### Populate Systems

This command populates the System model with fake data.

```bash
python manage.py populate_systems
```

### Populate Measurements

This command generates and saves a specified number of fake Measurement entries to the database.

```bash
python manage.py populate_measurements
```

### Start RabbitMQ Listener

This command launches a RabbitMQ listener for processing measurement messages.

```bash
python src/manage.py launch_queue_listener
```