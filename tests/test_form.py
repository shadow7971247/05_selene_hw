from selene import browser, be, have
import os


def test_fill_form():
    browser.open("https://xqa.io/practice/practice-form")

    # Заполнение полей
    browser.element("#firstName").type("Кто то там")
    browser.element("#lastName").type("Такой то")
    browser.element("#userEmail").type("ktoto@example.com")
    browser.element('//input[@value="Male"]').click()
    browser.element("#userNumber").type("1234567890")

    #так и не понял как сделать мануальный выбор
    browser.element('#dateOfBirthInput').clear().type('13-11-1995')

    browser.element('//input[@id="hobbies-Music"]').click()
    browser.element('//input[@id="hobbies-Reading"]').click()
    browser.element("#uploadPicture").send_keys(os.path.abspath("tests/test.jpg"))
    browser.element("#currentAddress").type("Улица Пушкина")
    browser.element("#state").click()
    browser.element('//option[contains(text(), "NCR")]').click()
    browser.element("#city").click()
    browser.element('//option[contains(text(), "Delhi")]').click()

    # Отправить и проверить
    browser.element("#submit").click()
    browser.element('//*[contains(text(), "Thanks for submitting")]').should(be.visible)

    browser.element('//td[text()="Student Name"]/following-sibling::td').should(have.text('Кто то там Такой то'))
    browser.element('//td[text()="Student Email"]/following-sibling::td').should(have.text('ktoto@example.com'))
    browser.element('//td[text()="Gender"]/following-sibling::td').should(have.text('Male'))
    browser.element('//td[text()="Mobile"]/following-sibling::td').should(have.text('1234567890'))
    browser.element('//td[text()="Date of Birth"]/following-sibling::td').should(have.text('1995-11-13'))
    browser.element('//td[text()="Hobbies"]/following-sibling::td').should(have.text('Music, Reading'))
    browser.element('//td[text()="Address"]/following-sibling::td').should(have.text('Улица Пушкина'))
    browser.element('//td[text()="State and City"]/following-sibling::td').should(have.text('NCR Delhi'))
