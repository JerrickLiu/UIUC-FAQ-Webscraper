# Webscraper for UIUC FAQ

Due to the rise of COVID-19 in the United States, the college that I'm attending, the University of Illinois at Urbana-Champaign (UIUC for short), has a posted a FAQ on their website for the arising number of questions and uncertainty in these times. I always want to stay updated on if there's any new info being added to the FAQ so I decided to build a webscraper using Python's BeautifulSoup library that scraps the questions on the website and checks if there is a new question. If there is a new question, the script emails me that there is a new question and in the body of the email tells me what the question is.  

## Technologies 

1. BeautifulSoup and the requests library

```bash
pip install beautifulsoup4
pip install requests
```

2. smtplib. smtplib is the built-in Python SMTP protocol client that allows us to connect to our email account and send mail via SMTP.
3. MIME. MIME (Multipurpose Internet Mail Extensions) is a standard for formatting files to be sent over the internet so they can be viewed in a browser or email application.

## Example

![demo](demo/demo.png)

## Usage

You can use this code for your own university you'd just need to to substitude the URL with your college and change the name of the HTML elements you are trying to find on your college webpage. I have my own email on the code so you would need to change that as well if you are running this code.
