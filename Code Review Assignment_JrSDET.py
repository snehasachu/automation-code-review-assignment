from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

"""
General Recommendations:
1. Config Driven parameters : Use configuration files or environment variables for URLs, paths, and credentials.
2. Modularity : Break down large methods into smaller, reusable methods for better maintainability.
3. Use POM model : Implement the Page Object Model (POM) to separate page-specific interactions from test logic.
4. Cross-browser Support : Parameterize browser choice to enable testing across different browsers.
5. Logging : Replace print statements with logging library for better traceability.
6. Missing Assert statements : Add assert statements to validate test outcomes and ensure correctness.
7. Error handling : Implement error handling to manage exceptions.
"""

# Name of the test case can be specific 
class Testcase101:
    # Test case documentation should be provided

    def main(self):
        # Initialization should be moved to setUp method for better test management
        # Remove usage of hardcoded paths. Paths should be parameterized or set via environment variables
        driver = webdriver.Firefox(executable_path="C:\\Users\\Johny\\Downloads\\geckodriver-v0.33.0-win64\\geckodriver.exe")

        # URL should be config driven and must be easily changeable for different environments like stage, production etc. 
        driver.get("https://interview.supporthive.com/staff/")

        # Implicit wait should not be used. It is better to wait until elements are detected.
        driver.implicitly_wait(30)
        driver.maximize_window()

        # Break down large methods into smaller, separate methods.
        # For example: create seperate methods for login, navigating to sections, adding new statuses and logout.
        driver.find_element(By.ID, "id_username").send_keys("Agent")

        # Use config files or environment variables for credentials
        driver.find_element(By.ID, "id_password").send_keys("Agent@123")
        driver.find_element(By.ID, "btn-submit").click()
        tickets = driver.find_element(By.ID, "ember29")
        action = ActionChains(driver)
        action.move_to_element(tickets).perform()
        statuses = driver.find_element(By.LINK_TEXT, "Statuses")
        statuses.click()
        driver.find_element(By.XPATH, "/html/body/div[3]/div/section/section/div/header/button").click()
        driver.find_element(By.TAG_NAME, "input").send_keys("Issue Created")
        statusColourSelect = driver.find_element(By.XPATH, "//div[@class='sp-replacer sp-light']")
        statusColourSelect.click()
        statusColourEnter = driver.find_element(By.XPATH, "//input[@class='sp-input']")
        statusColourEnter.clear()
        statusColourEnter.send_keys("#47963f")
        
        # Robot class is not imported or used correctly
        r = Robot()
        # KeyEvent is not imported or used correctly
        r.keyPress(KeyEvent.VK_ESCAPE)

        # If possible, it is better to name the variables appropriately by following a naming convention 
        # rather than using firstElement, secondElement etc. 
        firstElement = driver.find_element(By.XPATH, "//a[@id='first-link']")
        firstElement.click()
        secondElement = driver.find_element(By.XPATH, "//a[@id='second-link']")
        secondElement.click()
        driver.find_element(By.TAG_NAME, "textarea").send_keys("Status when a new ticket is created in HappyFox")
        addCreate = driver.find_element(By.XPATH, "//button[@class ='hf-entity-footer_primary hf-primary-action ember-view']")
        addCreate.click()
        
        # Using time.sleep is not recommended as it can lead to flaky tests 
        # It is better to use Selenium's WebDriverWait
        time.sleep(3)
        
        moveTo = driver.find_element(By.XPATH, "//td[@class ='lt-cell align-center hf-mod-no-padding ember-view']")
        action.move_to_element(moveTo).perform()
        moveTo.click()
        
        # not recommended better to use Selenium's WebDriverWait
        time.sleep(9)
        issue = driver.find_element(By.XPATH, "//div[contains(text(),'Issue Created')]")
        action.move_to_element(issue).perform()
        make = driver.find_element(By.LINK_TEXT, "Make Default")
        make.click()
        driver.find_element(By.LINK_TEXT, "Priorities").click()
        driver.find_element(By.XPATH, "//header/button[1]").click()
        driver.find_element(By.TAG_NAME, "input").send_keys("Assistance required")
        driver.find_element(By.TAG_NAME, "textarea").send_keys("Priority of the newly created tickets")
        button = driver.find_element(By.CSS_SELECTOR, "button[data-test-id='add-priority']")
        button.click()

        # not recommended to use time.sleep, better to use Selenium's WebDriverWait
        time.sleep(9)
        tickets2 = driver.find_element(By.ID, "ember29")
        action.move_to_element(tickets2).perform()
        priorities2 = driver.find_element(By.LINK_TEXT, "Priorities")
        priorities2.click()

        # It is not recommended to use implicitly_wait, instead use wait for element to be displayed 
        driver.implicitly_wait(20)

        # It is better to use smaller and precise XPATHs if possible
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[1]/section[1]/section[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[9]/td[2]").click()
        driver.find_element(By.LINK_TEXT, "Delete").click()

        # Use better naming conventions. Eg. btn_delete for delete button
        delete = driver.find_element(By.CSS_SELECTOR, "button[data-test-id='delete-dependants-primary-action']")
        delete.click()

        # It is not recommended to use time.sleep, instead use wait for element to be displayed 
        time.sleep(9)
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[1]/header[1]/div[2]/nav[1]/div[7]/div[1]/div[1]").click()
        driver.find_element(By.LINK_TEXT, "Logout").click()

class PagesforAutomationAssignment:
    # A documentation of the class can be provided

    def main(self):
        # parameterize browser choice for flexibility for testing across different browsers
        driver = webdriver.Chrome()
        driver.get("https://www.happyfox.com")

        # avoid hardcoded credentials for login
        loginPage = LoginPage(driver)
        loginPage.login("username", "password")

        homePage = HomePage(driver)
        homePage.verifyHomePage()

        # Add tearDown method to close the driver after tests
        driver.quit()

class BasePage:
    # proper initialization in the BasePage class.
    def __init__(self, driver):
        self.driver = driver

class LoginPage(BasePage):
    # A documentation of the class can be provided
    
    def login(self, username, password):
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "loginButton").click()

    def forgotPassword(self):
        self.driver.find_element(By.LINK_TEXT, "Forgot password?").click()

class HomePage(BasePage):

    def verifyHomePage(self):
        # URL should be config driven and must be easily changeable for different environments like stage, production etc. 
        if self.driver.current_url != "https://www.happyfox.com/home":
            raise Exception("Not on the home page")

    def navigateToProfile(self):
        self.driver.find_element(By.ID, "profileLink").click()

class TablePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.rowLocator = By.XPATH("//table[@id='dataTable']/tbody/tr")

    def retrieveRowTexts(self):
        rows = self.driver.find_elements(self.rowLocator)
        
        # Can use, instead of variable i 
        # for row in rows:
        for i in range(len(rows)):
            row = rows[i]
            rowText = row.text
            # It is better to use logging libraries rather than print statements
            print("Row " + str(i) + " Text: " + rowText)

