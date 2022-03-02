import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

base_url = 'https://www.imdb.com/'

def auto_search():
    driver = webdriver.Firefox()
    driver.get(base_url)

    #dropdown menu
    dropdown = driver.find_element_by_class_name('ipc-icon--arrow-drop-down')
    dropdown.click() 
    time.sleep(1)

    #advanced search from dropdown menu
    element = driver.find_element_by_link_text('Advanced Search')
    element.click()
    time.sleep(1)

    #advanced search title
    adv_title = driver.find_element_by_link_text('Advanced Title Search')
    adv_title.click()
    time.sleep(1)

    #chek the feature film checkbox
    feature_film = driver.find_element_by_id('title_type-1')
    feature_film.click()
    time.sleep(1)

    #check the tv movie checkbox
    tv_movie = driver.find_element_by_id('title_type-2')
    tv_movie.click()
    time.sleep(1)

    #start date 
    start_date = driver.find_element_by_name('release_date-min')
    start_date.click()
    start_date.send_keys('1990')  
    time.sleep(1)

    #end date 
    end_date = driver.find_element_by_name('release_date-max')
    end_date.click()
    end_date.send_keys('2020') 
    time.sleep(1)

    #rating min
    rating_min = driver.find_element_by_name('user_rating-min')
    rating_min.click()
    rating_min_drop = Select(rating_min)
    rating_min_drop.select_by_visible_text('1.0')
    time.sleep(1)

    #rating max
    rating_max = driver.find_element_by_name('user_rating-max')
    rating_max.click()
    rating_max_drop = Select(rating_max)
    rating_max_drop.select_by_visible_text('10')
    time.sleep(1)

    #oscar nominated checkbox
    oscar_nominated = driver.find_element_by_id('groups-7')
    oscar_nominated.click()
    time.sleep(1)

    #color 
    color = driver.find_element_by_id('colors-1')
    color.click()
    time.sleep(1)

    #language
    language = driver.find_element_by_name('languages')
    lang_drop = Select(language)
    lang_drop.select_by_visible_text('English')
    time.sleep(1)

    #no per page 
    no_per_page = driver.find_element_by_id('search-count')
    no_page_drop = Select(no_per_page)
    no_page_drop.select_by_index(2)
    time.sleep(1)

    # search click
    search_btn = driver.find_element_by_xpath('//button[@class="primary"]')
    search_btn.click()
    time.sleep(1)

if __name__ == '__main__':
    auto_search()