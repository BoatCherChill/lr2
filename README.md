# LR2 

Лабораторная работа №2: FastAPI с хранением данных в памяти (без БД) и валидацией через Pydantic.

## Стек

- Python 3.12
- FastAPI
- Pydantic v2
- Docker

## Структура проекта
```
lr2-fastapi/
├── app/
│ ├── init.py
│ ├── main.py # эндпоинты, словарь students
│ └── schemas.py # Pydantic-модели
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md
```

## Эндпоинты

| Метод | Путь | Описание | Коды ответа |
|---|---|---|---|
| POST | `/students` | Создать студента | 201, 400, 422 |
| GET | `/students` | Список всех студентов | 200 |
| GET | `/students/{id}` | Студент по id | 200, 404, 422 |
| DELETE | `/students/{id}` | Удалить студента | 204, 404, 422 |

Swagger UI: `http://localhost:8000/docs`

## Модель данных

Данные хранятся в словаре `students = {id: {...}}` в памяти процесса — **при перезапуске сервера всё теряется**.

| Поле | Тип | Ограничения |
|---|---|---|
| id | integer | генерируется сервером |
| name | string | 1–100 символов |
| email | string (email) | валидный, уникальный |

Пример запроса POST:

```json
{ "name": "Ivan", "email": "ivan@example.com" }
```
Пример ответа:

```json
{ "name": "Ivan", "email": "ivan@example.com", "id": 1 }
```
Запуск локально

```bash
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
.venv\Scripts\Activate.ps1       # Windows PowerShell
```
```pip install -r requirements.txt
uvicorn app.main:app --reload
```
Запуск в Docker
```bash
docker build -t lr2-fastapi .
docker run -d -p 8000:8000 --name lr2-fastapi lr2-fastapi
```
Открыть: http://localhost:8000/docs
