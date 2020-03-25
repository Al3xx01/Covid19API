from selenium import webdriver
from time import sleep
import sqlite3


class Coronavirus():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def clean(self, current):
        for x in current:
            if x.startswith('+'):
                current.remove(x)

        return current[0:3]

    def saveOnDb(self, table):
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        cur.execute('DELETE FROM DatiCovid')
        for t in table:
            current = t.split(' ')
            cleaned = self.clean(current)

            if str.isnumeric(cleaned[1]):
                cur.execute('INSERT INTO DatiCovid(country, total_cases, total_deaths) VALUES(?,?,?)', (cleaned[0], cleaned[1], cleaned[2],))
                conn.commit()


        conn.close()

    def table(self):
        table = str(self.driver.find_element_by_xpath('//*[@id="main_table_countries_today"]').text).split('\n')[10:]
        self.saveOnDb(table)


bot = Coronavirus()
bot.driver.get('https://www.worldometers.info/coronavirus/')
sleep(4)
bot.table()
