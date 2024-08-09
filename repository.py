from typing import List
from sqlalchemy import select
from database import new_session, TaskOrm
from schemas import STaskAdd, STask


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        # Метод для добавления новой задачи в базу данных
        async with new_session() as session:  # Открытие новой сессии
            task_dict = data.model_dump()  # Преобразование схемы данных в словарь
            task = TaskOrm(**task_dict)  # Создание экземпляра ORM модели
            session.add(task)  # Добавление задачи в сессию
            await session.flush()  # Сохранение изменений в базе данных
            await session.commit()  # Подтверждение изменений
            return task.id  # Возврат идентификатора добавленной задачи

    @classmethod
    async def find_all(cls) -> List[STask]:
        # Метод для получения всех задач из базы данных
        async with new_session() as session:  # Открытие новой сессии
            query = select(TaskOrm)  # Создание запроса для выбора всех задач
            result = await session.execute(query)  # Выполнение запроса
            task_models = result.scalars().all()  # Получение всех результатов запроса
            # Преобразование ORM моделей в схемы данных
            task_schemas = [STask.model_validate(task_model) for task_model in task_models]
            return task_schemas  # Возврат списка задач в виде схем данных
