from mechanize import Browser
from bs4 import BeautifulSoup as BS
from Textcleaner import cleanText
import urllib2

#number of pages to scrape
numOfPages = 10

br = Browser()

# Browser options
# Ignore robots.txt. Do not do this without thought and consideration.
br.set_handle_robots(False)

# Don't add Referer (sic) header
br.set_handle_referer(False)

# Don't handle Refresh redirections
br.set_handle_refresh(False)

#Setting the user agent as firefox
br.addheaders = [('User-agent', 'Firefox')]


def scrapeReviews(beername, beerID):
    stringDump = ""



    print "Scraping reviews for ", beername + "..."
    if beerID != None:
        #Scroll through pages
        for page in range(1, numOfPages+1):
            if page == 1:
                try:
                    br.open('https://www.ratebeer.com/beer/'+beerID+'/')
                    redirected_url = br.geturl()
                except urllib2.HTTPError, error:
                    "HTTP 500 ERROR"
                    break
            else:
                br.open(redirected_url+'1/'+str(page)+"/")

            #Getting the response in beautifulsoup
            soup = BS(br.response().read(),'html.parser')
            #print br.geturl()

            #Generate a resultset of reviews by their unique inline css styling
            reviews = soup.findAll('div', style="padding: 20px 10px 20px 0px; border-bottom: 1px solid #e0e0e0; line-height: 1.5;")

            #Iterate through result set and add to stringDump list
            stringDump += "".join(i.text for i in reviews)
            print "success",
    else:
        print "failed"
        pass



    return cleanText(stringDump)


