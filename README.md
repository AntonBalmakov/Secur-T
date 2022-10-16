# Secur-T
Test task
Запуск: python manage.py makemigrations/migrate/runserver
docker:
- docker-compose up -d --build
- docker-compose exec app python manage.py createsuperuser


Функционал: 
- Регистрация Aвторизация пользователей по токену djoser/jwt/SMTP
- Crud постов 
- Crud комментариев
- /auth/users/
- /api/v1/post/ - Все посты 
- /api/v1/post/id/ - Детальный пост с комментариями
- /api/v1/comment/ - Создание коментариев
- /api/v1/comment/id/ - Детальный коментарий
