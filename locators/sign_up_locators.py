from selenium.webdriver.common.by import By


class SignUpLocators:
    # start sign up
    LOCATOR_START_SIGN_UP_HEADER = (By.XPATH, '//p[contains(text(), \'EventSource Sign up\')]')
    LOCATOR_FULL_NAME_FIELD = (By.XPATH, '//input[@name = \'FullName\']')
    LOCATOR_EMAIL_FIELD = (By.XPATH, '//input[@name = \'Email\']')
    # LOCATOR_EVENT_TYPE_FIELD = (By.XPATH, '//input[@name= \'eventDate\']')
    LOCATOR_EVENT_DATE_FIELD = (By.XPATH, '//input[@name= \'eventDate\']')
    LOCATOR_CONTINUE_BTN = (By.XPATH, '//a[contains(text(), \'Continue\')]')

    # continue sign up
    LOCATOR_CONTINUE_SIGN_UP_HEADER = (By.XPATH, '//p[contains(text(), \'Stay Super Organized!\')]')
    # LOCATOR_EVENT_BUDGET_FIELD = (By.XPATH, '//input[@placeholder= \'Approx\']')
    # LOCATOR_GUESTS_NUMBER_FIELD = (By.XPATH, '//input[@placeholder= \'200\']')
    LOCATOR_SUBMIT_BTN = (By.XPATH, '//button[contains(@class, \'btn btn-red btn-submit\')]')

    # final sign up
    LOCATOR_FINAL_SIGN_UP_HEADER = (By.XPATH, '//p[contains(text(), \'Check your email\')]')
    LOCATOR_GOT_IT_BTN = (By.XPATH, '//button[contains(@class, \'btn btn-red btn-get-it\')]')
