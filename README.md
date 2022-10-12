Проект REST API для проекта Yatube.
Описание: Yatube это социальная сеть. Она дает пользователям возможность создавать учетную запись, публиковать записи и подписываться на любимых авторов. Мы создали REST API для Yatube. Через этот интерфейс могут работать мобильное приложение или чат-бот; через него же можно передавать данные в любое приложение или на фронтенд.

Возможности: Просматривать, создавать новые, удалять и изменять посты. Просматривать и создавать группы. Комментировать, смотреть, удалять и обновлять комментарии. Выполнять поиск по полям. Подписываться на пользователя.

Как запустить проект:
Установка Python 3.7 и подготовка окружения Установите программное обеспечение: скачайте установочные файлы и запустите их. Python: www.python.org/downloads/ устанавливаем Python 3.7 Visual Studio Code: code.visualstudio.com/download Git: git-scm.com/download/win

Запустить Git Bash
Клонировать репозиторий и перейти в него в командной строке Git Bash:
git clone git@github.com:ma9or/api_yatube.git


cd api_final_yatube

Cоздать и активировать виртуальное окружение:
на Mac или Linux:
python3 -m venv env
source env/bin/activate
для Windows:
python -m venv venv
source venv/Scripts/activate
Обновляем pip на Mac или Linux: python3 -m pip install --upgrade pip для Windows: python -m pip install --upgrade pip


Установить зависимости из файла requirements.txt:
pip install -r requirements.txt
Выполнить миграции:

на Mac или Linux: python3 manage.py migrate для Windows: python manage.py migrate


Запустить проект:
на Mac или Linux:
python3 manage.py runserver
для Windows:
python manage.py runserver
Документация к API проекта Yatube:
по адресу http://127.0.0.1:8000/redoc/ будет доступна документация для API Yatube

api/v1/posts/ (GET, POST) GET: Получить список всех публикаций. При указании параметров limit и offset выдача должна работать с пагинацией. { "count": 123, "next": "http://api.example.org/accounts/?offset=400&limit=100", "previous": "http://api.example.org/accounts/?offset=200&limit=100", "results": [ { "id": 0, "author": "string", "text": "string", "pub_date": "2021-10-14T20:41:29.648Z", "image": "string", "group": 0 } ] }

POST: Добавление новой публикации в коллекцию публикаций. Анонимные запросы запрещены. { "text": "string", "image": "string", "group": 0 }

api/v1/posts/{id}/ (GET, PUT, PATCH, DELETE) GET: Получение публикации по id. { "id": 0, "author": "string", "text": "string", "pub_date": "2019-08-24T14:15:22Z", "image": "string", "group": 0 } PUT: Обновление публикации по id. Обновить публикацию может только автор публикации. Анонимные запросы запрещены. { "text": "string", "image": "string", "group": 0 } PATCH: Частичное обновление публикации по id. Обновить публикацию может только автор публикации. Анонимные запросы запрещены. { "text": "string", "image": "string", "group": 0 } DEL: Удаление публикации по id. Удалить публикацию может только автор публикации. Анонимные запросы запрещены. { "detail": "Учетные данные не были предоставлены." }

api/v1/posts/{post_id}/comments/ (GET, POST) GET: Получение всех комментариев к публикации. [ { "id": 0, "author": "string", "text": "string", "created": "2019-08-24T14:15:22Z", "post": 0 } ] POST: Добавление нового комментария к публикации. Анонимные запросы запрещены. { "text": "string" }

api/v1/posts/{post_id}/comments/{id}/ (GET, PUT, PATCH, DELETE) GET: Получение комментария к публикации по id. { "id": 0, "author": "string", "text": "string", "created": "2019-08-24T14:15:22Z", "post": 0 } PUT: Обновление комментария к публикации по id. Обновить комментарий может только автор комментария. Анонимные запросы запрещены. { "text": "string" } PATCH: Частичное обновление комментария к публикации по id. Обновить комментарий может только автор комментария. Анонимные запросы запрещены. { "text": "string" } DEL: Удаление комментария к публикации по id. Обновить комментарий может только автор комментария. Анонимные запросы запрещены. { "detail": "Учетные данные не были предоставлены." }

api/v1/groups/ (GET) GET: Получение списка доступных сообществ. [ { "id": 0, "title": "string", "slug": "string", "description": "string" } ]

api/v1/groups/{id}/ (GET) GET: Получение информации о сообществе по id. { "id": 0, "title": "string", "slug": "string", "description": "string" }

api/v1/follow/ (GET, POST) GET: Возвращает все подписки пользователя, сделавшего запрос. Анонимные запросы запрещены. [ { "user": "string", "following": "string" } ] POST: Подписка пользователя от имени которого сделан запрос на пользователя переданного в теле запроса. Анонимные запросы запрещены. { "following": "string" }

api/v1/jwt/create/ (POST) POST: Получение JWT-токена. { "username": "string", "password": "string" }

api/v1/jwt/refresh/ (POST) POST: Обновить JWT-токен { "refresh": "string" }

api/v1/jwt/verify/ (POST) POST: Проверка JWT-токена. { "token": "string" }

Примеры запросов Пример POST-запроса с токеном Антона Чехова: добавление нового поста. POST .../api/v1/posts/ { "text": "Вечером собрались в редакции «Русской мысли», чтобы поговорить о народном театре. Проект Шехтеля всем нравится.", "group": 1 } Пример ответа: { "id": 14, "text": "Вечером собрались в редакции «Русской мысли», чтобы поговорить о народном театре. Проект Шехтеля всем нравится.", "author": "anton", "image": null, "group": 1, "pub_date": "2021-06-01T08:47:11.084589Z" } Пример POST-запроса с токеном Антона Чехова: отправляем новый комментарий к посту с id=14. POST .../api/v1/posts/14/comments/ { "text": "тест тест" } Пример ответа: { "id": 4, "author": "anton", "post": 14, "text": "тест тест", "created": "2021-06-01T10:14:51.388932Z" } Пример GET-запроса с токеном Антона Чехова: получаем информацию о группе. GET .../api/v1/groups/2/ Пример ответа: { "id": 2, "title": "Математика", "slug": "math", "description": "Посты на тему математики" }
