import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

# 目标网站的 URL
base_url = 'https://www.cnblogs.com/seafever/p/12345200.html'

# 创建下载文件夹
download_folder = 'E:/downloaded_files'
os.makedirs(download_folder, exist_ok=True)

# 获取网页内容
response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')

# 查找所有链接
for link in soup.find_all('a'):
    href = link.get('href')
    if href:
        # 拼接完整的 URL
        full_url = urljoin(base_url, href)
        # 下载文件
        try:
            file_response = requests.get(full_url)
            file_name = os.path.join(download_folder, href.split('/')[-1])
            with open(file_name, 'wb') as f:
                f.write(file_response.content)
                print(f'Downloaded: {file_name}')
        except Exception as e:
            print(f'Failed to download {full_url}: {e}')
