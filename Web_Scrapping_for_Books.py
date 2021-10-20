from selenium import webdriver
from bs4 import BeautifulSoup

class book:
    name = ""
    author = ""
    ISBN = ""
    pages = ""
    price = ""
        
        
driver = webdriver.Chrome(executable_path = 'C:\\Users\m_nou\Downloads\chromedriver_win32 (1)\chromedriver.exe')
array = []
for i in range(1,5):    
    basic = 'https://readings.com.pk/pages/category.aspx?Category=51&Level=Level1&Sortby=ArrivalDate&BookType=N&Page='
    link = basic + str(i)
    driver.get(link)
   
    content = driver.page_source
    soup = BeautifulSoup(content)
     
    for s in soup.findAll('div', attrs = {'class': 'product_detail_page_outer_colum'}):
        name = s.find('div', attrs = {'class':'product_detail_page_left_colum_author_name'}).find('h5').find('a').text #name
        author = s.find('div', attrs = {'class':'product_detail_page_left_colum_author_name'}).find('h6').find('a').text #author
        price = s.find('div', attrs = {'class': 'col-md-6 no_padding'}).find('div',attrs = {'class': 'our_price'}).find('h6').find('span',attrs = {'class':'linethrough'}).text #price
        ISBN = s.find('div' , attrs = {'class','col-md-6 no_padding'}).find('div',attrs = {'class': 'books_publisher'}).find('h6').text.split("|")[1].split(":")[1] # isbn
        pages = s.find('div' , attrs = {'class','col-md-6 no_padding'}).find('div',attrs = {'class': 'books_publisher'}).find('h6').text.split("|")[2].split(":")[1] #pages
        obj = book()
        obj.name = name
        obj.author = author
        obj.ISBN = ISBN
        obj.pages = pages
        obj.price = price
        print("Book Name: " + str(obj.name))
        print("ISBN: " + str(obj.ISBN) + "    Pages: "+ str(obj.pages) + "      Price: " + str(obj.price))
        array.append(obj)
#for i in array:
#    print("Book Name: " + str(i.name))
#    print("ISBN: " + str(i.ISBN) + " Pages: "+ str(i.pages) + " Price: " + str(i.price))
