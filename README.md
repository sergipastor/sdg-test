# SDG Technical Test: Country API

A Django REST Framework application for retrieving and storing country information using an external REST Countries API.

### Author: Sergi Pastor

## Relevant remarks

- In addition to the country name and the population, the `iso_code` is added to the Country table. This is done to store an additional key that can be really useful for future developments.
- A simple database is already provided with some country data in `django_project/db.sqlite3`.

## Setup

### Local

1. Clone repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```bash
   cd django_project
   python manage.py migrate
   ```
4. Start server:
   ```bash
   python manage.py runserver
   ```

### Docker

1. Build image:

   ```bash
   make build
   ```

2. Run application:

   ```bash
   make run
   ```

3. Stop application:

   ```bash
   make stop
   ```

4. Run tests:

   ```bash
   make test
   ```

5. Clean:
   ```bash
   make clean
   ```

## API Endpoints

- GET `/api/v1/data/country/`: List all countries
- POST `/api/v1/data/country/`: Add or update the country specified.

  Request body:

  ```json
  {
    "name": "Spain"
  }
  ```
