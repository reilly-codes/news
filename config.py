class Config:
    NEWS_API_BASE_URL = ('http://newsapi.org/v2/top-headlines?'
       'country=gb&category={}&pageSize={}&'
       'apiKey={}')
    NEWS_API_KEY = '9d427ce2e1ed49d9952286dec173b807'

class ProdConfig(Config):
    pass
class DevConfig(Config):
    DEBUG = True
    
config_options = {
    'development':DevConfig,
    'production':ProdConfig
}