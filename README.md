# We Go Trip 🌍


Техническое задание: https://docs.google.com/document/u/0/d/1aoWCmX5s5JjP8mhbbsNbX1ffhdKKMGx-08hnQVCxAqE/mobilebasic?pli=1
-

### Примечание ###
* По адресу _api/v1/swagger_ доступна документация к API
* При попытке выполнить запрос к удаленному API (пункт 3) возникала ошибка 404 (The URL was deleted manually, or expired automatically.), поэтому фрагмент кода отвечающий за обработку полученного ответа закомментирован

### Установка ###
Для установки проекта необходимо выполнить следующие команды
```
git clone https://github.com/g-ionov/we-go-trip.git
cd we-go-trip
docker-compose build
docker-compose up
```
При первом запуске необходимо выполнить следующие команды
```
docker-compose run --rm web-app sh -c "python manage.py makemigrations"
docker-compose run --rm web-app sh -c "python manage.py migrate"
docker-compose run --rm web-app sh -c "python manage.py loaddata status.json"
docker-compose run --rm web-app sh -c "python manage.py createsuperuser"
```
Для того, чтобы не прописывать такие длиные команды, можно воспользоваться терминалом сервиса web-app внутри Docker Desctop.
В таком случае команды будут выглядеть следующим образом:
```
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata status.json
python manage.py createsuperuser
```
