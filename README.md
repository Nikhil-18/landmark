# Sales Dashboard

## Overview

This project is a sales dashboard built with Django and React. It provides a way to visualize stock, sales, and profit data with multiple filters. The backend uses Django to create APIs, and the frontend uses React to display data in tables and charts.

## Features

- **Django Backend**: APIs for CRUD operations on sales data.
- **React Frontend**: Dashboard with tables and charts.
- **Filters**: Multiple filters to query data.
- **Charts**: Visualization of sales and profit data.

## Setup

### Backend (Django)

1. **Clone the repository:**

    ```sh
    git clone https://github.com/Nikhil-18/ust
    cd ust
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python3 -m venv env
    source env/bin/activate
    ```

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```sh
    python manage.py migrate
    ```

5. **Load data:**
    Update file paths in `backend/api/management/commands/load_into_db.py` to point to your csv files. Please note that the project only uses the first 100 rows from the csv. More data cleaning and processing is required to use all available data.

    ```sh
    python manage.py load_into_db
    ```

6. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

### Frontend (React)

1. **Navigate to the frontend directory:**

    ```sh
    cd frontend
    ```

2. **Install dependencies:**

    ```sh
    npm install
    ```

3. **Start the development server:**

    ```sh
    npm start
    ```

## Project Structure

### Backend

- **models.py**: Defines the models for stores, items, vendors, categories, and sales.
- **serializers.py**: Serializes the models to JSON format for the API using DRF.
- **views.py**: Contains the API views for handling CRUD operations.
- **urls.py**: Maps URLs to views.

### Frontend

- **components**:
  - **Dashboard.js**: Main component to display sales data in a table and chart.
  - **Filters.js**: Component to filter sales data.
  - **SalesChart.js**: Component to render the sales chart.

- **services**:
  - **api.js**: Contains functions to make API calls.

## Design Patterns

### Backend

- **Model-View-Template (MVT)**: Standard Django design pattern.
- **Class-Based Views**: Used for handling HTTP requests in a modular way.
- **Serializers**: Used to convert querysets to JSON.

### Frontend

- **Component-Based Architecture**: React components are used to create a modular and reusable UI.
- **State Management**: `useState` and `useEffect` hooks are used to manage state and side effects.
- **API Integration**: Axios is used to make HTTP requests to the Django backend.

## Assumptions

- **Data Relationships**: Assumes specific relationships between stores, items, vendors, categories, and sales.
- **Data Availability**: Assumes that the data is loaded from the given csv file.

## Usage

1. **Start both backend and frontend servers.**
2. **Access the dashboard**: Open your browser and go to `http://localhost:3000`.
3. **Filter data**: Use the filters to query sales data based on store, category, vendor, etc.
4. **View Charts**: See the sales and profit data visualized in the chart below the table.

## Other notes

1. Please note that this project has no auth implementation.
2. The project only uses the first 100 rows from the csv. More data cleaning and processing is required to use all available data.

