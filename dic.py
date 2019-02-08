from selenium import webdriver

# word = input('what word do you want to find?')
# country = input('choose dictionary 1.English 2.Chinese 3.French 4.Spanish')

word = 'pomme'
country = '2'
driver = webdriver.Chrome('chromedriver.exe')

# naver 사전
if country == '1':
    driver.get('https://endic.naver.com/?sLn=kr')
    driver.find_element_by_id(ac_input).send_keys(word)
    
elif country == '2':
    driver.get('https://zh.dict.naver.com/#/main')
elif country == '3':
    driver.get('https://dict.naver.com/frkodict/#/main')
elif country == '4':
    driver.get('https://dict.naver.com/eskodict/#/main')