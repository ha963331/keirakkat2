import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mblog.settings') # 需對應 wsgi.py #轉成json檔
django.setup()
# 更多操作請參考官方文檔: https://docs.djangoproject.com/en/3.1/topics/db/models/
from mainsite.models import Post, Branch, StoreIncome, FiveMountain
import json
from django.core.serializers.json import DjangoJSONEncoder
#=============================================================================#
posts = Post.objects.all()
post_dict_list = []
for post in posts:
    post_dict = {}
    post_dict['title'] = post.title
    post_dict['slug'] = post.slug
    post_dict['body'] = post.body
    post_dict['pub_date'] = post.pub_date
    post_dict_list.append(post_dict)
post_json = json.dumps(post_dict_list, cls=DjangoJSONEncoder)
print(f'{post_dict_list}\n')
print(f'{post_json}\n')

with open('Post.json', 'w') as fp:
    fp.write(post_json)

#=============================================================================#
stores = Branch.objects.all()
store_dict_list = []
for store in stores:
    store_dict = {}
    store_dict['title'] = store.title
    store_dict['name'] = store.name
    store_dict_list.append(store_dict)
stores_json = json.dumps(store_dict_list, cls=DjangoJSONEncoder)
print(f'{store_dict_list}\n')
print(f'{stores_json}\n')

with open('Branch.json', 'w') as fp:  #打包進檔案
    fp.write(stores_json)

#=============================================================================#
data = StoreIncome.objects.all()
store_income_dict_list = []
for store_income in data:
    store_income_dict = {}
    store_income_dict['income_year'] = store_income.income_year
    store_income_dict['income_month'] = store_income.income_month
    store_income_dict['income'] = store_income.income
    store_income_dict['branch.title'] = store_income.branch.title
    store_income_dict_list.append(store_income_dict)
store_income_json = json.dumps(store_income_dict_list, cls=DjangoJSONEncoder)
print(f'{store_income_dict_list}\n')
print(f'{store_income_json}\n')

with open('StoreIncome.json', 'w') as fp:
    fp.write(store_income_json)

#=============================================================================#
data = FiveMountain.objects.all()
five_mountain_dict_list = []
for five_mountain in data:
    five_mountain_dict = {}
    five_mountain_dict['mountain_name'] = five_mountain.mountain_name
    five_mountain_dict['mountain_high'] = five_mountain.mountain_high
    five_mountain_dict_list.append(five_mountain_dict)
five_mountain_json = json.dumps(five_mountain_dict_list, cls=DjangoJSONEncoder)
print(f'{five_mountain_dict_list}\n')
print(f'{five_mountain_json}\n')

with open('five_mountain.json', 'w') as fp:
    fp.write(five_mountain_json)