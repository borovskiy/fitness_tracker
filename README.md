Тестовое задание:
Создать API для мобильного приложения фитнес трекера.
Пользователь регистрируется в приложении с помощью электронной почты с подтверждением адреса.
Приложение отправляет на сервер отчёты об активности пользователя.
Отчёт содержит следующие данные:

Дата и время начала активности;
Дата и время окончания активности;
Тип активности (ходьба, бег, велосипед);
Расстояние;
Количество калорий.
Приложение может запрашивать статистику по пользовательским активностям с возможностью агрегирования за час и за сутки.
Используемые технологии: Django, Django Rest Framework, PostgreSQL.
Можно использовать любые дополнительные библиотеки по желанию.
Выложите результат на gitlab и отправьте ссылку.


Установка: Склонируйте репозиторий Создайте и войдите в вирутальное окружение 
Установите зависимости: pip install -r requirements.txt 

В settings.py в переменной DATABASES настройте свои параметры или 
создайте базу дынных на своем PostgreSQL database=fitness, user=bars, pass=1111 
ну и соответственно ip адреса и порт должен совпадать с тем что лежит в DATABASES

Так же необходимо настроить smtp на своей почте гугл (необходима почта с подтвержением по телефону)
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

Проведите миграции python manage.py makemigrations python manage.py migrate 
Создайте суперпользователя python manage.py createsuperuser 
Запустите тестовый сервер python manage.py runserver

Права доступа: Авторизованный пользователь
Права доступа: Все
url -
method -
QUERY PARAMETERS :

API

Регистрация
Права доступа: Все
url - http://127.0.0.1:8000/auth/users/
method - POST
QUERY PARAMETERS : username, password, email

Активация по ссылке
Права доступа: Все
url - http://127.0.0.1:8000/auth/users/activation/
method - POST
QUERY PARAMETERS :uid, token
QUERY PARAMETERS берем из ссылки  api/add_activ/activate_user/?uid={uid}&token={token}
хотя ссылка настроена так что при переходе пользователь просто активируется

Авторизация
Права доступа: Все
url - http://127.0.0.1:8000/auth/token/login/
method - POST
QUERY PARAMETERS : username, password,


Пользовательская часть

Добавление данных трекера
Права доступа: Авторизованный пользователь
url - http://127.0.0.1:8000/api/add_activ/
method - POST
QUERY PARAMETERS :
                    Headers
                      Authorization
                    Body
                      start_of_activity - формат для ввода 2021-08-18T13:10:27.853707Z
                      end_of_activity
                      type_active - формат для ввода   walking, running, cycling 
                      distance
                      calorie_count

Получение всех данных трекера
Права доступа: Авторизованный пользователь
url - http://127.0.0.1:8000/api/add_activ/
method - GET

Получение всех данных отдельного трэка
Права доступа: Авторизованный пользователь
url - http://127.0.0.1:8000/api/add_activ/<int:id>
method - GET

Получение Трэков за последний час
Права доступа: Авторизованный пользователь
http://127.0.0.1:8000/api/add_activ/activity_per_hour/
method - GET

Получение Трэков за сутки
Права доступа: Авторизованный пользователь
http://127.0.0.1:8000/api/add_activ/activity_per_day/
method - GET









