import requests
import re
from lxml import html
etree = html.etree
import datetime


def paqu(page):
    page = str(page*10 - 10)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
        'Cookie': 'BIDUPSID=3074999252C2CBB5E123EC2347E0BEF0; PSTM=1634124964; BAIDUID=3074999252C2CBB5CEBC9A65E5623783:FG=1; __yjs_duid=1_b214728d4be9757dd99376fcd9a3d8ef1634125656212; H_PS_PSSID=35838_36024_36166_34584_36120_36195_36125_35863_36236_26350_36101_36061; BD_UPN=12314753; BAIDUID_BFESS=3074999252C2CBB5CEBC9A65E5623783:FG=1; delPer=0; BD_CK_SAM=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; __sec_t_key=5231bcb9-a6d2-4fd8-b4f5-2115d74894a6; PSINO=5; BD_HOME=1; COOKIE_SESSION=2381_0_5_9_8_8_0_3_5_5_0_0_3749025_0_5_0_1650284514_0_1650284509|9#0_0_1650284509|1; baikeVisitId=4f40e222-f57c-4f59-bcc5-41e6dca10fad; H_PS_645EC=3befHF+WSSkTincRWLxnwWt1Usx5ggZM6JvkwKh11PXDUh7upnOzn7VU8YM; BA_HECTOR=ah200k2l0ga12l049n1h5qpqs0q'
        }
    url = "https://www.baidu.com/s?wd=复旦大学&pn=10&oq=复旦大学&ie=utf-8"
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    datas = []
    ytext = res.text
    ytext = ytext[ytext.find('<html>'):]
    ttext = etree.HTML(ytext)
    ydatas = ttext.xpath('//*[@id="content_left"]/div[@class="result c-container xpath-log new-pmd"]')
    for div in ydatas:
        tdata = div.xpath('.//h3//text()')
        ttitle = ''
        for tstr in tdata:
            ttitle += tstr
        datas.append(ttitle)
    return datas
    #"/html/body/div[2]/div[3]/div[1]/div[3]/div[1]"
    #"/html/body/div[2]/div[3]/div[1]/div[3]/div[2]"




if __name__ == '__main__':
    page = 1
    """
    fout = open("../../data/test.csv", "w")
    fout.write('title,stockName,stockCode,orgCode,orgName,orgSName,publishDate,predictNextTwoYearEps,predictNextTwoYearPe,predictNextYearEps,predictNextYearPe,predictThisYearEps,predictThisYearPe,predictLastYearEps,predictLastYearPe,actualLastTwoYearEps,actualLastYearEps,industryCode,industryName,emIndustryCode,indvInduCode,indvInduName,emRatingCode,emRatingValue,emRatingName,lastEmRatingCode,lastEmRatingValue,lastEmRatingName,ratingChange,reportType,author,indvIsNew,researcher,newListingDate,newPurchaseDate,newIssuePrice,newPeIssueA,indvAimPriceT,indvAimPriceL,attachType,attachSize,attachPages,encodeUrl,sRatingName,sRatingCode,market,authorID,count\n')
    fout.close()
    """
    data = paqu(10)
    
    fout2 = open("data/baidu.csv", "w")
    for i in data:
        fout2.write(i+"\n")
    fout2.close()
    