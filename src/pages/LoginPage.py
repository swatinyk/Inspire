from seleniumpagefactory import PageFactory


class LoginPage(PageFactory):

    user_name='pawarswati507@gmail.com'
    secret='inspire@123'

    def __init__(self, driver):
        self.driver = driver

    locators = {'sign_in': ('ID', 'logIn'),
                "username":('ID','email'),
                "password":('ID','pw'),
                "login_button":('ID','login_submit')}

    def click_sign_in(self):
        self.sign_in.click()

    def select_username(self):
        self.username.set_text(LoginPage.user_name)

    def select_password(self):
        self.password.set_text(LoginPage.secret)

    def click_login(self):
        self.login_button.click()
