# Calorie Counter (Django & PostgreSQL)

## Project Overview
This project is a simple web application built using the **Django** framework and **PostgreSQL** database to track daily calorie consumption.

### Core Features (CRUD)
* **Create (C):** Users can add new food items with their calorie count.
* **Read (R):** Displays all food items consumed today and calculates the **Total Calories**.
* **Delete (D):** Users can remove individual food items from the list.
* **Reset:** Users can delete all entries for the current day.

### Technologies Used
* **Backend:** Python, Django
* **Database:** PostgreSQL
* **Frontend/Styling:** HTML, Tailwind CSS (via CDN)
* **Dependency Management:** Pip

## Local Setup and Installation

1.  **Clone the Repository:**
    ```bash
    git clone [YOUR GITHUB REPO URL]
    cd calorie_counter_project
    ```
2.  **Create and Activate Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS or MINGW64
    # .\\venv\\Scripts\\activate  # On Windows PowerShell/CMD
    ```
3.  **Install Dependencies:**
    ```bash
    # Note: Requires Microsoft C++ Build Tools on Windows for psycopg2 compilation.
    pip install django psycopg2-binary django-widget-tweaks
    ```
4.  **Database Configuration:**
    Ensure PostgreSQL is running and update `calorie_counter_project/settings.py` with your database credentials.

5.  **Run Migrations:**
    ```bash
    python manage.py makemigrations calorie_tracker
    python manage.py migrate
    ```
6.  **Run Server:**
    ```bash
    python manage.py runserver
    ```
    Access the app at `http://127.0.0.1:8000/`.