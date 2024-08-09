# Task API

Это проект для управления задачами с использованием FastAPI и SQLAlchemy. Проект включает в себя создание, получение и управление задачами.

## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/MaxYakubovskiy/fast-api.git
    ```

2. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

3. Запустите проект:
    ```bash
    uvicorn main:app --reload
    ```

## Использование

1. Создание новой задачи:
    **POST** `/tasks`

    **Тело запроса:**
    ```json
    {
        "name": "Task name",
        "description": "Task description"
    }
    ```

    **Ответ:**
    ```json
    {
        "ok": true,
        "task_id": 1
    }
    ```

2. Получение списка задач:
    **GET** `/tasks`

    **Ответ:**
    ```json
    [
        {
            "id": 1,
            "name": "Task name",
            "description": "Task description"
        }
    ]
    ```

## API

**POST /tasks**

Создает новую задачу.

**Запрос:**

- **Тело:** Схема `STaskAdd`

**Ответ:**

- **Код 200:** Схема `STask` с полем `task_id`

**GET /tasks**

Возвращает список всех задач.

**Ответ:**

- **Код 200:** Список объектов `STask`

## Структура проекта

- **`schemas.py`**: Определение схем данных с помощью Pydantic.
- **`repository.py`**: Репозиторий для взаимодействия с базой данных.
- **`router.py`**: Роутер для обработки API запросов.
- **`database.py`**: Определение моделей и функции для работы с базой данных.
