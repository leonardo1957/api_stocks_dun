# Stock API Project

This project is a web API developed with Django to retrieve stock data from an external API (Polygon.io) and perform additional data scraping from a financial website (MarketWatch). The API provides two main endpoints to manage and view stock information, including historical performance data and competitors.

## Project Structure

```bash
stock_api/
├── Dockerfile
├── manage.py
├── requirements.txt
├── stock_api/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── stocks/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   ├── models.py
│   ├── serializers.py
│   ├── services.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── scraping.py
└── docker-compose.yml
```

### Directory and File Descriptions

- **Dockerfile**: Configuration file for building the Docker image of the application.
- **manage.py**: Django management script.
- **requirements.txt**: List of project dependencies.
- **stock_api/**: Directory containing global Django settings.
- **stocks/**: Main application directory containing models, serializers, views, services for external API integration, scraping logic, and tests.

## Requirements

- Python 3.10 or higher
- Docker (optional, for running the application in a container)
- PostgreSQL

## Environment Setup

### 1. Clone the Repository

```bash
git clone https://github.com/leonardo1957/api_stocks_dun.git
cd api_stocks_dun
```

### 2. Configure the Database

Set up the PostgreSQL database and add the configuration in the `stock_api/settings.py` file:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 3. Install Dependencies

If running locally:

```bash
python -m venv venv
source venv/bin/activate 
pip install -r requirements.txt

(ubuntu)
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Set Environment Variables

Add the Polygon.io API key in the `stock_api/settings.py` file or use environment variables:

```python
POLYGON_API_KEY = 'bmN7i7CrzrpKqFvgbB1fEaztCwZKSUjJ'
```

### 6. Run the Application

#### Running Locally

```bash
python manage.py runserver
```

#### Running with Docker

If you prefer to run the application in a Docker container:

1. **Build the Docker Image**:

   ```bash
   docker-compose up --build
   ```


The application will be available at [http://localhost:8000](http://localhost:8000)


## Available Endpoints

- **GET /api/stock/{stock_symbol}/YYYY-mm-dd**: Returns the data for a specific stock
- **POST /api/stock/{stock_symbol}**: Updates the purchased amount for the specified stock symbol