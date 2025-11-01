class RegisterFlow:

    def __init__(self, app_pages, test_data):
        self.__app_pages = app_pages
        self.__test_data = test_data

    def fill_personal_info(self, personal_info=None):
        if not personal_info:
            personal_info = self.__test_data.get_personal_info()

        self.__app_pages.register.fill_personal_info(
            phone=personal_info["phone"],
            email=personal_info["email"],
            address=personal_info["address"],
            last_name=personal_info["last_name"],
            first_name=personal_info["first_name"],
        )

    def register_user(self):
        password = self.__test_data.get_password()
        birth_date = self.__test_data.get_birth_date()
        form_selections = self.__test_data.get_form_selections()

        self.__app_pages.register.select_gender(form_selections["gender"])
        self.__app_pages.register.select_hobbies(form_selections["hobbies"])
        self.__app_pages.register.select_language(form_selections["language"])
        self.__app_pages.register.select_skills(form_selections["skills"])
        self.__app_pages.register.select_country(form_selections["country"])

        self.__app_pages.register.select_birth_date(
            birth_date["year"], birth_date["month"], birth_date["day"]
        )
        self.__app_pages.register.fill_password(password)
