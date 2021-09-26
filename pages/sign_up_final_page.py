from pages.base_page import BasePage
from locators.sign_up_locators import SignUpLocators


class SignUpFinalPage(BasePage):

    def should_be_sign_up_final_page(self):
        final_sign_up_header = self.find_element(SignUpLocators.LOCATOR_FINAL_SIGN_UP_HEADER)
        print("Какая-то дичь)))")
        print(final_sign_up_header.text)
        assert final_sign_up_header.text == "Check Your Email"

    def final_sign_up(self):
        got_it_btn = self.find_element(SignUpLocators.LOCATOR_GOT_IT_BTN)
        got_it_btn.click()
