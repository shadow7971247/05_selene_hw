from pages.registration_page import RegistrationPage


registration_page = RegistrationPage()


def test_fill_form():
    (
        registration_page
        .open()
        .fill_first_name("Кто то там")
        .fill_last_name("Такой то")
        .fill_email("ktoto@example.com")
        .select_male_gender()
        .fill_mobile("1234567890")
        .fill_date_of_birth("13-11-1995")
        .select_hobby_music()
        .select_hobby_reading()
        .upload_picture("test.jpg")
        .fill_address("Улица Пушкина")
        .select_state("NCR")
        .select_city("Delhi")
        .submit()
        .should_have_registered(
            student_name="Кто то там Такой то",
            student_email="ktoto@example.com",
            gender="Male",
            mobile="1234567890",
            date_of_birth="1995-11-13",
            hobbies="Music, Reading",
            address="Улица Пушкина",
            state_city="NCR Delhi"
        )
    )