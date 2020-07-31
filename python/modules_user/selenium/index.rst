.. title:: python selenium

.. meta::
    :description:
        Справочная информация по python модулю selenium.
    :keywords:
        python selenium

.. py:module:: selenium

selenium
========

.. code-block:: sh

    pip install selenium

.. code-block:: py

    from selenium import webdriver

    chromedriver = "chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chromedriver)

    geckodriver = "geckodriver.exe"
    driver = webdriver.Firefox(executable_path=geckodriver)

    iedriver = "IEDriverServer.exe"
    driver = webdriver.Firefox(executable_path=iedriver)

    driver = webdriver.Safari()
    
    driver.delete_cookie(cookie_item)
    driver.delete_all_cookies()
    driver.get_cookies()
    driver.page_source

    driver.set_window_size(1600, 1200)

    driver.get(url)
    elemeny = driver.find_element_by_id('register')
    elemeny = driver.find_element_by_class_name('register')
    elemeny = driver.find_element_by_tag_name('div')
    elemeny = driver.find_element_by_link_text('link text')
    elemeny = driver.find_element_by_partial_link_text('partial link text')

    elemeny = driver.find_element_by_css_selector('a[href="/sign-up"]')
    element.click()
    element.send_keys('email')
    element.send_keys(Keys.RETURN)

    select_element = Select(element)
    select_element.select_by_visible_text('Russia')
    select_element.select_by_value('Russia')
    select_element.select_by_index(1)

    driver.save_screenshot('1.png')

    driver.execute_script(js_code)

    iframe = driver.find_element_by_id(iframe_id)
    driver.switch_to.frame(the_iframe)
    element = driver.find_element_by_id(the_element_id)
    element.send_keys('41111111111111')
    driver.switch_to.default_content()

    driver.switch_to.alert.accept()
    driver.refresh()

    # hover
    ActionChains(driver).move_to_element(the_element).perform()

    # right click
    ActionChains(driver).context_click(the_element).perform()

    # click offset
    the_element = driver.find_element_by_id(the_id)
    offset = ActionChains(driver).move_to_element_with_offset(the_element,x,y)
    offset.click()
    offset.perform()

    # add extension
    options = webdriver.ChromeOptions()
    options.add_extension(extension_path)
    driver = webdriver.Chrome(
        executable_path = chromedriver, 
        chrome_options = options
    )

    # Simulate webcam and microphone
    options = webdriver.ChromeOptions()
    options.add_argument("--use-fake-ui-for-media-stream")
    options.add_argument("--use-fake-device-for-media-stream")
    driver = webdriver.Chrome(
        executable_path = chromedriver, 
        chrome_options = options
    )

    # Emulate mobile device
    google_pixel_3_xl_user_agent = 'Mozilla/5.0 (Linux; Android 9.0; Pixel 3 XL Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko)
    pixel_3_xl_emulation = {
       "deviceMetrics": {
          "width": 411, 
          "height": 731, 
          "pixelRatio": 3
       },
       "userAgent": google_pixel_3_xl_user_agent
    }
    options = webdriver.ChromeOptions()
    options.add_experimental_option("mobileEmulation", pixel_3_xl_emulation)
    driver = webdriver.Chrome(
       executable_path = chromedriver, 
       chrome_options = options)

    # Change the user agent string    
    options = webdriver.ChromeOptions()
    options.add_argument('--user-agent = '+ the_user_agent)
    driver = webdriver.Chrome(
       executable_path = chromedriver, 
       chrome_options = options)

    # page load timeout
    driver.set_page_load_timeout(20)

    # element load timeout
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, the_id)))