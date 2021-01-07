import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mblog.settings') # 需對應 wsgi.py #cmd 顯示
django.setup()
# 更多操作請參考官方文檔: https://docs.djangoproject.com/en/3.1/topics/db/models/
from mainsite.models import Post, Branch, StoreIncome
#=============================================================================#
# 添加一筆資料
# post = Post.objects.create(title="文章標題", slug="px", body='文章內容')
# post.save()

posts = Post.objects.all()
print(f'\nPost class 內資料: {posts}')
for i, post in enumerate(posts):
    print(f'\n第 {i+1} 筆 Post 資料')
    print(f'title: {post.title} slug: {post.slug} pub_date: {post.pub_date}')
    print(f'body: {post.body}')
print('\n')

#=============================================================================#
# 添加一筆資料
# store = Branch.objects.create(title="每日店", name="美麗店長")
# store.save()

stores = Branch.objects.all()
print(f'\nBranch class 內資料: {stores}')
for i, store in enumerate(stores):
    print(f'\n第 {i+1} 筆 Branch 資料')
    print(f'title: {store.title} name: {store.name}')
print('\n')
#=============================================================================#
# 添加一筆資料
# store = Branch.objects.get(title="每日店")
# store_income = StoreIncome.objects.create(income_year=2021, income_month=1, income=50000, branch=store)
# store_income.save()

data = StoreIncome.objects.all()
print(f'\nStoreIncome class 內資料: {data}')
for i, store_income in enumerate(data):
    print(f'\n第 {i+1} 筆 StoreIncome 資料')
    print(f'income_year: {store_income.income_year} income_month: {store_income.income_month} income: {store_income.income} branch: {store_income.branch}')
print('\n')