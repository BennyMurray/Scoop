![splashlogo-02](https://cloud.githubusercontent.com/assets/17185335/21775764/4a6dbb5c-d68f-11e6-90cc-5cb98d576d22.png)


#What is Scoop?

Scoop is a craft beer search-engine that autonomously generates data through web-scraping and semantic analysis.


#To build project:

###Install the following dependencies via pip or equivalent:


* Django

* djangorestframework

* bs4

* mechanize

* nltk

* Django-cors-headers


###Download nltk library:

* Run the python script: ‘nltk downloader.py’

* In the GUI, select ‘download all’


###Migrate the database:

* Python manage.py makemigrations ScoopApp

* Python manage.py migrate


###Load the sample database:

* Python loadSampleDB.py 


###Run the server:

*Python manage.py runserver
