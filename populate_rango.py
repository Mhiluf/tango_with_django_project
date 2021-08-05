import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    manufacturer_pages=[
        {'title': 'BMW','url':'https://www.carmodelslist.com/bmw/', 'views':'18',},
        {'title': 'Daihatsu','url':'https://www.carmodelslist.com/daihatsu/','views':'100',},
        {'title': 'JEEP','url':'https://www.carmodelslist.com/jeep/','views':'28',}]

    country_pages=[
        {'title':'Australia','url':'https://www.carmodelslist.com/australia-car-brands/','views':'18',},
        {'title':'United Kindgom','url':'https://www.carmodelslist.com/united-kingdom-car-brands/','views':'128',},
        {'title':'United States','url':'https://www.carmodelslist.com/united-states-car-brands/','views':'12',}
    ]

    other_pages=[
        {'title':'Cars Movie','url':'https://www.imdb.com/title/tt0317219/','views':'108',},
        {'title':'Forza Horizon game','url':'https://forzamotorsport.net/en-US/games/fh','views':'208',}
    ]

    cats = {
        'Manufacturer':{'pages': manufacturer_pages , 'views':'128', 'likes':'64'}, 
        'Brands by country':{'pages': country_pages , 'views':'64', 'likes':'32'},
        'Other Frameworks':{'pages':other_pages, 'views':'32', 'likes':'16'}
        }

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['views'], cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'],p['views'])
    
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'-{c}: {p}')
    

def add_page(cat,title,url,views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name,views=0,likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views=views
    c.likes=likes
    c.save()
    return c 

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()