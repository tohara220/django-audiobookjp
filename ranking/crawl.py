import re
from bs4 import BeautifulSoup
import requests

url_ranking = 'https://audiobook.jp/ranking/product-total'

def format_text(text):
    '''空白や改行コードを除去'''
    text = re.sub(r'\u2000|\u0020|\n','',text)
    return text

def main():
    '''メイン処理'''
    # レスポンスオブジェクトを取得（パーサーとして高速に処理できるlxmlを使用）
    res = requests.get(url_ranking)
    
    # HTMLを解析し、DOMツリーを作成
    soup = BeautifulSoup(res.text, 'lxml')
    
    # すべての要素を取得する
    all_elms = soup.find_all(class_= 'product-box media')
    
    # 空のリストを用意
    result = []
    
    # ループですべての要素を取得する
    for i, elms in enumerate(all_elms):
        try:
            title = format_text(elms.find('a', class_='product-box__link product-box__title').text)
            author = format_text(elms.find('div', class_='product-box__info--author').text)
            detail_link = format_text('https://audiobook.jp' + elms.a.get('href'))
            result.append([title, author, detail_link])
        except:
            pass
    return result

if __name__ == '__main__':
    main()