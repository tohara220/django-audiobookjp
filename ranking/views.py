import datetime
from django.shortcuts import render
from . import crawl

def index(request):
    # ランキングを取得
    ranking = crawl.main()
    # 日時を取得
    now = datetime.datetime.now()
    date = f'{now:%Y/%m/%d_%H:%M:%S}'
    
    context = {
        'ranking': ranking,
        'date': date,
    }
    return render(request, 'ranking/index.html', context=context)