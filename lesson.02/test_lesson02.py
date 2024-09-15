import pytest
import json
from model import Book, User, WrongInt


# Тесты для класса User
def test_create_user_with_valid_data():
    user = User("John Doe", "1234567890", "Test comment")
    assert user.full_name == "John Doe"
    assert user.phone == "1234567890"
    assert user.comment == "Test comment"
    assert user.id == 0


def test_create_user_with_invalid_phone():
    with pytest.raises(WrongInt):
        User("John Doe", "invalid_phone", "Test comment")


@pytest.fixture(autouse=True)
def reset_id_counter():
    User._id_counter = 0  # сбрасываем счетчик, чтобы не было ошибки


def test_user_id_assignment():
    user1 = User("John Doe", "1234567890", "Test comment")
    user2 = User("Jane Doe", "0987654321", "Test comment")
    assert user1.id == 0
    assert user2.id == 1


# Тесты для класса Book
@pytest.fixture
def temp_book_file(tmpdir):
    file_path = tmpdir.join("test_book.json")
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump([{"id": 0, "full_name": "John Doe", "phone": "1234567890", "comment": "Test comment",
                    "date_added": "2023-10-01T12:00:00"}], file)
    return file_path


def test_read_users(temp_book_file):
    book = Book(temp_book_file)
    users = book.read_users()
    assert len(users) == 1
    assert users[0].full_name == "John Doe"


def test_save_book(temp_book_file):
    book = Book(temp_book_file)
    book.add_user("Jane Doe", "0987654321", "Another comment")
    book.save_book()

    with open(temp_book_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
        assert len(data) == 2
        assert data[1]['full_name'] == "Jane Doe"


def test_search_user(temp_book_file):
    book = Book(temp_book_file)
    user = book.search_user(0)
    assert user.full_name == "John Doe"


def test_remove_user(temp_book_file):
    book = Book(temp_book_file)
    book.remove_user(0)
    assert len(book.users) == 0


def test_edit_user(temp_book_file):
    book = Book(temp_book_file)
    book.edit_user(0, full_name="John Smith", phone="1111111111")
    user = book.search_user(0)
    assert user.full_name == "John Smith"
    assert user.phone == "1111111111"


def test_add_user(temp_book_file):
    book = Book(temp_book_file)
    new_user = book.add_user("Jane Doe", "0987654321", "Another comment")
    assert new_user.id == 1
    assert new_user.full_name == "Jane Doe"


def test_about_book(temp_book_file):
    book = Book(temp_book_file)
    record_count, file_size = book.about_book()
    assert record_count == 1
    assert file_size > 0
