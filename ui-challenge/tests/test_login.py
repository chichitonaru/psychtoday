import time
from cdrive import ChromeDrive

url = 'https://member.psychologytoday.com/us/login'

def test_login_no_password():
    driver = ChromeDrive(url)
    assert driver.wait_for_text_no_class('h1', 'Welcome Back')
    assert driver.type_by_id('edit-user_name', 'username')
    assert driver.click_by_css_selector('#form-login_form > div.form-actions > button')
    assert driver.wait_for_text('small', 'form-text text-muted', 'Password field is required')

    time.sleep(1)
    driver.teardown()

def test_login_no_username():
    driver = ChromeDrive(url)
    assert driver.wait_for_text_no_class('h1', 'Welcome Back')
    assert driver.type_by_id('edit-password', 'password')
    assert driver.click_by_css_selector('#form-login_form > div.form-actions > button')
    assert driver.wait_for_text('small', 'form-text text-muted', 'Username field is required')

    time.sleep(1)
    driver.teardown()

if __name__ == '__main__':
    test_login_no_password()
    test_login_no_username()

    print('END OF LINE.')
