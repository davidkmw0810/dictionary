from selenium import webdriver

word = input('what word do you want to find?')
country = input('choose dictionary 1.English 2.Chinese 3.French 4.Spanish')

# headless 옵션 설정
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

# Chrome 드라이버 불러오기
driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)

# naver 사전
if country == '1':
    # 단어 검색
    driver.get('https://endic.naver.com/?sLn=kr')
    driver.find_element_by_id('ac_input').send_keys(word)
    driver.find_element_by_xpath('//*[@id="top_search"]/fieldset/a[1]').click()

    # 뜻 불러오기
    driver.find_element_by_class_name('fnt_e30').click()
    means = driver.find_elements_by_class_name('fnt_k06')
    for mean in means:
        print(mean.text)

else:
    # 단어 검색
    if country == '2':
        driver.get('https://zh.dict.naver.com/#/main')
    elif country == '3':
        driver.get('https://dict.naver.com/frkodict/#/main')
    elif country == '4':
        driver.get('https://dict.naver.com/eskodict/#/main')
    driver.find_element_by_id('ac_input').send_keys(word)
    driver.find_element_by_xpath('//*[@id="searchArea"]/button').click()

    # 뜻 불러오기
    driver.find_element_by_xpath('//*[@id="searchPage_entry"]/ul/li[1]/div/a/strong').click()
    means = driver.find_elements_by_class_name('mean_item')
    for mean in means:
        print(mean.find_element_by_class_name('cont').text)

driver.close()