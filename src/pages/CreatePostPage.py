from seleniumpagefactory import PageFactory
from time import sleep


class CreatePostPage(PageFactory):

    def __init__(self, driver):
        self.driver = driver

    locators = {'pop_up_title':('ID','header_text'),
                'choose_community': ('ID', 'toggle_community_list'),
                "add_community": ('XPATH', '//div[@class="pfsc-body"]/div/div[text()="Abortion"]'),
                "choose_topic": ('ID', 'toggle_topic_list'),
                "add_topic": ('XPATH', '//div[@class="pfsc-body"]//*[contains(text(),"News")]'),
                "add_title":('ID','post-title-textbox'),
                "add_body":('XPATH', '//*[@class="ck-placeholder"]'),
                "privacy":('XPATH','//*[@id="dropdown_wrapper"]'),
                "add_privacy":('XPATH','//div[@id="dropdown_animation_panel"]//div[contains(text(),"Inspire")]'),
                "post_button":('ID','submit-post-button'),
                "close_alert":('XPATH','//*[@id="dismiss_nudge"]'),
                "profile_menu":('ID','profile-menu-icon'),
                'home_icon':('XPATH','//*[@id="goToHome"]/i')
                }

    def verify_overlay_popup(self):
        actual_header=self.pop_up_title.get_text()
        assert actual_header =='Write a new post'

    def choose_add_community(self):
        self.choose_community.click()
        self.add_community.click()
        sleep(5)

    def choose_add_topic(self):
        self.choose_topic.click()
        self.add_topic.click()

    def input_title(self,title):
        self.add_title.set_text(title)

    def input_body(self,body):
        self.add_body.set_text(body)

    def click_add_privacy(self):
        self.privacy.click()
        self.add_privacy.click()

    def submit_post(self):
        self.post_button.click()

    def navigate_to_accounts_page(self):
        self.close_alert.click()
        self.profile_menu.click()
        self.home_icon.click()
