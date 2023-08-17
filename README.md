# IntegraSolutions

IntegraSolutions is a data validation software project that consists of both a backend (built with Flask) and a frontend (built with Vue.js). It provides data validation functionalities to ensure data integrity and accuracy.

## Table of Contents

- [Technologies Used](#technologies-used)
  - [Backend](#backend)
  - [Frontend](#frontend)
- [Getting Started](#getting-started)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Usage](#usage)

## Technologies Used

### Frontend

- Vue.js 3: A progressive JavaScript framework for building user interfaces.
- Vite: A fast build tool and development server for modern web projects.
- Bootstrap: A popular front-end component library for responsive and mobile-first web development.
- axios: A promise-based HTTP client for making API requests.
- vue-pdf-embed: A Vue.js component for embedding PDF files.

### Backend

- Python: A versatile programming language used for backend development.
- Flask 2: A micro web framework written in Python for building web applications.
- PyPDF2: A Python library for working with PDF files.

## Getting Started

To run the IntegraSolutions project, follow the setup instructions below for both the backend and frontend parts.

### Backend Setup

1. Navigate to the `backend` folder:

   ```bash
   cd backend
   ```

2. Create and activate a virtual environment using Pipenv:

   ```bash
   cd backend
   pipenv shell
   ```

3. Install the backend dependencies using Pipenv:

   ````bash
   pipenv install -r requirements.txt
   ```

   ````

4. Run Flask Application:
   ```bash
   python main.py
   ```

### Frontend Setup

1. Navigate to the `frontend` folder:
   ```bash
   cd frontend
   npm install
   npm run dev
   ```
2. Install the frontend dependencies using npm:

   ```bash
   npm install
   ```

3. Run the Vue.js development server:

   ```bash
   npm run dev
   ```

### Usage

Once both the backend and frontend are set up and running, you can access the IntegraSolutions data validation software through your web browser. Open your browser and navigate to http://localhost:5173 to interact with the frontend user interface.

The backend Flask application provides the necessary APIs for data validation. You can make API requests to the backend server from your Vue.js frontend.
