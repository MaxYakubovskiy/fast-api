from typing import List
from fastapi import APIRouter, Depends
from repository import TaskRepository
from schemas import STaskAdd, STask


# Создание маршрутизатора для обработки запросов на '/tasks'
router = APIRouter(
    prefix='/tasks',  # Префикс для всех маршрутов в этом роутере
    tags=['Task'],    # Тэги для группировки эндпоинтов в документации
)


# Эндпоинт для добавления новой задачи
@router.post('')
async def add_task(task: STaskAdd = Depends()):
    task_id = await TaskRepository.add_one(task)  # Добавление задачи в репозиторий
    return {'ok': True, 'task_id': task_id}  # Возврат идентификатора добавленной задачи


# Эндпоинт для получения всех задач
@router.get('')
async def get_home() -> List[STask]:
    tasks = await TaskRepository.find_all()  # Получение всех задач из репозитория
    return tasks  # Возврат списка задач
