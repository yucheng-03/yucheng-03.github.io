import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import datetime

# 你的 GitHub 个人主页 URL
github_url = "https://github.com/yucheng-03"

# 发送请求获取页面内容
response = requests.get(github_url)
soup = BeautifulSoup(response.text, 'html.parser')

# 创建 Sitemap 的根元素
urlset = ET.Element('urlset', xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

# 查找所有项目链接
repo_links = soup.find_all('a', itemprop="name codeRepository")
for link in repo_links:
    repo_url = "https://github.com" + link['href']
    # 创建 url 元素
    url = ET.SubElement(urlset, 'url')
    loc = ET.SubElement(url, 'loc')
    loc.text = repo_url
    lastmod = ET.SubElement(url, 'lastmod')
    lastmod.text = datetime.datetime.now().strftime("%Y-%m-%d")
    changefreq = ET.SubElement(url, 'changefreq')
    changefreq.text = "monthly"
    priority = ET.SubElement(url, 'priority')
    priority.text = "0.8"

# 生成 XML 文件
tree = ET.ElementTree(urlset)
tree.write('sitemap.xml', encoding='utf-8', xml_declaration=True)