from run import app
import urllib.request, json
from .models import News

api_key = app.config['NEWS_API_KEY']
base_url = app.config['NEWS_API_BASE_URL']

def get_news(category,list_size):
    get_news_url = base_url.format(category,list_size,api_key)
    
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_respone = json.loads(get_news_data)
        
        
        news = None
        
        if get_news_respone['articles']:
            news_list = get_news_respone['articles']
            news = process_results(news_list)
            
    return news
    
def process_results(news_list):
    news_result = []
    for news_item in news_list:
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        content = news_item.get('content')
        
        if url:
            news_object = News(author, title, description, url, content)
            news_result.append(news_object)
        
        
    return news_result
