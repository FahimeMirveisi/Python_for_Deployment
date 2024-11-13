
from flask import Flask, render_template
from newsapi import NewsApiClient


# init flask app
app = Flask("BBC & CNN NEWS")

# Init news api 

newsapi = NewsApiClient(api_key='ca8991b7d439432f9c94490cdd337cad')


@app.route('/')
def headlines():
    #headlines = topHeadlines()

    top_headlines = newsapi.get_top_headlines(sources= 'cnn, bbc_news')
    
    articles = top_headlines['articles']
    

    title = []
    desc = []
    author = []
    img = []
    p_date = []
    url = []

    for i in range(len(articles)):
        headline = articles[i]
        

        title.append(headline['title'])
        desc.append(headline['description'])
        author.append(headline['author'])
        img.append(headline['urlToImage'])
        p_date.append(headline['publishedAt'])
        url.append(headline['url'])

        headlines = zip(title, desc, author, img, p_date, url)


    return  render_template('headlines.html', headlines = headlines)


@app.route('/business')
def business():
    top_headlines = newsapi.get_top_headlines(category='business')
    
    articles = top_headlines['articles']
    

    title = []
    desc = []
    author = []
    img = []
    p_date = []
    url = []

    for i in range(len(articles)):
        headline = articles[i]
        

        title.append(headline['title'])
        desc.append(headline['description'])
        author.append(headline['author'])
        img.append(headline['urlToImage'])
        p_date.append(headline['publishedAt'])
        url.append(headline['url'])

        headlines = zip(title, desc, author, img, p_date, url)


    return  render_template('business.html', headlines = headlines)

@app.route('/tech')
def tech():
    top_headlines = newsapi.get_top_headlines(category='technology')
    
    articles = top_headlines['articles']
    

    title = []
    desc = []
    author = []
    img = []
    p_date = []
    url = []

    for i in range(len(articles)):
        headline = articles[i]
        

        title.append(headline['title'])
        desc.append(headline['description'])
        author.append(headline['author'])
        img.append(headline['urlToImage'])
        p_date.append(headline['publishedAt'])
        url.append(headline['url'])

        headlines = zip(title, desc, author, img, p_date, url)


    return  render_template('tech.html', headlines = headlines)

@app.route('/entertainment')
def entertainment():
    top_headlines = newsapi.get_top_headlines(category='entertainment')
    
    articles = top_headlines['articles']
    

    title = []
    desc = []
    author = []
    img = []
    p_date = []
    url = []

    for i in range(len(articles)):
        headline = articles[i]
        

        title.append(headline['title'])
        desc.append(headline['description'])
        author.append(headline['author'])
        img.append(headline['urlToImage'])
        p_date.append(headline['publishedAt'])
        url.append(headline['url'])

        headlines = zip(title, desc, author, img, p_date, url)


    return  render_template('entertainment.html', headlines = headlines)

@app.route('/science')
def science():
    top_headlines = newsapi.get_top_headlines(category='science')
    
    articles = top_headlines['articles']
    

    title = []
    desc = []
    author = []
    img = []
    p_date = []
    url = []

    for i in range(len(articles)):
        headline = articles[i]
        

        title.append(headline['title'])
        desc.append(headline['description'])
        author.append(headline['author'])
        img.append(headline['urlToImage'])
        p_date.append(headline['publishedAt'])
        url.append(headline['url'])

        headlines = zip(title, desc, author, img, p_date, url)


    return  render_template('science.html', headlines = headlines)

@app.route('/sports')
def sports():
    top_headlines = newsapi.get_top_headlines(category='sports')
    
    articles = top_headlines['articles']
    

    title = []
    desc = []
    author = []
    img = []
    p_date = []
    url = []

    for i in range(len(articles)):
        headline = articles[i]
        

        title.append(headline['title'])
        desc.append(headline['description'])
        author.append(headline['author'])
        img.append(headline['urlToImage'])
        p_date.append(headline['publishedAt'])
        url.append(headline['url'])

        headlines = zip(title, desc, author, img, p_date, url)


    return  render_template('sports.html', headlines = headlines)

@app.route('/health')
def health():
    top_headlines = newsapi.get_top_headlines(category='health')
    
    articles = top_headlines['articles']
    

    title = []
    desc = []
    author = []
    img = []
    p_date = []
    url = []

    for i in range(len(articles)):
        headline = articles[i]
        

        title.append(headline['title'])
        desc.append(headline['description'])
        author.append(headline['author'])
        img.append(headline['urlToImage'])
        p_date.append(headline['publishedAt'])
        url.append(headline['url'])

        headlines = zip(title, desc, author, img, p_date, url)


    return  render_template('health.html', headlines = headlines)