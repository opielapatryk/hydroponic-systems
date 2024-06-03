# Measurements Service

This Django-based service provides APIs for managing measurements. It includes endpoints for viewing, creating, updating, and deleting measurement instances, along with API schema documentation using Swagger.

## Features

- **APIs for managing measurements.**
- **API schema documentation with Swagger.**
- **Automatic creation of fake measurement data.**

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/opielapatryk/hydroponic-systems
    cd measurementservice
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

5. **Populate fake measurement data:**
    ```bash
    python src/manage.py populate_measurements
    ```

## API Endpoints

### Measurement Endpoints

- **View measurements, create, update, and delete measurements:**
  ```
  GET /api/v1/measurement/
  POST /api/v1/measurement/
  PUT /api/v1/measurement/{measurement_id}/
  PATCH /api/v1/measurement/{measurement_id}/
  DELETE /api/v1/measurement/{measurement_id}/
  ```

### Schema Documentation

- **Swagger UI**: View the API schema and interact with the endpoints.
  ```
  GET /api/v1/schema/measurement
  ```


## Management Commands

### Populate Measurements

This command generates and saves a specified number of fake Measurement entries to the database.

```bash
python manage.py populate_measurements
```