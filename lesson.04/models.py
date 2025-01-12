"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os
from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# URI для подключения к PostgreSQL
PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql://postgres:password@localhost:5432/postgres"

# Создаем engine для подключения к базе данных
engine = create_engine(PG_CONN_URI, echo=True)

# Создаем declarative base
Base = declarative_base()

# Создаем объект Session
Session = sessionmaker(bind=engine)

# Определяем модель User
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)

    # Связь с моделью Post
    posts = relationship("Post", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, username={self.username}, email={self.email})>"

# Определяем модель Post
class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String, nullable=False)
    body = Column(Text, nullable=False)

    # Связь с моделью User
    user = relationship("User", back_populates="posts")

    def __repr__(self):
        return f"<Post(id={self.id}, user_id={self.user_id}, title={self.title}, body={self.body})>"

# Создаем таблицы в базе данных (если они еще не созданы)
def create_tables():
    """
    Синхронная функция для создания таблиц в базе данных.
    """
    Base.metadata.create_all(bind=engine)

def drop_tables():
    """
    Синхронная функция для удаления таблиц из базы данных.
    """
    Base.metadata.drop_all(bind=engine)
    print("Таблицы успешно удалены.")

# Пример использования
if __name__ == "__main__":
    session = Session()

    # Пример добавления пользователя
    new_user = User(name="John", username="john", email="john@example2.com")
    session.add(new_user)
    session.commit()

    # Пример добавления поста
    new_post = Post(user_id=new_user.id, title="My First Post 2", body="This is the content of my first post. 2")
    session.add(new_post)
    session.commit()

    # Закрываем сессию
    session.close()


# import os
# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
# from sqlalchemy.orm import declarative_base, sessionmaker
# from sqlalchemy import Column, Integer, String, Text, ForeignKey
# from sqlalchemy.orm import relationship

# # URI для подключения к PostgreSQL
# PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql://postgres:password@localhost:5432/postgres"

# # Создаем асинхронный engine
# engine = create_async_engine(PG_CONN_URI, echo=True)

# # Создаем declarative base
# Base = declarative_base()

# # Создаем асинхронную сессию
# AsyncSessionLocal = sessionmaker(
#     bind=engine,
#     class_=AsyncSession,
#     expire_on_commit=False
# )

# # Определяем модель User
# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#     username = Column(String, nullable=False, unique=True)
#     email = Column(String, nullable=False, unique=True)

#     # Связь с моделью Post
#     posts = relationship("Post", back_populates="user")

#     def __repr__(self):
#         return f"<User(id={self.id}, name={self.name}, username={self.username}, email={self.email})>"

# # Определяем модель Post
# class Post(Base):
#     __tablename__ = "posts"

#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
#     title = Column(String, nullable=False)
#     body = Column(Text, nullable=False)

#     # Связь с моделью User
#     user = relationship("User", back_populates="posts")

#     def __repr__(self):
#         return f"<Post(id={self.id}, user_id={self.user_id}, title={self.title}, body={self.body})>"

# # Асинхронная функция для создания таблиц
# async def create_tables():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)

# # Пример асинхронной функции для добавления данных
# async def add_sample_data():
#     async with AsyncSessionLocal() as session:
#         async with session.begin():
#             # Пример добавления пользователя
#             new_user = User(name="John Doe", username="johndoe", email="john@example.com")
#             session.add(new_user)
#             await session.commit()

#             # Пример добавления поста
#             new_post = Post(user_id=new_user.id, title="My First Post", body="This is the content of my first post.")
#             session.add(new_post)
#             await session.commit()

# # Основная асинхронная функция
# import asyncio

# async def main():
#     await create_tables()
#     await add_sample_data()

# # Запуск асинхронной программы
# if __name__ == "__main__":
#     asyncio.run(main())