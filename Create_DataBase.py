import pymysql

class CreateDatabase:
    def create(self):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='wangyang123', db='music',
                                          charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            new_music_sql = '''create table `new_music`(`id` int(11) NOT NULL ,`name` VARCHAR(256) COLLATE utf8_bin NOT NULL ,`album` VARCHAR(256) COLLATE utf8_bin NOT NULL ,
                      `album_id` int(11) COLLATE utf8_bin   NOT NULL,`url` VARCHAR(256) COLLATE utf8_bin NOT NULL,`artist` VARCHAR(256) COLLATE utf8_bin NOT NULL,
                      `duration` int(11) COLLATE utf8_bin NOT NULL , `pic` VARCHAR(256) COLLATE utf8_bin NOT NULL , PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE utf8_bin AUTO_INCREMENT=1'''
            hot_music_sql = '''create table `hot_music`(`id` int(11) NOT NULL ,`name` VARCHAR(256) COLLATE utf8_bin NOT NULL ,`album` VARCHAR(256) COLLATE utf8_bin NOT NULL ,
                      `album_id` int(11) COLLATE utf8_bin   NOT NULL,`url` VARCHAR(256) COLLATE utf8_bin NOT NULL,`artist` VARCHAR(256) COLLATE utf8_bin NOT NULL,
                      `duration` int(11) COLLATE utf8_bin NOT NULL , `pic` VARCHAR(256) COLLATE utf8_bin NOT NULL , PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE utf8_bin AUTO_INCREMENT=1'''
            billboard_music_sql = '''create table `billboard_music`(`id` int(11) NOT NULL ,`name` VARCHAR(256) COLLATE utf8_bin NOT NULL ,`album` VARCHAR(256) COLLATE utf8_bin NOT NULL ,
                      `album_id` int(11) COLLATE utf8_bin   NOT NULL,`url` VARCHAR(256) COLLATE utf8_bin NOT NULL,`artist` VARCHAR(256) COLLATE utf8_bin NOT NULL,
                      `duration` int(11) COLLATE utf8_bin NOT NULL , `pic` VARCHAR(256) COLLATE utf8_bin NOT NULL , PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE utf8_bin AUTO_INCREMENT=1'''
            pop_music_sql = '''create table `pop_music`(`id` int(11) NOT NULL ,`name` VARCHAR(256) COLLATE utf8_bin NOT NULL ,`album` VARCHAR(256) COLLATE utf8_bin NOT NULL ,
                      `album_id` int(11) COLLATE utf8_bin   NOT NULL,`url` VARCHAR(256) COLLATE utf8_bin NOT NULL,`artist` VARCHAR(256) COLLATE utf8_bin NOT NULL,
                      `duration` int(11) COLLATE utf8_bin NOT NULL , `pic` VARCHAR(256) COLLATE utf8_bin NOT NULL , PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE utf8_bin AUTO_INCREMENT=1'''
            cursor.execute("drop table if exists new_music")
            cursor.execute("drop table if exists hot_music")
            cursor.execute("drop table if exists billboard_music")
            cursor.execute("drop table if exists pop_music")
            cursor.execute(new_music_sql)
            cursor.execute(hot_music_sql)
            cursor.execute(billboard_music_sql)
            cursor.execute(pop_music_sql)