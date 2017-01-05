# -*- coding: utf-8 -*-

from mechanize import Browser
from bs4 import BeautifulSoup
import re
from time import sleep

br = Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1'), ('Accept', '*/*')]


def getGeoLocation(ip_address):

        page = br.open("http://www.ip-tracker.org/locator/ip-lookup.php?ip="+ip_address)
        soup = BeautifulSoup(page, "html.parser")
        td = soup.findAll("td", {"class": "tracking lessimpt"})

        location = re.findall(r"[A-Z][a-z]+", str(td))
        return "".join(location)


