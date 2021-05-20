import time
import os
import datetime
from cdrive import ChromeDrive

dir_path = os.path.dirname(os.path.realpath(__file__))
today = datetime.datetime.today().strftime('%m-%d-%Y')

url = 'https://www.psychologytoday.com/us'

def test_headers_and_links():
    driver = ChromeDrive(url)
    assert driver.wait_for_link('/us', 'Psychology Today')

    assert driver.wait_for_link('/us/news', 'News')
    assert driver.click_by_css_selector("body > div.container.mb-3 > div > div.container.main.main--sidebar.mx-0 > div > div.col-12.col-sm-10.col-lg-12.col-xl-3.order-xl-first > div > div > div.card-header > h2 > a")
    assert driver.get_url() == 'https://www.psychologytoday.com/us/news'
    assert driver.click_by_css_selector("#block-mainnavbarblock > div > div > nav > h1 > a")
    assert driver.get_url() == url
    assert driver.wait_for_text('h2', 'card-title', 'Most Popular')
    assert driver.wait_for_text('h2', 'section-title', 'The Latest')
    assert driver.wait_for_text('h2', 'card-title', 'Meet Our Experts')

    assert driver.click_by_css_selector("body > div.container.mb-3 > div > div.col-12.col-sm-10.col-lg-12 > div > div.row.align-items-inherit.no-gutters.pb-0.mt-2.td_callout > div.td_callout__fat.px-3.px-sm-5 > div > div > h2 > a")
    assert driver.get_url() == "https://www.psychologytoday.com/us/therapists"
    assert driver.click_by_css_selector("#logo-menu-container > span > a")
    assert url in driver.get_url()

    time.sleep(1)
    driver.teardown()

if __name__ == '__main__':
    test_headers_and_links()

    print('END OF LINE.')
