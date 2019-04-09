# django2-app

Bootstrap configuration for launching django projects

To run:

docker-compose build
docker-compose run --rm app sh -c "python manage.py runserver"

To run tests:
docker-compose run --rm app sh -c "python manage.py test && flake8"
