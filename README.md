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
2. Download and install docker on either mac os or windows
3. Follow the next command in the terminal

## Running Docker Compose

```
docker-compose up —build
```

## Running migrations

Open a new terminal and run:

```
docker-compose run <docker-image-name> python manage.py makemigrations
docker-compose run <docker-image-name> python manage.py migrate
```

## Scrape the site information using this command

```
docker-compose run <docker-image-name> python api.py
```
