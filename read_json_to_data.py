import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mblog.settings') # 需對應 wsgi.py
django.setup()
# 更多操作請參考官方文檔: https://docs.djangoproject.com/en/3.1/topics/db/models/
from mainsite.models import Post, Branch, StoreIncome, FiveMountain
import json
#=============================================================================#
"""
with open('Post.json', 'r') as read_file:   #開啟檔案到編譯器的變數
    post_json = json.load(read_file)

for i, post_dict in enumerate(post_json):
    title = post_dict['title']
    slug = post_dict['slug']
    body = post_dict['body']
    pub_date = post_dict['pub_date']
    p = Post.objects.create(title=title, slug=slug, body=body) #到資料庫
    p.save()
"""
#=============================================================================#
with open('Branch.json', 'r') as read_file:
    stores_json = json.load(read_file)

for i, store_dict in enumerate(stores_json):
    title = store_dict['title']
    name = store_dict['name']
    #filter 出資料庫所有相同資料
    filter_stores = Branch.objects.filter(title=title, name=name)
    #若沒任何相同就創建新的一筆資料
    if len(filter_stores) == 0:
        Branch.objects.create(title=title, name=name)
    else:
        print(f'有重複 {len(filter_stores)} 筆 {filter_stores}')


#=============================================================================#
with open('StoreIncome.json', 'r') as read_file:
    store_income_json = json.load(read_file)

for i, store_income_dict in enumerate(store_income_json):
    income_year = store_income_dict['income_year']
    income_month = store_income_dict['income_month']
    income = store_income_dict['income']
    if income >= 2147483647: # 資料型態 不能超出 21億 (max=2^31 - 1)
        print(f'StoreIncome income={income} 超出過 2147483647')
        income = 22147483
    branch_title = store_income_dict['branch.title']
    
    # filter出資料庫，所有 相同的 Branch 資料
    filter_stores = Branch.objects.filter(title=branch_title)
    if len(filter_stores) == 0: # 沒有這家店
        print(f'不存在 店名 {branch_title}')
        continue # 繼續下 1 筆資料
    elif len(filter_stores) > 1: # 列印出 重複店名 訊息
        print(f'有重複 {len(filter_stores)} 間店名 {filter_stores}')
    
    store = filter_stores[0] # 取第一間

    # filter出資料庫，所有 相同的 StoreIncome 資料
    filter_store_incomes = StoreIncome.objects.filter(income_year=income_year, income_month=income_month, branch=store)
    
    # 如果 沒有任何相同，則創建新的一筆資料
    if len(filter_store_incomes) == 0:
        StoreIncome.objects.create(income_year=income_year, income_month=income_month, income=income, branch=store)

#store = Branch.objects.filter(title=branch_title)[0]    
#創建另一個model


#=============================================================================#
with open('five_mountain.json', 'r') as read_file:
    five_mountain_json = json.load(read_file)

for i, five_mountain_dict in enumerate(five_mountain_json):
    mountain_name = five_mountain_dict['mountain_name']
    mountain_high = five_mountain_dict['mountain_high']
     # filter出資料庫，所有 相同的資料
    filter_five_mountains = FiveMountain.objects.filter(mountain_name=mountain_name)
    
    # 如果 沒有任何相同，則創建新的一筆資料
    if len(filter_five_mountains) == 0:
        FiveMountain.objects.create(mountain_name=mountain_name, mountain_high=mountain_high)
    else:
        print(f'有重複 {len(filter_five_mountains)} 筆 {filter_five_mountains}')
    

