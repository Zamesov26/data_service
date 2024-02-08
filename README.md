# Quizzes for the lesson

Проект предназначен для лучшего запоминания материалов уроков

Приложение будет связанно с сервисом Telegram-bot через который будет проводить тестирование

Также  для комфортной работы учителя/администратора/модератора

## Установка
### Добавление переменных окружения
Создать в корне основной .env, и для тестирования .test.env в которых должны присутствовать следующие поля

Пример:
```dotenv
# режим работы
MODE=TEST

# Подключение к postgres
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASS=postgres
DB_NAME=test_quiz_db
```
MODE - может принимать следующие параметры `['TEST', 'DEV', 'PROD']`

### Установка зависимостей
#### Для запуска
...
#### Для разработки
...

## Запуск
```bash
uvicorn app.main:app [--reload]
```

## Список функций
### User
- Создание пользователя
- Прикрепление добавление к пользователю вопросов к уроку

### Quize
- Создание вопроса(один из многих/несколько из многих/текстовый ответ)
  - Добавление вариантов ответов к нему

### Lesson
- Создание урока
  - Добавление Quizzes к нему
- Получение списка уроков
  - Получение списков вопросов к уроку