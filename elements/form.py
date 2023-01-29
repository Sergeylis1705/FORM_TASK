
from sel_base.base import SeleniumBase


class Form(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.name = 'input[id="firstName"]'
        self.lastName = 'input[id="lastName"]'
        self.email = 'input[id="userEmail"]'
        self.gender = 'label[for="gender-radio-3"]'
        self.mobile = 'input[id="userNumber"]'
        self.dateOfBirth = 'input[id="dateOfBirthInput"]'
        self.hobbies = 'label[for="hobbies-checkbox-1"]'
        self.currentAddress = 'textarea[id="currentAddress"]'
        self.subjects = 'div[class="subjects-auto-complete__value-container subjects-auto-complete__value-container--is-multi css-1hwfws3"]'
        self.test_text = 'Test'
        self.email_test_text = 'Test@test.test'
        self.mobile_test_text = '1000000000'
        self.button_submit = 'button[class="btn btn-primary"]'
        self.table_item = 'table[class="table table-dark table-striped table-bordered table-hover"]'
        self.EXPECTED_RESULT = [['Label Values', 'Student Name Test Test', 'Student Email Test@test.test', 'Gender Other', 'Mobile 1000000000', 'Date of Birth 29 January,2023', 'Subjects', 'Hobbies Sports', 'Picture', 'Address Text', 'State and City']]


    def find_name(self):
        return self.is_visible('css', self.name, '')

    def find_lastName(self):
        return self.is_visible('css', self.lastName, '')

    def find_email(self):
        return self.is_visible('css', self.email, '')

    def find_gender(self):
        button = self.is_visible('css', self.gender, '')
        self.click_on_element(button)

    def find_mobile(self):
        return self.is_visible('css', self.mobile, '')

    def find_dateOfBirsth(self):
        return self.is_visible('css', self.dateOfBirth, '')

    def find_hobbies(self):
        button = self.is_visible('css', self.hobbies, '')
        self.click_on_element(button)

    def find_currentAddress(self):
        return self.is_visible('css', self.currentAddress, '')

    def find_button_submit(self):
        button = self.is_visible('css', self.button_submit)
        self.click_on_element(button)

    def find_table_element(self):
        table_element = self.are_visible('css', self.table_item)
        data = []
        for item in table_element:
            data.append(item.text.splitlines())
        return data




