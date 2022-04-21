import requests
from lxml import etree
import csv

class doubanspider:
    def __init__(self):
        self.url_temp="https://www.douban.com/doulist/45097500/?start={}"
        self.headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}


    def get_urllist(self):
        return [self.url_temp.format(i*25) for i in range(1,9)]

    def parse_url(self,url):
        print(url)
        response=requests.get(url,headers=self.headers)
        return response.content.decode()

    def get_content(self,html_url):
        html=etree.HTML(html_url)
        div_list=html.xpath("//div[@class='article']/div[@class='doulist-item']")
        content_list=[]
        for div in div_list:
            item={}
            item["name"]=div.xpath(".//div[@class='title']/a/text()")
            item["name"] =[i.replace("\n",'') for i in item["name"]]
            item["name"]=''.join(item["name"])
            item["author"] = div.xpath(".//div[@class='abstract']/text()")
            item["author"] = item["author"][0] if len(item["author"]) > 0 else None
            item["publish"] = div.xpath(".//div[@class='abstract']/text()")
            item["publish"]=item["publish"][1] if len(item["publish"])>0 else None
            # item["year"] = div.xpath(".//div[@class='abstract']/text()")
            # item["year"] = item["year"][2] if len(item["year"]) > 0 else None

            # item["year"] = div.xpath(".//div[@class='abstract']/text()")[2]
            item["scores"] = div.xpath(".//div[@class='rating']/span[@class='rating_nums']/text()")

            content_list.append(item)

        return content_list
    def save_file(self,content_list):
        with open("douban.csv", 'w', encoding="UTF-8") as f:
            writer = csv.DictWriter(f, fieldnames=['name', 'author', 'publish','scores'])
            writer.writeheader()
            for i in content_list:
                print("正在写入：" +i['name'])
                writer.writerow(i)

    def run(self):#实现主要逻辑
        #获取url_list
        url_list=self.get_urllist()
        #遍历，获取请求，获得响应
        for url in url_list:
            html_url=self.parse_url(url)
        #爬取数据
            contentlist=self.get_content(html_url)
        #保存数据
            self.save_file(contentlist)
#程序入口
if __name__ == "__main__":
    douban=doubanspider()
    douban.run()