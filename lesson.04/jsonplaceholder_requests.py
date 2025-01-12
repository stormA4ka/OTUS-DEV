"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

import aiohttp
import asyncio

# URL ресурсов
USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_data(session, url):
    """
    Асинхронная функция для выполнения GET-запроса к указанному URL.
    """
    async with session.get(url) as response:
        if response.status == 200:
            return await response.json()
        else:
            print(f"Ошибка при запросе {url}: {response.status}")
            return None


async def get_users_data():
    """
    Асинхронная функция для получения данных пользователей.
    """
    async with aiohttp.ClientSession() as session:
        return await fetch_data(session, USERS_DATA_URL)


async def get_posts_data():
    """
    Асинхронная функция для получения данных постов.
    """
    async with aiohttp.ClientSession() as session:
        return await fetch_data(session, POSTS_DATA_URL)


async def main():
    """
    Основная асинхронная функция для выполнения запросов к обоим ресурсам.
    """
    users_task = asyncio.create_task(get_users_data())
    posts_task = asyncio.create_task(get_posts_data())

    users_data, posts_data = await asyncio.gather(users_task, posts_task)

    print("Данные пользователей:")
    print(users_data)
    print("\nДанные постов:")
    print(posts_data)


# Запуск асинхронной программы
if __name__ == "__main__":
    asyncio.run(main())