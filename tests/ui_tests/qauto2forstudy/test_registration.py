import time

def test_registration(driver, registration_page, main_page):
    registration_page.get_dialog_window()
    registration_page.fill_forms()
    time.sleep(2)
    #check_new_url()
    main_page.check_header_items()
    assert (driver.current_url == "https://guest:welcome2qauto@qauto2.forstudy.space/panel/garage"), \
       "Incorrect URL opens after registration"

