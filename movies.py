from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup as bs
import random
import wget
import time
import json
import sys

app = Flask(__name__)


@app.route('/search/', methods=['GET', 'POST'])
def search():
    session = requests.Session()
    list_of_user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
        'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
        'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
        
        ]
    #RANDOM SELECTION OF USER AGENTS TO PREVENT EASY BANNING BY THE SITE
    user_agent = random.choice(list_of_user_agents)
    headers = {'User-Agent':user_agent}
    movie_name = request.args.get('movie')
    url = 'https://lightdlmovies.blogspot.com/search?q={}'.format(movie_name)
    #print(movie_name)
    get_url = session.get(url, headers=headers)
    soup = bs(get_url.text, 'html.parser')
    div = soup.find('div',{'id':'Blog1'})
    #print(div)
    div_2 = div.find('div', {'class':'post-body'})
    a_href = div_2.find_all('a')
    print(a_href)
    download_links = []
    #count = 0
    del a_href[0]
    for dl in a_href:
        link = dl['href']
        download_links.append(link)
        #count += 1
        print('yes')
        print(download_links)
        download_header = "Click the links to download any quality of your choice"
    #count = 0 
    #for dl in download_links:
    #    print(f'{count} ---->>>>> {download_links[count]} \n')
    #    count += 1

    return render_template('home.html', title='home', download_header=download_header, download_links=download_links)

def download_movies():
        while True:
            session = requests.Session()
            list_of_user_agents = [
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
                'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
                'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
                'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
                'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
                'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
                'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
                'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
                'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
                'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
                'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
                'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
                'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
                'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
                'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
                
                ]
            #RANDOM SELECTION OF USER AGENTS TO PREVENT EASY BANNING BY THE SITE
            user_agent = random.choice(list_of_user_agents)
            headers = {'User-Agent':user_agent}
            print('WELCOME TO MOVIESOGET \n ENTER 1 TO CONTINUE OR 2 TO EXIT \n ENTER THE NAME OF THE MOVIE SPECIFICALLY EG: AVENGERS AGE OF ULTRON, \n NOT VAGUE TITLES')
            while True:
                try:
                    choice = int(input(">>>:"))
                    if choice == 1:
                        movie_name = input('What movie would you like to download?:::::::')
                        url = 'https://lightdlmovies.blogspot.com/search?q={}'.format(movie_name)  
                        get_url = session.get(url, headers=headers)
                        soup = bs(get_url.text, 'html.parser')
                        div = soup.find('div',{'class':'Blog'})
                        div_2 = div.find('div', {'class':'post-body'})
                        a_href = div_2.find_all('a')
                        download_links = {}
                        count = 0
                        del a_href[0]
                        for dl in a_href:
                            link = dl['href']
                            download_links[count] = link
                            count += 1
                        count = 0 
                        for dl in download_links:
                            print(f'{count} ---->>>>> {download_links[count]} \n')
                            count += 1
                        print('ENTER THE NUMBER TO DOWNLOAD THE QUALITY YOU WISH')
                        while True:
                            try:
                                user_quality = int(input(">>:"))
                                movie = wget.download(download_links[user_quality])
                            except(ValueError):
                                print("ENTER A WHOLE NUMBER NOT STRING OR DECIMAL")
                                continue
                    else:
                        sys.exit()
                except(ValueError):
                    print('INPUT MUST EITHER 1 OR 2')
                    continue


@app.route('/')
def home():

    
    #download_movies()
    return render_template("home.html" )




if __name__ == "__main__":
    app.run(debug=True)
