"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""


import asyncio
from models import Base, User, Post, engine, AsyncSessionLocal, create_tables, drop_tables
from jsonplaceholder_requests import get_users_data, get_posts_data


async def add_users_and_posts_to_db(users_data, posts_data):
    """
    Асинхронная функция для добавления пользователей и постов в базу данных.
    """
    async with AsyncSessionLocal() as session:
        async with session.begin():
            # Добавляем пользователей
            for user_data in users_data:
                user = User(
                    name=user_data["name"],
                    username=user_data["username"],
                    email=user_data["email"]
                )
                session.add(user)

            # Добавляем посты
            for post_data in posts_data:
                post = Post(
                    user_id=post_data["userId"],
                    title=post_data["title"],
                    body=post_data["body"]
                )
                session.add(post)

            await session.commit()


async def async_main():
    """
    Основная асинхронная функция, которая выполняет полный цикл программы.
    """
    # Удаляем таблицы
    await drop_tables()

    # Создаем таблицы
    await create_tables()

    # Загружаем пользователей и посты
    users_task = asyncio.create_task(get_users_data())
    posts_task = asyncio.create_task(get_posts_data())
    users_data, posts_data = await asyncio.gather(users_task, posts_task)

    # Добавляем пользователей и посты в базу данных
    await add_users_and_posts_to_db(users_data, posts_data)

    print("Данные успешно загружены и добавлены в базу данных!")


def main():
    """
    Основная функция, которая запускает асинхронную функцию async_main.
    """
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
