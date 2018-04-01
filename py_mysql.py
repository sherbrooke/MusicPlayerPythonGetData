import pymysql

class PyMySQL:

    def __init__(self):
        #change this config to yourself's
        self.connection = pymysql.connect(host='localhost',port=3306,user='root',password='XXXXXXXXX',db='music',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)

    def insert_new_info(self,id,name,album,album_id,url,artist,duration,pic):
        with self.connection.cursor() as cursor:
            sql = '''
                insert into `new_music`(`id`,`name`,`album`,`album_id`,`url`,`artist`,`duration`,`pic`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);
            '''
            cursor.execute(sql,(id,name,album,album_id,url,artist,duration,pic))
            self.connection.commit()
    def insert_hot_info(self,id,name,album,album_id,url,artist,duration,pic):
        with self.connection.cursor() as cursor:
            sql = '''
                insert into `hot_music`(`id`,`name`,`album`,`album_id`,`url`,`artist`,`duration`,`pic`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);
            '''
            cursor.execute(sql,(id,name,album,album_id,url,artist,duration,pic))
            self.connection.commit()
    def insert_billboard_info(self,id,name,album,album_id,url,artist,duration,pic):
        with self.connection.cursor() as cursor:
            sql = '''
                insert into `billboard_music`(`id`,`name`,`album`,`album_id`,`url`,`artist`,`duration`,`pic`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);
            '''
            cursor.execute(sql,(id,name,album,album_id,url,artist,duration,pic))
            self.connection.commit()
    def insert_pop_info(self,id,name,album,album_id,url,artist,duration,pic):
        with self.connection.cursor() as cursor:
            sql = '''
                insert into `pop_music`(`id`,`name`,`album`,`album_id`,`url`,`artist`,`duration`,`pic`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);
            '''
            cursor.execute(sql,(id,name,album,album_id,url,artist,duration,pic))
            self.connection.commit()

