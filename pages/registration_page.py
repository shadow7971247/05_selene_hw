from selene import browser, have, be
import os


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element("#firstName")
        self.last_name = browser.element("#lastName")
        self.email = browser.element("#userEmail")
        self.gender_male = browser.element('//input[@value="Male"]')
        self.mobile = browser.element("#userNumber")
        self.date_of_birth = browser.element("#dateOfBirthInput")
        self.hobbies_music = browser.element('//input[@id="hobbies-Music"]')
        self.hobbies_reading = browser.element('//input[@id="hobbies-Reading"]')
        self.picture = browser.element("#uploadPicture")
        self.address = browser.element("#currentAddress")
        self.state = browser.element("#state")
        self.city = browser.element("#city")
        self.submit_button = browser.element("#submit")
        self.modal_title = browser.element('//*[contains(text(), "Thanks for submitting")]')

    def open(self):
        browser.open("https://xqa.io/practice/practice-form")
        return self

    def fill_first_name(self, value: str):
        self.first_name.type(value)
        return self

    def fill_last_name(self, value: str):
        self.last_name.type(value)
        return self

    def fill_email(self, value: str):
        self.email.type(value)
        return self

    def select_male_gender(self):
        self.gender_male.click()
        return self

    def fill_mobile(self, value: str):
        self.mobile.type(value)
        return self

    def fill_date_of_birth(self, value: str):
        self.date_of_birth.clear().type(value)
        return self

    def select_hobby_music(self):
        self.hobbies_music.click()
        return self

    def select_hobby_reading(self):
        self.hobbies_reading.click()
        return self

    def upload_picture(self, file_name: str):
        file_path = os.path.abspath(f"tests/{file_name}")
        self.picture.send_keys(file_path)
        return self

    def fill_address(self, value: str):
        self.address.type(value)
        return self

    def select_state(self, state_name: str):
        self.state.click()
        browser.element(f'//option[contains(text(), "{state_name}")]').click()
        return self

    def select_city(self, city_name: str):
        self.city.click()
        browser.element(f'//option[contains(text(), "{city_name}")]').click()
        return self

    def submit(self):
        self.submit_button.click()
        return self

    def should_have_registered(self, **expected_data):
        self.modal_title.should(be.visible)

        if 'student_name' in expected_data:
            browser.element('//td[text()="Student Name"]/following-sibling::td').should(
                have.text(expected_data['student_name'])
            )

        if 'student_email' in expected_data:
            browser.element('//td[text()="Student Email"]/following-sibling::td').should(
                have.text(expected_data['student_email'])
            )

        if 'gender' in expected_data:
            browser.element('//td[text()="Gender"]/following-sibling::td').should(
                have.text(expected_data['gender'])
            )

        if 'mobile' in expected_data:
            browser.element('//td[text()="Mobile"]/following-sibling::td').should(
                have.text(expected_data['mobile'])
            )

        if 'date_of_birth' in expected_data:
            browser.element('//td[text()="Date of Birth"]/following-sibling::td').should(
                have.text(expected_data['date_of_birth'])
            )

        if 'hobbies' in expected_data:
            browser.element('//td[text()="Hobbies"]/following-sibling::td').should(
                have.text(expected_data['hobbies'])
            )

        if 'address' in expected_data:
            browser.element('//td[text()="Address"]/following-sibling::td').should(
                have.text(expected_data['address'])
            )

        if 'state_city' in expected_data:
            browser.element('//td[text()="State and City"]/following-sibling::td').should(
                have.text(expected_data['state_city'])
            )

        return self