from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Chrome('C:\\Program Files (x86)\\Google\\chromedriver.exe')
text_search = 'iphone 12 mini'
websites = ['https://www.newegg.com', 'https://www.bhphotovideo.com']


def site_login():
    for item in websites:
        driver.get(item)

        if 'bhp' in item:
            driver.find_element_by_xpath('//*[@id="top-search-input"]').send_keys(text_search)
            driver.find_element_by_xpath('//*[@id="header"]/section[1]/div[1]/form/p/button').click()
            driver.find_elements_by_partial_link_text(text_search)
            bhp_descr = driver.find_element_by_xpath('//*[@id="listingRootSection"]/div/div[3]/section/div[2]/div[1]'
                                                     '/div/div[2]/h3/a/span').text
            print("BHP Description: ", bhp_descr)
            bhp_price = driver.find_element_by_xpath('//*[@id="listingRootSection"]/div/div[3]/section/div[2]/div[1]'
                                                     '/div/div[3]/div[1]/div[1]/div[1]/span/span').text
            try:
                bhp_original_price = driver.find_element_by_xpath('//*[@id="listingRootSection"]/div/div[3]/section'
                                                                  '/div[2]/div[1]/div/div[3]/div[1]/div/del').text
                print("BHP Original Price: ", bhp_original_price)
            except NoSuchElementException:
                bhp_original_price = 'Not Found'
            print("BHP Price: ", bhp_price.strip())
            driver.implicitly_wait(5)

        if 'newegg' in item:
            driver.find_element_by_xpath('//*[@id="app"]/header/div[1]/div[3]/div[1]/form/div/div[1]/input').\
                send_keys(text_search)
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/header/div[1]/div[3]/'
                                                                                  'div[1]/form/div/div[2]/button'))).click()
            try:
                new_egg_discount_price = driver.find_element_by_xpath("//*[starts-with(@id, 'item_cell_')]").text
                print("NewEgg Description/ Price: ", new_egg_discount_price.split("Free")[0])
            except NoSuchElementException:
                new_egg_discount_price = 'Not Found'
                print(new_egg_discount_price)

        #if 'amazon' in item:
        #    driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]').send_keys(text_search)
        #    driver.find_element_by_id('nav-search-submit-button').click()
        #
        #    try:
        #        amazon_price = driver.find_element_by_xpath("//a[starts-with@class='a-link-normal").text
        #    except NoSuchElementException:
        #        amazon_price = 'Not Found'
        #    driver.implicitly_wait(5)
        #    print("Amazon Price: ", amazon_price)



        #if 'google' in item:
        #    driver.find_element_by_xpath('//*[@id="REsRA"]').send_keys(text_search)
        #    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kO001e"]/c-wiz/form/div[2]/div[2]/ul/li[1]/div/div[1]'))).click()
        #    try:
        #        text = 'compare prices from'
        #        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, text))).click()
        #        print("found")
        #        check_all_vendors = driver.find_element_by_xpath("//*[starts-with(@id, 'rso')]").text
        #        vendor_1_name = driver.find_element_by_xpath('//*[@id="rso"]/div[2]/div[1]/div[3]/div/div[2]/div/div/div/div/div[1]/div[2]/div[4]/div[3]/div[1]/a/div/div[3]/span').text
        #    except NoSuchElementException:
        #        vendor_1_price = 'Not Found'
        #        vendor_1_name = 'Not Found'
        #        print(vendor_1_name, ' = ', vendor_1_price)

    # driver.quit()

if __name__ == "__main__":
    site_login()

'''
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@id='pixlee_lightbox_iframe']")))
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@ass='vote_button mfp-voteText']"))).click()

//*[@id="search"]/div[1]/div/div[1]/div/span[3]/div[2]/div[2]/div/span/div/div/div/div/div[2]/div[2]/div/div[1]/h2/a/span
'''
