from seleniumpagefactory import PageFactory


class HomePage(PageFactory):

    def __init__(self, driver):
        self.driver = driver

    locators = {'post_button': ('ID', 'startPostButton'),
                'title':('XPATH','//section[@id="post-section"]//h3[@class="pb-title"]')}

    def click_on_post_button(self):
        self.driver.execute_script("arguments[0].click();", self.post_button)

    def verify_title_of_post(self,expected_title):
        actual_title=self.title.get_text()
        assert actual_title==expected_title
