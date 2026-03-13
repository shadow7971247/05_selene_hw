from pages.registration_page import RegistrationPage
from data import users

registration_page = RegistrationPage()


def test_register_student():
    student = users.student
    registration_page.open()
    registration_page.register(student)
    registration_page.submit()
    registration_page.should_have_registered(
        student_name=student.full_name,
        student_email=student.email,
        gender=student.gender,
        mobile=student.mobile,
        date_of_birth="1995-11-13",
        hobbies=student.hobbies_str,
        address=student.address,
        state_city=student.state_city
    )


def test_register_female_student():
    student = users.female_student
    registration_page.open()
    registration_page.register(student)
    registration_page.submit()
    registration_page.should_have_registered(
        student_name=student.full_name,
        student_email=student.email,
        gender=student.gender,
        mobile=student.mobile,
        date_of_birth="1250-01-01",
        hobbies=student.hobbies_str,
        address=student.address,
        state_city=student.state_city
    )


def test_register_up_student():
    student = users.student_from_up
    registration_page.open()
    registration_page.register(student)
    registration_page.submit()
    registration_page.should_have_registered(
        student_name=student.full_name,
        student_email=student.email,
        gender=student.gender,
        mobile=student.mobile,
        date_of_birth="2026-01-01",
        hobbies=student.hobbies_str,
        address=student.address,
        state_city=student.state_city
    )