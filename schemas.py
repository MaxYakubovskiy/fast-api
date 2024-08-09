from typing import Optional
from database import new_session, TaskOrm
from pydantic import BaseModel


# Схема для добавления новой задачи
class STaskAdd(BaseModel):
    name: str  # Название задачи (обязательно)
    description: Optional[str] = None  # Описание задачи (необязательно)


# Схема для представления задачи с идентификатором
class STask(STaskAdd):
    id: int  # Идентификатор задачи (обязательно)
