import time

import pytest


from elements.form import Form


@pytest.mark.usefixtures('setup')
class TestElements:

    def test_text_box(self):
        form_page = Form(self.driver)
        form_page.find_name().send_keys('Test')
        form_page.find_lastName().send_keys('Test')
        form_page.find_email().send_keys('Test@test.test')
        form_page.find_gender().click()
        form_page.find_mobile().send_keys('1000000000')
        form_page.find_hobbies().click()
        form_page.find_currentAddress().send_keys('Text')
        time.sleep(2)
        form_page.find_button_submit()
        time.sleep(5)
        inform = form_page.find_table_element()
        print(inform)
        expected_result = form_page.EXPECTED_RESULT
        assert expected_result == inform


