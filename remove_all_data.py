import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mblog.settings') # 需對應 wsgi.py
django.setup()
# 更多操作請參考官方文檔: https://docs.djangoproject.com/en/3.1/topics/db/models/
from mainsite.models import Post, Branch, StoreIncome, FiveMountain
#=============================================================================#
#Post.objects.all().delete()
posts = Post.objects.all()
for i, post in enumerate(posts):
    title = post.title
    slug = post.slug
    pub_date = post.pub_date
    body = post.body

    filter_posts = Post.objects.filter(title=title, slug=slug)
    
    if len(filter_posts) > 1:
        for ipost in filter_posts[1:]:
            ipost.delete()

#=============================================================================#
#Branch.objects.all().delete()

stores = Branch.objects.all()
for i, store in enumerate(stores):
    title = store.title
    name = store.name
    
    filter_stores = Branch.objects.filter(title=title)
    
    if len(filter_stores) > 1:
        for istore in filter_stores[1:]:
            istore.delete()

#=============================================================================#
#StoreIncome.objects.all().delete()

data = StoreIncome.objects.all()
for i, store_income in enumerate(data):
    # 讀取出每一筆資料
    income_year = store_income.income_year
    income_month = store_income.income_month
    income = store_income.income
    branch_title = store_income.branch.title
    
    # filter出資料庫，所有 相同的 Branch 資料
    filter_stores = Branch.objects.filter(title=branch_title)
    if len(filter_stores) > 1: # 列印出 重複店名 訊息
        for istore in filter_stores[1:]:
            istore.delete()
    
    store = filter_stores[0] # 取第一間

    # filter出資料庫，所有 相同的 StoreIncome 資料
    filter_store_incomes = StoreIncome.objects.filter(income_year=income_year, income_month=income_month, branch=store)
    
    # 如果大於1間店，代表有重複，需刪除
    if len(filter_store_incomes) > 1:
        # filter_store_incomes[1:] 代表 除了第1筆之後的 都刪除
        for istore_income in filter_store_incomes[1:]:
            istore_income.delete()

#=============================================================================#
#FiveMountain.objects.all().delete()

five_mountains = FiveMountain.objects.all()
for i, five_mountain in enumerate(five_mountains):
    mountain_name = five_mountain.mountain_name
    mountain_high = five_mountain.mountain_high
        
    filter_five_mountains = FiveMountain.objects.filter(mountain_name=mountain_name)
    
    if len(filter_five_mountains) > 1:
        for ifive_mountain in filter_five_mountains[1:]:
            ifive_mountain.delete()