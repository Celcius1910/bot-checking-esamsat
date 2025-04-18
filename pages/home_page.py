from playwright.sync_api import Page
from utils.config import *
import allure
import pyautogui
import time


class HomePage:
    def __init__(self, page: Page):
        self.page = page

        # instance
        self.findYourService_navbar = self.FindYourService_Navbar(self)
        self.successStories_navbar = self.SuccessStories_Navbar(self)
        self.becomeAServiceProvider_navbar = self.BecomeAServiceProvider_Navbar(self)
        self.aboutUs_navbar = self.AboutUs_Navbar(self)
        self.phoneNumber_navbar = self.PhoneNumber_Navbar(self)
        self.bookAConsultation_navbar = self.BookAConsultation_Navbar(self)
        self.bookAConsultation_button = self.BookAConsultation_Button(self)
        self.ourServices_section = self.OurServices_Section(self)
        self.viewAllServices_button = self.ViewAllServices_Button(self)
        self.viewAllIndustries_button = self.ViewAllIndustries_Button(self)
        self.faq_section = self.FAQ_Section(self)
        self.bookACall_form = self.BookACall_Form(self)

        self.element_findYourService_navbar = "#w-dropdown-toggle-0"
        self.element_findYourService_navbarItem = ".dropdown--services-grid-item"
        self.element_serviceName = ".dropdown--services-label"
        self.element_navbar = ".navbar1_link"
        self.element_phoneNumber_navbarText = ".nav-phone"
        self.element_aboutUs_navbar = "#w-dropdown-toggle-1"
        self.element_aboutUs_navbarItem = ".navbar1_dropdown-link"
        self.element_bookAConsulation_navbar = "div.navbar1_menu-buttons a.w-button"
        self.element_bookAConsulation_button = 'a.w-button[href="/book-a-consultation"]'
        self.element_viewAllServices_button = 'a.w-button[href="/our-services"]'
        self.element_viewAllIndustries_button = (
            'a.w-button[href="/industries-we-serve"]'
        )
        self.element_faq_section = ".faq1_accordion"
        self.element_faq_content = ".paragraph-3"

    def load(self):
        with allure.step(title="Open browser"):
            self.page.goto(BASE_URL)

    def maximize_browser(self):
        with allure.step(title="Maximize browser"):
            screen_width, screen_height = pyautogui.size()
            self.page.set_viewport_size(
                {"width": screen_width, "height": screen_height}
            )

    class FindYourService_Navbar:
        def __init__(self, parent: "HomePage"):
            self.page = parent.page
            self.parent = parent

        def hover_findYourServices(self):
            with allure.step(title="Hover 'Find Your Services'"):
                self.page.hover(self.parent.element_findYourService_navbar)

        def open_navbar_item(self, index: int):
            product_locator = self.page.locator(self.parent.element_serviceName).nth(
                index
            )
            product_name = product_locator.inner_text()
            with allure.step(title=f"Click Navbar Item '{product_name}'"):
                navbar_item_locator = self.page.locator(
                    self.parent.element_findYourService_navbarItem
                ).nth(index)
                navbar_item_locator.click()

        def validate_nav_item(self, index: int):
            product_locator = self.page.locator(self.parent.element_serviceName).nth(
                index
            )
            product_name = product_locator.inner_text()
            with allure.step(title=f"Validate '{product_name}'"):
                title = self.page.locator(".heading-style-h1")
                assert (
                    title.inner_text() == "Lorem Services"
                ), f"'{product_name}' is not opened!"

    class SuccessStories_Navbar:
        def __init__(self, parent: "HomePage"):
            self.page = parent.page
            self.parent = parent

        def open_successStories_navbar(self):
            successStories_navbar = self.page.locator(self.parent.element_navbar).nth(0)
            with allure.step(title=f"Click 'Success Stories' Navbar"):
                successStories_navbar.click()

        def validate_successStories_link(self):
            with allure.step(title=f"Validate 'Success Stories' Navbar"):
                actual_url = self.page.url
                assert (
                    actual_url == f"{BASE_URL}/industries-we-serve"
                ), "'Success Stories' page is not opened!"

    class BecomeAServiceProvider_Navbar:
        def __init__(self, parent: "HomePage"):
            self.page = parent.page
            self.parent = parent

        def open_becomeAServiceProvider_navbar(self):
            becomeAServiceProvider_navbar = self.page.locator(
                self.parent.element_navbar
            ).nth(1)
            with allure.step(title=f"Click 'Become A Service Provider' Navbar"):
                becomeAServiceProvider_navbar.click()

        def validate_becomeAServiceProvider_link(self):
            with allure.step(title=f"Validate 'Become A Service Provider' Navbar"):
                actual_url = self.page.url
                assert (
                    actual_url == f"{BASE_URL}/become-a-partner"
                ), "'Become A Service Provider' page is not opened!"

    class AboutUs_Navbar:
        def __init__(self, parent: "HomePage"):
            self.page = parent.page
            self.parent = parent

        def hover_aboutUs_navbar(self):
            with allure.step(title=f"Hover 'About Us' Navbar"):
                self.page.hover(self.parent.element_aboutUs_navbar)

        def open_aboutUs_navbarItem(self, index: int):
            aboutUs_navbarItem_locator = self.page.locator(
                self.parent.element_aboutUs_navbarItem
            ).nth(index)
            aboutUs_navbarItem_name = aboutUs_navbarItem_locator.inner_text()
            with allure.step(title=f"Click Navbar Item '{aboutUs_navbarItem_name}'"):
                navbar_item_locator = self.page.locator(
                    self.parent.element_aboutUs_navbarItem
                ).nth(index)
                navbar_item_locator.click()

        def validate_nav_item(self, index: int):
            aboutUs_navbarItem_locator = self.page.locator(
                self.parent.element_aboutUs_navbarItem
            ).nth(index)
            aboutUs_navbarItem_name = aboutUs_navbarItem_locator.inner_text()
            with allure.step(title=f"Validate '{aboutUs_navbarItem_name}'"):
                title = self.page.locator(".heading-style-h1")
                if index == 0:
                    navbarItem = "Resources"
                elif index == 1:
                    navbarItem = "Careers"
                elif index == 2:
                    navbarItem = "Contact Us"
                else:
                    raise ValueError(
                        f"Invalid index {index}: Expected 0 (Resources), 1 (Careers), or 2 (Contuct Us)"
                    )

                assert (
                    title.inner_text() == f"{navbarItem}"
                ), f"'{navbarItem}' is not opened!"

    class PhoneNumber_Navbar:
        def __init__(self, parent: "HomePage"):
            self.page = parent.page
            self.parent = parent
            self.phoneNumber = None

        def open_phoneNumber_navbar(self):
            phoneNumber_list = self.phoneNumber = self.page.locator(
                self.parent.element_phoneNumber_navbarText
            ).all_inner_texts()
            self.phoneNumber = phoneNumber_list[0]
            with allure.step(title=f"Open 'Phone Number'"):
                self.page.locator(self.parent.element_phoneNumber_navbarText)
            return self.phoneNumber

        def validate_phoneNumber(self):
            actual_link = self.page.locator(
                f"a{self.parent.element_phoneNumber_navbarText}"
            ).get_attribute("href")
            if self.phoneNumber is None:
                raise ValueError(
                    "Phone Number is not set. Call open_phoneNumber_navbar() first"
                )
            with allure.step(title=f"Validate 'Phone Number' == {self.phoneNumber}"):
                assert (
                    f"{BASE_URL}/{actual_link}" == f"{BASE_URL}/tel:{self.phoneNumber}"
                ), "Phone Number is not valid!"

    class BookAConsultation_Navbar:
        def __init__(self, parent: "HomePage"):
            self.page = parent.page
            self.parent = parent

        def open_bookAConsultation_navbar(self):
            with allure.step(title=f"Click 'Book A Consulation' Navbar"):
                self.page.locator(self.parent.element_bookAConsulation_navbar).click()

        def validate_bookAConsultation_navbar(self):
            actual_url = self.page.url
            with allure.step(title=f"Validate 'Book A Consultation' Navbar"):
                assert (
                    actual_url == f"{BASE_URL}/book-a-consultation"
                ), "'Book A Consultation' Navbar not opened!"

    class BookAConsultation_Button:
        def __init__(self, parent: "HomePage"):
            self.page = parent.page
            self.parent = parent

        def open_bookAConsultation_button(self, index):
            with allure.step(title=f"Click 'Book A Consulation' Button"):
                button = self.page.locator(self.parent.element_bookAConsulation_button)
                button.nth(index).scroll_into_view_if_needed()
                button.nth(index).click()

        def validate_bookAConsultation_navbar(self):
            actual_url = self.page.url
            with allure.step(title=f"Validate 'Book A Consultation' Button"):
                assert (
                    actual_url == f"{BASE_URL}/book-a-consultation"
                ), "'Book A Consultation' Button not opened!"

    class OurServices_Section:
        def __init__(self, parent: "HomePage"):
            self.page = parent.page
            self.parent = parent
            self.formatted_number = None
            self.current_tab_name = None

        def open_services_tab(self, index):
            index = index + 1
            self.formatted_number = str(index).zfill(2) if index < 10 else str(index)
            tab_locator = self.page.locator(
                f"#splide-tabs-slide{self.formatted_number}"
            )
            tab_locator.scroll_into_view_if_needed()
            self.current_tab_name = (
                self.page.locator(".splide__tabs--text").nth(index - 1).inner_text()
            )
            with allure.step(
                title=f"Click 'Our Services' Tab: {self.current_tab_name}"
            ):
                tab_locator.click()
                time.sleep(1)
            return self.formatted_number

        def validate_services_content_active(self):
            with allure.step(
                title=f"Validate 'Our Services' Content: {self.current_tab_name}"
            ):
                element = self.page.locator(f"#cs_slider-slide{self.formatted_number}")
                class_attribute = element.get_attribute("class")
                assert (
                    "is-visible" in class_attribute
                ), "Error: is-visible not found in class"
                assert (
                    "is-active" in class_attribute
                ), "Error: is-active not found in class"

        def click_services_detail(self):
            with allure.step(
                title=f"Click 'Our Services' Detail: {self.current_tab_name}"
            ):
                button = self.page.locator(
                    f"#cs_slider-slide{self.formatted_number} a.button"
                )
                button.click()
                actual_url = self.page.url
            with allure.step(title=f"Validate 'Our Services' URL"):
                assert (
                    actual_url
                    == f"{BASE_URL}/our-services/electrical-services"  # With assumption all services detail directed to electrical services
                ), f"'Our Services' Button ({self.current_tab_name}) is not opened!"

    class ViewAllServices_Button:
        def __init__(self, parent: "HomePage"):
            self.page = parent.page
            self.parent = parent

        def open_viewAllServices_button(self, index):
            with allure.step(title=f"Click 'View All Services' Button"):
                button = self.page.locator(self.parent.element_viewAllServices_button)
                button.nth(index).scroll_into_view_if_needed()
                button.nth(index).click()

        def validate_viewAllServices_navbar(self):
            actual_url = self.page.url
            with allure.step(title=f"Validate 'View All Services' Button"):
                assert (
                    actual_url == f"{BASE_URL}/our-services"
                ), "'View All Services' Button not opened!"

    class ViewAllIndustries_Button:
        def __init__(self, parent: "HomePage"):
            self.page = parent.page
            self.parent = parent

        def open_viewAllIndustries_button(self):
            with allure.step(title=f"Click 'View All Industries' Button"):
                button = self.page.locator(self.parent.element_viewAllIndustries_button)
                button.scroll_into_view_if_needed()
                button.click()

        def validate_viewAllIndustries_link(self):
            with allure.step(title=f"Validate 'View All Industries' Button"):
                actual_url = self.page.url
                assert (
                    actual_url == f"{BASE_URL}/industries-we-serve"
                ), "'View All Industries' page is not opened!"

    class FAQ_Section:
        def __init__(self, parent: "HomePage"):
            self.page = parent.page
            self.parent = parent

        def open_FAQ(self, index):
            with allure.step(title=f"Click 'FAQ' Section index: {index}"):
                locator = self.page.locator(self.parent.element_faq_section)
                locator.nth(index).click()

        def validate_FAQ(self, index):
            with allure.step(title=f"Validate 'FAQ' Content index: {index}"):
                locator = self.page.locator(self.parent.element_faq_content)
                assert locator.nth(
                    index
                ).is_visible(), f"'FAQ' section with index: {index} cannot opened!"

    class BookACall_Form:
        def __init__(self, parent: "HomePage"):
            self.page = parent.page
            self.parent = parent

            self.element_firstName_input = "#Contact-5-Name"
            self.element_lastName_input = "#Contact-5-Name-2"
            self.element_companyName_input = "#Contact-5-Email-2"
            self.element_email_input = "#Contact-5-Name-3"
            self.element_phoneNumber_input = "#Contact-5-Name-2"
            self.element_CB_check = 'input[name="Contact-5-Checkbox"]'
            self.element_submit_button = (
                "#w-node-_75021966-9c8a-503a-8e03-708132419e77-080ad32d"
            )

        def fill_firstName(self, firstName):
            with allure.step(title=f"Fill 'First Name' Field"):
                self.page.locator(
                    self.element_firstName_input
                ).scroll_into_view_if_needed()
                self.page.locator(self.element_firstName_input).type(firstName, delay=1)

        def fill_lastName(self, lastName):
            with allure.step(title=f"Fill 'Last Name' Field"):
                self.page.locator(self.element_lastName_input).nth(0).type(
                    lastName, delay=1
                )

        def fill_companyName(self, companyName):
            with allure.step(title=f"Fill 'Company' Field"):
                self.page.locator(self.element_companyName_input).type(
                    companyName, delay=1
                )

        def fill_email(self, email):
            with allure.step(title=f"Fill 'Email' Field"):
                self.page.locator(self.element_email_input).type(email, delay=1)

        def fill_phoneNumber(self, phoneNumber):
            with allure.step(title=f"Fill 'Phone Number' Field"):
                self.page.locator(self.element_phoneNumber_input).nth(1).type(
                    phoneNumber, delay=1
                )

        def check_CB(self):
            with allure.step(title=f"Check 'Check Box' Field"):
                self.page.evaluate(
                    "document.querySelector('input[name=\"Contact-5-Checkbox\"]').click()"
                )

        def click_submit(self):
            with allure.step(title=f"Click 'Submit' Button"):
                self.page.locator(self.element_submit_button).click()

        def validate_link(self):
            with allure.step(title=f"Validate 'Book A Call' URL"):
                self.page.wait_for_url(
                    "https://facility-network-f278f6-46422f00f1ecc61.webflow.io/booked",
                    timeout=120000
                )
