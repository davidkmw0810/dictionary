from selenium import webdriver

# word = input('what word do you want to find?')
# country = int(input('choose dictionary 1.English 2.Korean 3.Hanja 4.Japanese 5.Chinese 6.French 7.Spanish 8.German'))

word = 'pomme'
country = 6
driver = webdriver.Chrome('chromedriver.exe')

# naver 사전
driver.get('https://dict.naver.com/')

# 사전별로 링크 클릭해서 들어가기
dics = driver.find_elements_by_class_name("Nnav_cell")
dics[country].click()

# 검색
driver.find_element_by_id('ac_input').send_keys(word)
driver.find_element_by_class_name('btn_search').click()

# 긁어오기
mean = driver.find_element_by_class_name('fnt_k05').text
print(mean)
