from selene import browser, be
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
    browser.element('#dateOfBirthInput').type('13-11-1995')

    browser.element('//input[@id="hobbies-Music"]').click()
    browser.element('//input[@id="hobbies-Reading"]').click()
    browser.element("#uploadPicture").send_keys(os.path.abspath("test.jpg"))
    browser.element("#currentAddress").type("Улица Пушкина")
    browser.element("#state").click()
    browser.element('//option[contains(text(), "NCR")]').click()
    browser.element("#city").click()
    browser.element('//option[contains(text(), "Delhi")]').click()

    # Отправить и проверить
    browser.element("#submit").click()
    browser.element('//*[contains(text(), "Thanks for submitting")]').should(be.visible)
    # сделан поиск через часть текста, тк мешает всплывающее окно хрома
