from selenium import webdriver
import time, datetime
import requests, bs4
import socket
import pickle
from Crypto.Hash import MD5
import sys
from webdriver_manager.chrome import ChromeDriverManager


def connected():
    try:
        return True
        socket.create_connection(("www.google.com", 80))
    except Exception:
        return False


def toHash(msg):
    return MD5.new(msg.encode("utf-8")).hexdigest()


class watsapp_bot():
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def login(self):
        self.driver.get('https://web.whatsapp.com')
        input('Press Enter when after scanning')

    def busy(self):
        def reply(self):
            inp = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            inp.send_keys('This is an automated generated Text.Hitesh is currently busy.')
            self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]').click()

        self.names = ['Rishika', 'Cinderella', 'Saaand', 'Lulla']
        while True:
            links = self.driver.find_elements_by_class_name('X7YrQ')
            for link in links:
                if len(link.text.split('\n')) is 4 and link.text.split('\n')[-1].isdigit():
                    dt = datetime.datetime.now().time()
                    dt = dt.hour, dt.minute
                    if dt == tuple([int(i) for i in link.text.split('\n')[1].split(':')]):
                        print(link.text)
                        link.click()
                        reply(self)
            time.sleep(2)

    def spam(self, name='notes', message='hey', times=10):
        self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/input').send_keys(name)
        names = self.driver.find_elements_by_class_name('_19RFN')
        for chat in names:
            if chat.text.lower() == name.lower():
                chat.click()
                time.sleep(0.5)
                inp = self.driver.find_element_by_class_name('_3u328')
                for i in range(times):
                    inp.send_keys(message)
                    self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
                return
    def check_online(self,name='Saakshi'):
        start=None
        self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys(name)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[6]/div/div/div[2]').click()
        online=False
        while True:
            try:
                self.driver.find_element_by_xpath('//*[@id="main"]/header/div[2]/div[2]/span')
                start = time.time()
                print(datetime.datetime.now().time())
                while True:
                    time.sleep(10)
                    try:
                        self.driver.find_element_by_xpath('//*[@id="main"]/header/div[2]/div[2]/span')
                    except:
                        print(time.time()-start)
                        break
            except Exception as e:
                time.sleep(10)



    def news(self):
        f = open('Hash_CV.ser', "rb")
        sourcelink = 'https://timesofindia.indiatimes.com/coronavirus/india'
        res = requests.get(sourcelink)
        html = bs4.BeautifulSoup(res.text, "html.parser")
        linksource = html.select_one('.w_tle').select('a')
        link = linksource[0]['href']
        group = 'Notes'
        texts = pickle.load(f)
        change = False
        start=datetime.datetime.fromtimestamp(time.time())
        for chat in self.driver.find_elements_by_class_name('_2WP9Q'):
            if group in chat.text:
                chat.click()
                break
        while True:
            if connected():
                try:
                    res = requests.get(link)
                    html = bs4.BeautifulSoup(res.text, "html.parser")
                    newEl = html.select_one('._1KydD')
                    if newEl.select_one('b').text.lower() not in texts:
                        headt = newEl.select_one('b').text
                        head = '*' + headt + '*'
                        bodys = newEl.select('p')
                        if len(bodys) > 1:
                            body = bodys[1].text
                            head += '.' + body
                        if '</a>' in str(newEl):
                            head += ' ' + newEl.select_one('a')['href']
                        if '<img' in str(newEl):
                            head += ' ' + newEl.select_one('img')['src']
                        texts.append(headt.lower())
                        texts = texts[1:]
                        print(texts, head, datetime.datetime.now(), sep='\n')
                        self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(
                            head)
                        self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]').click()
                        start=datetime.datetime.now()
                    '''if 0< datetime.datetime.now().hour < 12:
                        change = True
                    if change:
                        linksource = html.select_one('.IXtDK').select('a')
                        newlink = linksource[0]['href']
                        if newlink != link:
                            link = newlink
                            change = False
                            start=datetime.datetime.fromtimestamp(time.time())'''
                    time.sleep(20)
                except KeyboardInterrupt:
                    f.close()
                    f = open('Hash_CV.ser', "wb")
                    pickle.dump(texts, f)
                    f.close()
                    print(1)
                    print(texts)
                    sys.exit()
                except Exception as e:
                    print(e)
            else:
                print("Check network")

    def pause(self):
        input('Press enter 2 times to resume')
        input()


w = watsapp_bot()
w.login()
w.news()

