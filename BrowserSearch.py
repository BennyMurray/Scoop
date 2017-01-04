import mechanize
from bs4 import BeautifulSoup
import re


def browsersearch(searchterm):
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.set_handle_equiv(False)
    br.addheaders = [('User-agent', 'Mozilla/5.0')]
    br.open('http://www.google.com/')

    # do the query
    br.select_form(name='f')
    br.form['q'] = searchterm
    data = br.submit()
    soup = BeautifulSoup(data.read(), "html.parser")
    links = soup.find_all('a')

    try:
        code = re.findall(r"www\.ratebeer\.com\/beer\/[\w+-/]+[0-9]", str(links))[0]
        return ''.join(re.findall(r"[0-9]+",code))

    #In event no result is found
    except IndexError:
        return None

