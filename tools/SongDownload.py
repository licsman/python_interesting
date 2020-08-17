from typing import List, Any

import requests
import re
import time


def download(song_ids, song_names):
    for i in range(0, len(song_ids)):
        song_url = "http://f2.htqyy.com/play8/" + song_ids[i] + "/mp3/8"
        song_name = song_names[i]
        referer = 'http://www.htqyy.com/play/{}'.format(song_ids[i])
        headers = {
            'Referer': referer,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
        }
        data = requests.get(song_url, params="", headers=headers)
        print("正在下载第", i + 1, "首,歌曲名称：:", song_name, ",歌曲URL:", song_url)
        print()
        # 将文件保存到指定目录
        with open("D:\\music\\{}.mp3".format(song_name), "wb") as f:
            f.write(data.content)
        time.sleep(0.5)


if __name__ == '__main__':
    songIds = []  # 存放歌曲的sid
    songNames = []  # 存放歌曲的名称
    url = "http://www.htqyy.com/top/hot"  # 歌曲列表的url
    # 获取音乐榜单的网页信息
    html = requests.get(url)
    htmlText = html.text
    pat1 = r'sid="(.*?)"'  # 用于解析sid的正则
    pat2 = r'title="(.*?)" sid'  # 用于解析歌曲名称的正则
    idList = re.findall(pat1, htmlText)  # 从爬取到的网页内容中获取sid
    titleList = re.findall(pat2, htmlText)  # 从爬取到的网页内容中获取歌曲名称
    songIds.extend(idList)  # 将sid追加到列表
    songNames.extend(titleList)  # 将歌曲名称追加到列表
    download(songIds, songNames)
