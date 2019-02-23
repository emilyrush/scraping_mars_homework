# Dependencies
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pandas as pd
import time

def scrape():
    ### NASA Mars News
    url = "https://mars.nasa.gov/news/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    news_title = soup.find('div', class_="content_title").text
    news_title

    news_p = soup.find('div', class_="rollover_description_inner").text
    news_p

    ### JPL Mars Space Images - Featured Image
    executable_path = {'executable_path': 'C:/Users/emrus/chromedriver.exe'}
    browser = Browser('chrome', **executable_path)
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    time.sleep(3)
    featured_image = browser.find_by_id('full_image')
    featured_image.click()
    time.sleep(3)
    more_info = browser.find_link_by_partial_text('more info')
    more_info.click()

    html = browser.html
    soupsearch = BeautifulSoup(html, 'html.parser')

    part_image_url = soupsearch.find('img', class_='main_image').get('src')
    featured_image_url = 'https://www.jpl.nasa.gov' + part_image_url
    featured_image_url

    ### Mars Weather
    url = "https://twitter.com/marswxreport?lang=en"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    mars_weather = soup.find('div', class_='js-tweet-text-container').text
    mars_weather

    ### Mars Facts
    # executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path)
    url = 'https://space-facts.com/mars/'
    marsFacts_df = pd.read_html(url)
    marsFacts_df = marsFacts_df[0]
    marsFacts_df


    marsFacts_df.to_html()

    ### Mars Hemispheres
    # executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path)
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    cerberus = browser.find_link_by_partial_text('Cerberus')
    cerberus.click()

    html = browser.html
    soupsearch = BeautifulSoup(html, 'html.parser')

    astrogeology_url = 'https://astrogeology.usgs.gov/'
    #---------------------------------------
    cerberus_url = soupsearch.find('img', class_='wide-image').get('src')
    cerberus_img_url = astrogeology_url + cerberus_url


    back = browser.find_link_by_partial_text('Back')
    back.click()
    #---------------------------------------
    schiaparelli = browser.find_link_by_partial_text('Schiaparelli')
    schiaparelli.click()

    html = browser.html
    soupsearch = BeautifulSoup(html, 'html.parser')

    schiaparelli_url = soupsearch.find('img', class_='wide-image').get('src')
    schiaparelli_img_url = astrogeology_url + schiaparelli_url

    back = browser.find_link_by_partial_text('Back')
    back.click()

    #---------------------------------------

    syrtis = browser.find_link_by_partial_text('Syrtis')
    syrtis.click()

    html = browser.html
    soupsearch = BeautifulSoup(html, 'html.parser')

    syrtis_url = soupsearch.find('img', class_='wide-image').get('src')
    syrtis_img_url = astrogeology_url + syrtis_url

    back = browser.find_link_by_partial_text('Back')
    back.click()

    valles = browser.find_link_by_partial_text('Valles')
    valles.click()

    html = browser.html
    soupsearch = BeautifulSoup(html, 'html.parser')

    valles_url = soupsearch.find('img', class_='wide-image').get('src')
    valles_img_url = astrogeology_url + valles_url
    valles_img_url


    print(cerberus_img_url, schiaparelli_img_url, syrtis_img_url, valles_img_url)

    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": valles_img_url},
        {"title": "Cerberus Hemisphere", "img_url": cerberus_img_url},
        {"title": "Schiaparelli Hemisphere", "img_url": schiaparelli_img_url},
        {"title": "Syrtis Major Hemisphere", "img_url": syrtis_img_url},
    ]

    hemisphere_image_urls
#---------------------------------------
# Create results dictionary

    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_weather": mars_weather,
        "mars_facts" : marsFacts_df.to_html,
        "hemisphere_image_urls": hemisphere_image_urls
    }
    return mars_data