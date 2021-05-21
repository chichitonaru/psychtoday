import time
from rdrive import RemoteDrive

url = 'https://www.psychologytoday.com/us/therapists'

def test_therapist_search():
    driver = RemoteDrive(url)
    assert driver.wait_for_link('https://www.psychologytoday.com/us?tr=Hdr_Brand', 'Psychology Today')
    assert driver.type_by_id('autosuggestSearchInput', 'Snohomish')
    assert driver.click_by_id('searchSubmit')

    assert driver.get_url() == 'https://www.psychologytoday.com/us/therapists?search=Snohomish'
    assert driver.wait_for_link('https://www.psychologytoday.com/us?tr=Hdr_Brand', 'Psychology Today')
    assert driver.wait_for_text_no_class('h1', 'Therapists in Snohomish, WA')

    time.sleep(1)
    driver.teardown()

def test_therapist_search_no_results():
    driver = RemoteDrive(url)
    assert driver.wait_for_link('https://www.psychologytoday.com/us?tr=Hdr_Brand', 'Psychology Today')
    assert driver.type_by_id('autosuggestSearchInput', 'Yu-Gi-Oh')
    assert driver.click_by_id('searchSubmit')

    assert driver.get_url() == 'https://www.psychologytoday.com/us/therapists?search=Yu-Gi-Oh'
    assert driver.wait_for_link('https://www.psychologytoday.com/us?tr=Hdr_Brand', 'Psychology Today')
    assert driver.wait_for_text_no_class('h2', 'No Results for “Yu-Gi-Oh”\n')
    assert driver.wait_for_text_no_class('h3', 'Suggestions:')
    assert driver.wait_for_text_no_class('h3', 'Browse by Country:')

    time.sleep(1)
    driver.teardown()

def test_teletherapy_search():
    driver = RemoteDrive(url)
    assert driver.wait_for_link('https://www.psychologytoday.com/us?tr=Hdr_Brand', 'Psychology Today')
    assert driver.click_by_id('profClassSelectText')
    assert driver.click_by_css_selector('#profClassMenu > span:nth-child(2)')
    assert driver.type_by_id('autosuggestSearchInput', 'Snohomish')
    assert driver.click_by_id('searchSubmit')

    assert driver.get_url() == 'https://www.psychologytoday.com/us/therapists/online-counseling?search=Snohomish'
    assert driver.wait_for_link('https://www.psychologytoday.com/us?tr=Hdr_Brand', 'Psychology Today')
    assert driver.wait_for_text_no_class('h1', 'Teletherapy for Snohomish, WA')

    time.sleep(1)
    driver.teardown()

if __name__ == '__main__':
    test_therapist_search()
    test_therapist_search_no_results()
    test_teletherapy_search()

    print('END OF LINE.')