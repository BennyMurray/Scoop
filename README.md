![splashlogo-02](https://cloud.githubusercontent.com/assets/17185335/21775764/4a6dbb5c-d68f-11e6-90cc-5cb98d576d22.png)


# What is Scoop?

Scoop is a craft beer search-engine that autonomously generates data through web-scraping and semantic analysis.

## Demo

# To build project:

### Install the following dependencies via pip or equivalent:


* Django

* djangorestframework

* bs4

* mechanize

* nltk

* Django-cors-headers


### Download nltk library:

* Run the python script: ‘nltk downloader.py’

* In the GUI, select ‘download all’


### Migrate the database:

* Python manage.py makemigrations ScoopApp

* Python manage.py migrate


### Load the sample database:

* Python loadSampleDB.py 


### Run the server:

* Python manage.py runserver

# Screenshots

![scoop1](https://user-images.githubusercontent.com/17185335/28250815-b58970f2-6a69-11e7-8ed9-0dadcbb48a03.png)
![scoop2](https://user-images.githubusercontent.com/17185335/28250816-b58a8df2-6a69-11e7-9da5-b83757c7b362.png)
![scoop3](https://user-images.githubusercontent.com/17185335/28250818-b58c5254-6a69-11e7-9dbe-1fb895d74adf.png)
![scoop4](https://user-images.githubusercontent.com/17185335/28250817-b58c4a0c-6a69-11e7-9307-8c35835bb2b9.png)

## Structure
![scoop5](https://user-images.githubusercontent.com/17185335/28250819-b59a51ba-6a69-11e7-91f3-06d8c3abb11f.png)


