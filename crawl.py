from bs4 import BeautifulSoup
import requests

url_ranking = 'https://audiobook.jp/ranking/product-total'

def main():
    '''メイン処理'''
    # レスポンスオブジェクトを取得（パーサーとして高速に処理できるlxmlを使用）
    res = requests.get(url_ranking)
    
    # HTMLを解析し、DOMツリーを作成
    soup = BeautifulSoup(res.text, 'lxml')
    
    # すべての要素を取得する
    all_elms = soup.find_all(class_= 'product-box media')
    
    # ループですべての要素を取得する
    for i, elms in enumerate(all_elms):
        try:
            title = elms.find('a', class_='product-box__link product-box__title').text
            author = elms.find('div', class_='product-box__info--author').text
            detail_link = elms.a.get('href')
            print(title, author, detail_link)
        except:
            pass

if __name__ == '__main__':
    main()