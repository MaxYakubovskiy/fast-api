from typing import Optional
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# Создание асинхронного движка для работы с базой данных SQLite
engine = create_async_engine(
    'sqlite+aiosqlite:///tasks.db'  # Путь к базе данных
)

# Создание асинхронной фабрики сессий
new_session = async_sessionmaker(engine, expire_on_commit=False)

# Базовый класс для всех моделей SQLAlchemy
class Model(DeclarativeBase):
    pass

# Определение ORM модели для задачи
class TaskOrm(Model):
    __tablename__ = 'tasks'  # Имя таблицы в базе данных

    id: Mapped[int] = mapped_column(primary_key=True)  # Поле id как первичный ключ
    name: Mapped[str]  # Поле name типа строка
    description: Mapped[Optional[str]]  # Поле description типа строка или None

# Асинхронная функция для создания таблиц в базе данных
async def create_tables():
    async with engine.begin() as conn:  # Открытие соединения с базой данных
        await conn.run_sync(Model.metadata.create_all)  # Создание всех таблиц

# Асинхронная функция для удаления таблиц из базы данных
async def delete_tables():
    async with engine.begin() as conn:  # Открытие соединения с базой данных
        await conn.run_sync(Model.metadata.drop_all)  # Удаление всех таблиц
