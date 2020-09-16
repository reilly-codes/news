from flask import render_template,url_for
from . import main
from app.request import get_news

@main.route('/')
def index():
    sports = get_news('sports',2)
    entertainment = get_news('entertainment',2)
    health = get_news('health',2)
    tech = get_news('technology',2)
    business = get_news('business',2)
    science = get_news('science',2)
    general = get_news('general',7)
    title = 'HOME - Centre of United Kingdom News'
    
    return render_template('index.html', title = title, sports = sports, entertainment = entertainment, health = health, tech = tech, science = science, business = business, gen = general)

@main.route('/ent')
def ent():
    ent = get_news('entertainment',20)
    
    return render_template('ent.html', ent = ent)
@main.route('/biz')
def biz():
    biz = get_news('business', 20)
    
    return render_template('biz.html', biz = biz)

@main.route('/health')
def health():
    healthy = get_news('health', 20)
    
    return render_template('health.html', healthy = healthy)

@main.route('/science')  
def science():
    scienze =get_news('science', 20)
    
    return render_template('science.html', science = scienze)
    
@main.route('/sports')
def sports():
    sport = get_news('sports', 20)
    
    return render_template('sport.html', sport = sport)
 
@main.route('/tech')   
def tech():
    technology = get_news('technology', 20)
    
    return render_template('tech.html', tech = technology)

