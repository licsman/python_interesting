from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import time

if __name__ == '__main__':
    chrome_opt = Options()      # 创建参数设置对象.
    chrome_opt.add_argument('--headless')   # 无界面化.
    chrome_opt.add_argument('--disable-gpu')    # 配合上面的无界面化.
    chrome_opt.add_argument('--window-size=1366,768')   # 设置窗口大小, 窗口大小会有影响.

    # 创建Chrome对象并传入设置信息.
    driver = webdriver.Chrome(options=chrome_opt)
    dyUrl = 'https://v.douyin.com/JwYBbge/'
    driver.implicitly_wait(6)
    driver.get(dyUrl)

    time.sleep(2)

    videoName = driver.find_element_by_id("pageletReflowVideo").find_element_by_class_name("video-info").find_element_by_class_name("desc").text
    print(videoName)

    driver.find_element_by_class_name("xgplayer-start").click()
    time.sleep(1)
    wtUrl = driver.find_element_by_xpath("//*[@id=\"pageletReflowVideo\"]/div/div[2]/div[1]/div[1]/video").get_attribute("src")
    print(wtUrl)
    noWtUrl = str.replace(wtUrl, "playwm", "play")
    UA = "Mozilla/5.0 (Linux; Android 8.0.0; FRD-AL10 Build/HUAWEIFRD-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/11.20 SP-engine/2.16.0 baiduboxapp/11.20.0.14 (Baidu; P1 8.0.0)"
    headers = {'Referer': noWtUrl, 'User-Agent': UA}
    data = requests.get(noWtUrl, params="", headers=headers)
    print("正在下载无水印", videoName)
    # 将文件保存到指定目录
    with open("D:\\music\\{}.mp4".format(videoName), "wb") as f:
        f.write(data.content)
    driver.quit()