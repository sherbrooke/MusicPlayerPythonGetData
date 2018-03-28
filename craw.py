import requests
from bs4 import BeautifulSoup
import json
import py_mysql

class Craw:
    def craw(self,url,type):
        db = py_mysql.PyMySQL()
        session = requests.session()
        response = session.get(url, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}, verify=False)
        soup = BeautifulSoup(response.text, 'html.parser')
        print(response)
        lis = soup.find('div', id='song-list-pre-cache').find('ul').findAll('li')

        info = soup.find('div', id='song-list-pre-cache').find('textarea')
        text = info.text
        print(text)
        b = json.loads(text)
        for song in b:
            id = song['id']
            name = song['name']
            album = song['album']['name']
            album_id = song['album']['id']
            url = 'http://music.163.com/song/media/outer/url?id=' + str(id) + '.mp3'
            print(url)
            artist = song['artists'][0]['name']
            print(artist)
            duration = song['duration']
            pic = song['album']['picUrl']
            print(name)
            if type == 1:
                db.insert_new_info(id, name, album, album_id, url, artist, duration, pic)
            elif type == 2:
                db.insert_hot_info(id, name, album, album_id, url, artist, duration, pic)
            elif type == 3:
                db.insert_billboard_info(id, name, album, album_id, url, artist, duration, pic)
            elif type == 4:
                db.insert_pop_info(id, name, album, album_id, url, artist, duration, pic)
            else:
                pass



if __name__ == "__main__":
    # 新歌榜
    new_url = 'https://music.163.com/discover/toplist?id=19723756'
    # 热歌榜
    hot_url = 'https://music.163.com/discover/toplist?id=3778678'
    billboard_url = 'https://music.163.com/discover/toplist?id=60198'
    pop_url = 'https://music.163.com/discover/toplist?id=1978921795'

    c = Craw()
    c.craw(new_url,1)
    c.craw(hot_url,2)
    c.craw(billboard_url,3)
    c.craw(pop_url,4)


# id = '123'
# url1 = 'http://music.163.com/song/media/outer/url?id='+id+'.mp3'