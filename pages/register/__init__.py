import random
from typing import List
from .locators import Locators
from utils.logger import get_logger
from pages.base_page import BasePage

class RegisterPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.__locators = Locators
        self.__logger = get_logger()

    def fill_personal_info(self, first_name: str, last_name: str, address: str, email: str, phone: str):
        self.fill(self.__locators.FIRST_NAME, first_name)
        self.fill(self.__locators.LAST_NAME, last_name)
        self.fill(self.__locators.ADDRESS, address)
        self.fill(self.__locators.EMAIL, email)
        self.fill(self.__locators.PHONE, phone)
    
    def select_gender(self, gender: str = "Male"):
        if gender.lower() == "male":
            self.click(self.__locators.GENDER_MALE)
        else:
            self.click(self.__locators.GENDER_FEMALE)
    
    def select_hobbies(self, hobbies: List[str] = random.choice(["Cricket", "Movies", "Hockey"])):
        for hobby in hobbies:
            match hobby.lower():
                case "cricket":
                    self.click(self.__locators.HOBBIES_CRICKET)
                case "movies":
                    self.click(self.__locators.HOBBIES_MOVIES)
                case "hockey":
                    self.click(self.__locators.HOBBIES_HOCKEY)
    
    def select_skills(self, skill: str = "Java"):
        skill = skill.title()
        self.select_option(self.__locators.SKILLS_DROPDOWN, skill)
    
    def select_country(self, country: str = "India"):
        country = country.title()
        self.select_option(self.__locators.COUNTRY_DROPDOWN, country)


    def select_language(self, language: str = "English"):
        language = language.title()
        self.click(self.__locators.LANGUAGES_DROPDOWN)

        if self.page.is_visible(self.__locators.GENERIC_LANGUAGE_ENTITY.format(language)):
            self.click(self.__locators.GENERIC_LANGUAGE_ENTITY.format(language))

        self.close_dropdown()


    def select_birth_date(self, year: str = "1990", month: str = "January", day: str = "1"):
        self.select_option(self.__locators.YEAR_DROPDOWN, year)
        self.select_option(self.__locators.MONTH_DROPDOWN, month)
        self.select_option(self.__locators.DAY_DROPDOWN, day)
    
    def fill_password(self, password: str, confirm_password: str = None):
        if confirm_password is None:
            confirm_password = password
        self.fill(self.__locators.PASSWORD, password)
        self.fill(self.__locators.CONFIRM_PASSWORD, confirm_password)
    
    def submit_form(self):
        self.click(self.__locators.SUBMIT_BUTTON)
    
    def fill_complete_form(self):
        self.fill_personal_info(
            last_name="Doe",
            first_name="John",
            email="john.doe@test.com",
            address="123 Test Street, Test City",
            phone="1234567890"
        )
        self.select_gender("Male")
        self.select_hobbies(["Cricket"])
        self.select_language("English")
        self.select_skills("Java")
        self.select_country("India")
        self.select_birth_date("1990", "January", "1")
        self.fill_password("TestPassword123")