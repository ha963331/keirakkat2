import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mblog.settings') # 需對應 wsgi.py
django.setup()
# 更多操作請參考官方文檔: https://docs.djangoproject.com/en/3.1/topics/db/models/
from mainsite.models import Post, Branch, StoreIncome
import json
#=============================================================================#
with open('Post.json', 'r') as read_file:   #開啟檔案到編譯器的變數
    post_json = json.load(read_file)

for i, post_dict in enumerate(post_json):
    title = post_dict['title']
    slug = post_dict['slug']
    body = post_dict['body']
    pub_date = post_dict['pub_date']
    p = Post.objects.create(title=title, slug=slug, body=body) #到資料庫
    p.save()
#=============================================================================#
with open('Branch.json', 'r') as read_file:
    stores_json = json.load(read_file)

for i, store_dict in enumerate(stores_json):
    title = store_dict['title']
    name = store_dict['name']
    Branch.objects.create(title=title, name=name)
#=============================================================================#
with open('StoreIncome.json', 'r') as read_file:
    store_income_json = json.load(read_file)

for i, store_income_dict in enumerate(store_income_json):
    income_year = store_income_dict['income_year']
    income_month = store_income_dict['income_month']
    income = store_income_dict['income']
    branch_title = store_income_dict['branch.title']
    store = Branch.objects.get(title=branch_title)
    #store = Branch.objects.filter(title=branch_title)[0]
    store_income = StoreIncome.objects.create(income_year=income_year, income_month=income_month, income=income, branch=store) #創建另一個model