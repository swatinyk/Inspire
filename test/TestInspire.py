from webdriver_manager.chrome import ChromeDriverManager
from src.pages.LoginPage import *
from src.pages.CreatePostPage import *
from src.pages.HomePage import *
import pytest


from selenium import webdriver

#performs the setup and teardown activities
@pytest.fixture
def setup():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.inspire.com')
    driver.maximize_window()
    yield driver
    driver.close()


# create the objects of each class and make calls to the methods of each class
def test_inspire(setup):
    title='My_first_post_on_inpsire.com'

    login_page = LoginPage(setup)
    create_post_page = CreatePostPage(setup)
    home_page = HomePage(setup)

    login_page.click_sign_in()
    login_page.select_username()
    login_page.select_password()
    login_page.click_login()

    home_page.click_on_post_button()

    create_post_page.verify_overlay_popup()
    create_post_page.choose_add_community()
    create_post_page.choose_add_topic()
    create_post_page.input_title(title)
    create_post_page.input_body('My_first_post_on_inpsire.com')
    create_post_page.click_add_privacy()
    create_post_page.submit_post()
    create_post_page.navigate_to_accounts_page()

    home_page.verify_title_of_post(title)
