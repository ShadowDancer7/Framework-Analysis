from pages.loginPage_BlazeDemo import BlazeDemoLogin
from utilities import excelReader
import pytest

@pytest.mark.usefixtures("setup_and_teardown")
class TestBlazeDemoLogin:

    @pytest.mark.parametrize("emailAddress, password", 
                             excelReader.get_data_from_excel("C:/Users/Shado/Documents/Framework_Analysis_10/virtual_env/ExcelFiles/BlazeDemoLoginCredentials.xlsx", "Login"))
    def test_blazedemo_login_credentials(self, emailAddress, password):
        type_email_address = BlazeDemoLogin(self.driver)
        type_email_address.enter_email(emailAddress)

        type_password = BlazeDemoLogin(self.driver)
        type_password.enter_password(password)

        click_button = BlazeDemoLogin(self.driver)
        click_button.click_login_button()