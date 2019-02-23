# Dependencies
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pandas as pd

def scrape():
    # URL of page to be scraped
    url = "https://mars.nasa.gov/news/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(response.text)


    # Find latest news title about Mars
    news_title = soup.find('div', class_="content_title").text
    news_title


    # Find latest news blurb
    news_p = soup.find('div', class_="rollover_description_inner").text
    news_p
    get_ipython().system('which chromedriver')

    # * Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.
    # * Make sure to find the image url to the full size `.jpg` image.
    # * Make sure to save a complete url string for this image.
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path)
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    featured_image = browser.find_by_id('full_image')
    featured_image.click()

    more_info = browser.find_link_by_partial_text('more info')
    more_info.click()

    # Pull featured image url
    html = browser.html
    soupsearch = BeautifulSoup(html, 'html.parser')

    part_image_url = soupsearch.find('img', class_='main_image').get('src')
    featured_image_url = 'https://www.jpl.nasa.gov' + part_image_url
    featured_image_url




    # Visit the Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en) 
    # and scrape the latest Mars weather tweet from the page. Save the tweet text for the weather
    # report as a variable called `mars_weather`.
    url = "https://twitter.com/marswxreport?lang=en"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    mars_weather = soup.find('div', class_='js-tweet-text-container').text
    mars_weather

    # Pull Mars facts table from Space-Facts
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path)
    url = 'https://space-facts.com/mars/'
    marsFacts_df = pd.read_html(url)
    marsFacts_df = marsFacts_df[0]
    marsFacts_df

    # * Use Pandas to convert the data to a HTML table string.
    marsFacts_df.to_html('mars_facts.html', index=False)

    # Scrape Hemisphere image urls
    executable_path = {'executable_path': 'chromedriver.exe'}
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

    # html = browser.html
    # soupsearch = BeautifulSoup(html, 'html.parser')

    schiaparelli_url = soupsearch.find('img', class_='wide-image').get('src')
    schiaparelli_img_url = astrogeology_url + schiaparelli_url

    back = browser.find_link_by_partial_text('Back')
    back.click()

    #---------------------------------------

    syrtis = browser.find_link_by_partial_text('Syrtis')
    syrtis.click()

    # html = browser.html
    # soupsearch = BeautifulSoup(html, 'html.parser')

    syrtis_url = soupsearch.find('img', class_='wide-image').get('src')
    syrtis_img_url = astrogeology_url + syrtis_url

    back = browser.find_link_by_partial_text('Back')
    back.click()

    valles = browser.find_link_by_partial_text('Valles')
    valles.click()

    # html = browser.html
    # soupsearch = BeautifulSoup(html, 'html.parser')

    valles_url = soupsearch.find('img', class_='wide-image').get('src')
    valles_img_url = astrogeology_url + valles_url
    valles_img_url


    print(cerberus_img_url, schiaparelli_img_url, syrtis_img_url, valles_img_url)

    # Save hemisphere image urls in a dictionary.
    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": valles_img_url},
        {"title": "Cerberus Hemisphere", "img_url": cerberus_img_url},
        {"title": "Schiaparelli Hemisphere", "img_url": schiaparelli_img_url},
        {"title": "Syrtis Major Hemisphere", "img_url": syrtis_img_url},
    ]

    return(hemisphere_image_urls)