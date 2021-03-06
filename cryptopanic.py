import requests
import time
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from settings import CRYPTOPANIC_API_KEY

analyser = SentimentIntensityAnalyzer()
search_term = "QSP"
total_score = 0
total_results = 0
custom_negative_words = ["sell", "tanked",
                         "tanking", "price is down", "bubble", "through support"]
custom_positive_words = ["moon", "lambo", "mooon", "breaks", "adopting",
                         "mooning", "moooon", "fuck yeah", "buy", "ath", "price is up", "surges", "broke", u"\U0001F680"]
start_url = 'http://cryptopanic.com/api/posts/?auth_token={0}&currency={1}&filter=trending'.format(
    CRYPTOPANIC_API_KEY, search_term)


def sentiment_scores(sentence):
    snt = analyser.polarity_scores(sentence)['compound']
    return snt

def parse_titles(array):
    global total_score
    # print(total_score)
    for headline in array:
        title = headline['title']
        votes = headline['votes']
        print(title)
        # print(votes)
        if votes['negative'] > votes['positive'] or any(ext in title.lower() for ext in custom_negative_words):
            # print('bad')
            total_score = total_score + -1
        elif votes['positive'] > votes['negative'] or any(ext in title.lower() for ext in custom_positive_words):
            # print('good')
            total_score = total_score + 1
        else:
            total_score = total_score + sentiment_scores(headline['title'])

def get_json_from_url(url):
        global total_results
        r = requests.get(url)
        results =  r.json()['results']
        num_results = len(results)
        
        if  num_results == 0 and total_results == 0:
            print('Insufficient Results')
        elif num_results == 0 and total_results > 0:
            calculate()
        else:
            total_results = total_results + num_results
            parse_titles(results)

            if (r.json()['next']):
                time.sleep(1)
                get_json_from_url(r.json()['next'])
            else:
                calculate()
     
def calculate():
    print(total_score)
    print(total_results)
    print(total_score/total_results)


get_json_from_url(start_url)
