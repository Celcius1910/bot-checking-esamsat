import pytest
from pages import HomePage
import allure
from faker import Faker


@allure.severity(allure.severity_level.NORMAL)
@allure.feature("Find Your Service Navbar")
@allure.story("Navbar Item")
@pytest.mark.parametrize("index", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
def test_open_findYourService_navbar(page, index):
    home_page = HomePage(page)
    home_page.load()
    home_page.findYourService_navbar.hover_findYourServices()
    home_page.findYourService_navbar.open_navbar_item(index)
    home_page.findYourService_navbar.validate_nav_item(index)


@allure.severity(allure.severity_level.NORMAL)
@allure.feature("'Success Stories' Navbar")
def test_open_successStories_navbar(page):
    home_page = HomePage(page)
    home_page.load()
    home_page.successStories_navbar.open_successStories_navbar()
    home_page.successStories_navbar.validate_successStories_link()


@allure.severity(allure.severity_level.NORMAL)
@allure.feature("'Become A Service Provider' Navbar")
def test_open_becomeAServiceProvider_navbar(page):
    home_page = HomePage(page)
    home_page.load()
    home_page.becomeAServiceProvider_navbar.open_becomeAServiceProvider_navbar
    home_page.becomeAServiceProvider_navbar.validate_becomeAServiceProvider_link()


@allure.severity(allure.severity_level.NORMAL)
@allure.feature("'About Us' Navbar")
@pytest.mark.parametrize("index", [0, 1, 2])
def test_open_aboutUs_navbar(page, index):
    home_page = HomePage(page)
    home_page.load()
    home_page.aboutUs_navbar.hover_aboutUs_navbar()
    home_page.aboutUs_navbar.open_aboutUs_navbarItem(index)
    home_page.aboutUs_navbar.validate_nav_item(index)


@allure.severity(allure.severity_level.NORMAL)
@allure.feature("'Phone Number' Navbar")
def test_open_phoneNumber_navbar(page):
    home_page = HomePage(page)
    home_page.load()
    home_page.maximize_browser()
    home_page.phoneNumber_navbar.open_phoneNumber_navbar()
    home_page.phoneNumber_navbar.validate_phoneNumber()


@allure.severity(allure.severity_level.NORMAL)
@allure.feature("'Book A Consultation' Navbar")
def test_open_bookAConsultation_navbar(page):
    home_page = HomePage(page)
    home_page.load()
    home_page.bookAConsultation_navbar.open_bookAConsultation_navbar()
    home_page.bookAConsultation_navbar.validate_bookAConsultation_navbar()


@allure.severity(allure.severity_level.NORMAL)
@allure.feature("'Book A Consultation' Button")
@pytest.mark.parametrize("index", [0, 1, 2, 3, 4, 5, 6, 7])
def test_open_bookAConsultation_button(page, index):
    home_page = HomePage(page)
    home_page.load()
    home_page.bookAConsultation_button.open_bookAConsultation_button(index)
    home_page.bookAConsultation_button.validate_bookAConsultation_navbar()


@allure.severity(allure.severity_level.NORMAL)
@allure.feature("'Our Services' Section")
@pytest.mark.parametrize("index", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
def test_ourService_section(page, index):
    home_page = HomePage(page)
    home_page.load()
    home_page.ourServices_section.open_services_tab(index)
    home_page.ourServices_section.validate_services_content_active()
    home_page.ourServices_section.click_services_detail()


@allure.severity(allure.severity_level.NORMAL)
@allure.feature("'View All Services' Button")
@pytest.mark.parametrize("index", [0, 1])
def test_open_viewAllServices_button(page, index):
    home_page = HomePage(page)
    home_page.load()
    home_page.viewAllServices_button.open_viewAllServices_button(index)
    home_page.viewAllServices_button.validate_viewAllServices_navbar()


@allure.severity(allure.severity_level.NORMAL)
@allure.feature("'View All Industries' Button")
def test_open_viewAllIndustries_button(page):
    home_page = HomePage(page)
    home_page.load()
    home_page.viewAllIndustries_button.open_viewAllIndustries_button()
    home_page.viewAllIndustries_button.validate_viewAllIndustries_link()


@allure.severity(allure.severity_level.NORMAL)
@allure.feature("'FAQ' Section")
@pytest.mark.parametrize("index", [0, 1, 2, 3, 4])
def test_open_faq_section(page, index):
    home_page = HomePage(page)
    home_page.load()
    home_page.faq_section.open_FAQ(index)
    home_page.faq_section.validate_FAQ(index)


faker = Faker()


@allure.severity(allure.severity_level.BLOCKER)
@allure.feature("'Book A Call' Form")
@pytest.mark.parametrize(
    "data",
    [
        {
            "firstName": faker.first_name(),
            "lastName": faker.last_name(),
            "companyName": faker.company(),
            "email": faker.safe_email(),
            "phoneNumber": faker.basic_phone_number()
        }
    ]
)
def test_open_bookACall_form(page, data):
    home_page = HomePage(page)
    home_page.load()
    home_page.bookACall_form.fill_firstName(data["firstName"])
    home_page.bookACall_form.fill_lastName(data["lastName"])
    home_page.bookACall_form.fill_companyName(data["companyName"])
    home_page.bookACall_form.fill_email(data["email"])
    home_page.bookACall_form.fill_phoneNumber(data["phoneNumber"])
    home_page.bookACall_form.check_CB()
    home_page.bookACall_form.click_submit()
    home_page.bookACall_form.validate_link()
