from selene import browser, have, be
import os


class RegistrationPage:
    def open(self):
        browser.open("https://xqa.io/practice/practice-form")
        return self

    def fill_first_name(self, value):
        browser.element("#firstName").type(value)
        return self

    def fill_last_name(self, value):
        browser.element("#lastName").type(value)
        return self

    def fill_email(self, value):
        browser.element("#userEmail").type(value)
        return self

    def select_male_gender(self):
        browser.element('//input[@value="Male"]').click()
        return self

    def select_female_gender(self):
        browser.element('//input[@value="Female"]').click()
        return self

    def fill_mobile(self, value):
        browser.element("#userNumber").type(value)
        return self

    def fill_date_of_birth(self, value):
        browser.element("#dateOfBirthInput").clear().type(value)
        return self

    def select_hobby_music(self):
        browser.element('//input[@id="hobbies-Music"]').click()
        return self

    def select_hobby_reading(self):
        browser.element('//input[@id="hobbies-Reading"]').click()
        return self

    def select_hobby_sports(self):
        browser.element('//input[@id="hobbies-Sports"]').click()
        return self

    def upload_picture(self, file_name):
        file_path = os.path.abspath(f"tests/{file_name}")
        browser.element("#uploadPicture").send_keys(file_path)
        return self

    def fill_address(self, value):
        browser.element("#currentAddress").type(value)
        return self

    def select_state(self, state_name):
        browser.element("#state").click()
        browser.element(f'//option[contains(text(), "{state_name}")]').click()
        return self

    def select_city(self, city_name):
        browser.element("#city").click()
        browser.element(f'//option[contains(text(), "{city_name}")]').click()
        return self

    def submit(self):
        browser.element("#submit").click()
        return self

    def should_have_registered(self, **data):
        browser.element('//*[contains(text(), "Thanks for submitting")]').should(be.visible)

        if 'student_name' in data:
            browser.element('//td[text()="Student Name"]/following-sibling::td').should(
                have.text(data['student_name'])
            )
        if 'student_email' in data:
            browser.element('//td[text()="Student Email"]/following-sibling::td').should(
                have.text(data['student_email'])
            )
        if 'gender' in data:
            browser.element('//td[text()="Gender"]/following-sibling::td').should(
                have.text(data['gender'])
            )
        if 'mobile' in data:
            browser.element('//td[text()="Mobile"]/following-sibling::td').should(
                have.text(data['mobile'])
            )
        if 'date_of_birth' in data:
            browser.element('//td[text()="Date of Birth"]/following-sibling::td').should(
                have.text(data['date_of_birth'])
            )
        if 'hobbies' in data:
            browser.element('//td[text()="Hobbies"]/following-sibling::td').should(
                have.text(data['hobbies'])
            )
        if 'address' in data:
            browser.element('//td[text()="Address"]/following-sibling::td').should(
                have.text(data['address'])
            )
        if 'state_city' in data:
            browser.element('//td[text()="State and City"]/following-sibling::td').should(
                have.text(data['state_city'])
            )
        return self

    def register(self, user):
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)

        if user.gender == "Male":
            self.select_male_gender()
        elif user.gender == "Female":
            self.select_female_gender()

        self.fill_mobile(user.mobile)
        self.fill_date_of_birth(user.date_of_birth)

        for hobby in user.hobbies:
            if hobby == "Music":
                self.select_hobby_music()
            elif hobby == "Reading":
                self.select_hobby_reading()
            elif hobby == "Sports":
                self.select_hobby_sports()

        self.upload_picture(user.picture)
        self.fill_address(user.address)
        self.select_state(user.state)
        self.select_city(user.city)
        return self