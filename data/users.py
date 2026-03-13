from data.user import User

student = User(
    first_name="Кто то там",
    last_name="Такой то",
    email="ktoto@example.com",
    gender="Male",
    mobile="1234567890",
    date_of_birth="13-11-1995",
    hobbies=["Music", "Reading"],
    picture="test.jpg",
    address="Улица Пушкина",
    state="NCR",
    city="Delhi"
)

female_student = User(
    first_name="Жанка",
    last_name="Арбузарова",
    email="zhanna@example.com",
    gender="Female",
    mobile="0987654321",
    date_of_birth="01-01-1250",
    hobbies=["Reading"],
    picture="test.jpg",
    address="Дом Колотушкина",
    state="NCR",
    city="Delhi"
)

student_from_up = User(
    first_name="Иван",
    last_name="Золо",
    email="ivan@example.com",
    gender="Male",
    mobile="7777777777",
    date_of_birth="01-01-2026",
    hobbies=["Music"],
    picture="test.jpg",
    address="под номером 3",
    state="Uttar Pradesh",
    city="Delhi"
)