## Technologies Used

- Python
- Django
- Docker
- Xlxswriter
- Django Rest Framework
- Selenium
- SQLite
- Chrome Driver

## Endpoints

- /api/countries - return the list of countries
- /api/sectors - return the list of sectors
- /api/loans - return the list of loans (basically that table but in JSON format)

## Instructions To Follow

1. Clone the project
2. cd into the project
2. Download and install docker on either mac os or windows
3. Follow the next command in the terminal

## Running Docker Compose

```
docker-compose up --build
```

## Running migrations

Open a new terminal and run:

```
docker-compose run <docker-dir-name> python manage.py makemigrations
docker-compose run <docker-dir-name> python manage.py migrate
```

## Scrape the site information using this command

```
docker-compose run <docker-dir-name> python api.py
```

HAPPY CODING (^^)



# Task Tracker

This is a Task Tracker application built with ReactJS, using Tailwind CSS for styling. It allows users to add, delete, and track tasks. The project follows a component-based architecture, with Redux state management.

## Table of Contents
- [Features](#features)
- [Folder Structure](#folder-structure)
- [Installation](#installation)
- [Running the App](#running-the-app)
- [Usage](#usage)
- [Built With](#built-with)

## Features
- Add new tasks with custom details.
- Mark tasks as completed or pending.
- Remove tasks from the list.
- Toggle between dark and light themes.

## Folder Structure
The main folders and files are structured as follows:

```plaintext
task-tracker/
├── public/
│   ├── favicon.ico
│   ├── index.html
│   ├── logo192.png
│   ├── logo512.png
│   └── manifest.json
├── src/
│   ├── assets/
│   │   ├── dark.png
│   │   ├── light.png
│   │   └── header.json
│   ├── components/
│   │   ├── ui/
│   │   │   ├── Button.jsx
│   │   │   ├── DarkButton.jsx
│   │   │   ├── LightButton.jsx
│   │   ├── TaskForm.jsx
│   │   ├── TaskItem.jsx
│   │   └── TaskList.jsx
│   ├── store/
│   │   ├── index.js
│   │   └── reducer.js
│   ├── App.css
│   ├── App.js
│   ├── index.css
│   ├── index.js
│   └── reportWebVitals.js
├── .gitignore
├── package.json
├── README.md
└── tailwind.config.js
```

## Installation

### Prerequisites
Ensure you have Node.js and npm installed on your machine. You can check the installation by running:

```bash
node -v
npm -v
```

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/task-tracker.git
   cd task-tracker
   ```

2. **Install Dependencies**
   ```bash
   npm install
   ```

3. **Configure Tailwind CSS**
   Make sure `tailwind.config.js` is configured as required for your project setup. The setup should be compatible with React by following Tailwind's React setup guide.

## Running the App

To start the development server, run:

```bash
npm start
```

This will start the app locally, and you can view it in the browser at `http://localhost:3000`.

### Additional Scripts
- **Build the app**: `npm run build` - Compiles the app for production in the `build` folder.
- **Run tests**: `npm test` - Launches the test runner.
- **Linting and formatting**: (Optional based on ESLint and Prettier setup)

## Usage
1. **Add Task**: Enter task details in the provided form and click the 'Add Task' button.
2. **Delete Task**: Click the delete icon next to each task to remove it.
3. **Toggle Dark Mode**: Click on the dark/light button in the UI to switch between themes.

## Built With
- [React](https://reactjs.org/) - A JavaScript library for building user interfaces.
- [Tailwind CSS](https://tailwindcss.com/) - A utility-first CSS framework.
- [Redux](https://redux.js.org/) - A predictable state container for JavaScript apps.

---

Feel free to customize this README as per your project’s specific features and functionality!
