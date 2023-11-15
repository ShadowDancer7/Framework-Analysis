from pages.resetPasswordPage_BlazeDemo import BlazeDemoResetPasswordPage
from utilities import excelReader
import pytest

@pytest.mark.usefixtures("setup_and_teardown")
class TestBlazeDemoResetPasswordPage:

    @pytest.mark.parametrize("emailAddress", 
                             excelReader.get_data_from_excel("C:/Users/Shado/Documents/Framework_Analysis_10/virtual_env/ExcelFiles/BlazeDemoResetPassword.xlsx", "Email"))
    def test_password_reset_page(self, emailAddress):
        enter_email_address = BlazeDemoResetPasswordPage(self.driver)
        enter_email_address.enter_email_address(emailAddress)

        click_send_password_reset_link_button = BlazeDemoResetPasswordPage(self.driver)
        click_send_password_reset_link_button.click_password_reset_button()
