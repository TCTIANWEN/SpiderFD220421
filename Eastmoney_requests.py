import requests
import re

import datetime
from requests.adapters import HTTPAdapter

zd = {
    'title': 0,
    'stockName': 1,
    'stockCode': 2,
    'orgCode': 3,
    'orgName': 4,
    'orgSName': 5,
    'publishDate': 6,
    'predictNextTwoYearEps': 7,
    'predictNextTwoYearPe': 8,
    'predictNextYearEps': 9,
    'predictNextYearPe': 10,
    'predictThisYearEps': 11,
    'predictThisYearPe': 12,
    'predictLastYearEps': 13,
    'predictLastYearPe': 14,
    'actualLastTwoYearEps': 15,
    'actualLastYearEps': 16,
    'industryCode': 17,
    'industryName': 18,
    'emIndustryCode': 19,
    'indvInduCode': 20,
    'indvInduName': 21,
    'emRatingCode': 22,
    'emRatingValue': 23,
    'emRatingName': 24,
    'lastEmRatingCode': 25,
    'lastEmRatingValue': 26,
    'lastEmRatingName': 27,
    'ratingChange': 28,
    'reportType': 29,
    'author': 30,
    'indvIsNew': 31,
    'researcher': 32,
    'newListingDate': 33,
    'newPurchaseDate': 34,
    'newIssuePrice': 35,
    'newPeIssueA': 36,
    'indvAimPriceT': 37,
    'indvAimPriceL': 38,
    'attachType': 39,
    'attachSize': 40,
    'attachPages': 41,
    'encodeUrl': 42,
    'sRatingName': 43,
    'sRatingCode': 44,
    'market': 45,
    'authorID': 46,
    'count': 47,
    }


def del_code(strr):
    return strr.replace('\u2219', "").replace('\u2f12', "").replace('\xae', '').replace('\ufeff', '').replace('\u2022', '').replace('\u201a', '').replace('\u201b', '')


def paqu(page, url):
    page = str(page)
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'cowCookie=true; intellpositionL=1484px; qgqp_b_id=34c0bd01971ffe933f85752c10bdbc0e; st_si=07084464771524; st_asi=delete; st_pvi=25768213133288; st_sp=2021-01-19%2016%3A06%3A15; st_inirUrl=https%3A%2F%2Fwww.so.com%2Flink; st_sn=2; st_psi=20210121141950156-113300303752-7616321630; intellpositionT=2818px',
        'Host': 'reportapi.eastmoney.com',
        'Referer': 'http://data.eastmoney.com/report/stock.jshtml',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    s = requests.Session()
    s.mount('http://', HTTPAdapter(max_retries=3))
    s.mount('https://', HTTPAdapter(max_retries=3))
    try:
        r = s.get(url, headers=headers)
        return del_code(r.text)
    except requests.exceptions.RequestException as e:
        print(e)
        return -1



def blankdealing(a):
    if a == []:
        return ""
    else:
        return a[0]

def datamining(text):
    text = text.replace('"', '')
    ydata = re.findall(r'{ti(.*?)}', text)
    data = []
    for i in ydata:
        title = blankdealing(re.findall(r'tle:(.*?),', i))
        stockName = blankdealing(re.findall(r'stockName:(.*?),', i))
        stockCode = blankdealing(re.findall(r'stockCode:(.*?),', i))
        orgCode = blankdealing(re.findall(r'orgCode:(.*?),', i))
        orgName = blankdealing(re.findall(r'orgName:(.*?),', i))
        orgSName = blankdealing(re.findall(r'orgSName:(.*?),', i))
        publishDate = blankdealing(re.findall(r'publishDate:(.*?) 00', i))
        predictNextTwoYearEps = blankdealing(re.findall(r'predictNextTwoYearEps:(.*?),', i))
        predictNextTwoYearPe = blankdealing(re.findall(r'predictNextTwoYearPe:(.*?),', i))
        predictNextYearEps = blankdealing(re.findall(r'predictNextYearEps:(.*?),', i))
        predictNextYearPe = blankdealing(re.findall(r'predictNextYearPe:(.*?),', i))
        predictThisYearEps = blankdealing(re.findall(r'predictThisYearEps:(.*?),', i))
        predictThisYearPe = blankdealing(re.findall(r'predictThisYearPe:(.*?),', i))
        predictLastYearEps = blankdealing(re.findall(r'predictLastYearEps:(.*?),', i))
        predictLastYearPe = blankdealing(re.findall(r'predictLastYearPe:(.*?),', i))
        actualLastTwoYearEps = blankdealing(re.findall(r'actualLastTwoYearEps:(.*?),', i))
        actualLastYearEps = blankdealing(re.findall(r'actualLastYearEps:(.*?),', i))
        industryCode = blankdealing(re.findall(r'industryCode:(.*?),', i))
        industryName = blankdealing(re.findall(r'industryName:(.*?),', i))
        emIndustryCode = blankdealing(re.findall(r'emIndustryCode:(.*?),', i))
        indvInduCode = blankdealing(re.findall(r'indvInduCode:(.*?),', i))
        indvInduName = blankdealing(re.findall(r'indvInduName:(.*?),', i))
        emRatingCode = blankdealing(re.findall(r'emRatingCode:(.*?),', i))
        emRatingValue = blankdealing(re.findall(r'emRatingValue:(.*?),', i))
        emRatingName = blankdealing(re.findall(r'emRatingName:(.*?),', i))
        lastEmRatingCode = blankdealing(re.findall(r'lastEmRatingCode:(.*?),', i))
        lastEmRatingValue = blankdealing(re.findall(r'lastEmRatingValue:(.*?),', i))
        lastEmRatingName = blankdealing(re.findall(r'lastEmRatingName:(.*?),', i))
        ratingChange = blankdealing(re.findall(r'ratingChange:(.*?),', i))
        reportType = blankdealing(re.findall(r'reportType:(.*?),', i))
        author = re.findall(r'author:\[(.*?)],', i)
        indvIsNew = blankdealing(re.findall(r'indvIsNew:(.*?),', i))
        researcher = blankdealing(re.findall(r'researcher:(.*?),new', i))
        newListingDate = blankdealing(re.findall(r'newListingDate:(.*?) 00', i))
        newPurchaseDate = blankdealing(re.findall(r'newPurchaseDate:(.*?) 00', i))
        newIssuePrice = blankdealing(re.findall(r'newIssuePrice:(.*?),', i))
        newPeIssueA = blankdealing(re.findall(r'newPeIssueA:(.*?),', i))
        indvAimPriceT = blankdealing(re.findall(r'indvAimPriceT:(.*?),', i))
        indvAimPriceL = blankdealing(re.findall(r'indvAimPriceL:(.*?),', i))
        attachType = blankdealing(re.findall(r'attachType:(.*?),', i))
        attachSize = blankdealing(re.findall(r'attachSize:(.*?),', i))
        attachPages = blankdealing(re.findall(r'attachPages:(.*?),', i))
        encodeUrl = blankdealing(re.findall(r'encodeUrl:(.*?),', i))
        sRatingName = blankdealing(re.findall(r'sRatingName:(.*?),', i))
        sRatingCode = blankdealing(re.findall(r'sRatingCode:(.*?),', i))
        market = blankdealing(re.findall(r'market:(.*?),', i))
        authorID = re.findall(r"authorID:\[(.*?)],", i)
        count = blankdealing(re.findall(r'count:(.*?),', i))
        data.append([title,stockName,stockCode,orgCode,orgName,orgSName,publishDate,predictNextTwoYearEps,predictNextTwoYearPe,predictNextYearEps,predictNextYearPe,predictThisYearEps,predictThisYearPe,predictLastYearEps,predictLastYearPe,actualLastTwoYearEps,actualLastYearEps,industryCode,industryName,emIndustryCode,indvInduCode,indvInduName,emRatingCode,emRatingValue,emRatingName,lastEmRatingCode,lastEmRatingValue,lastEmRatingName,ratingChange,reportType,author,indvIsNew,researcher,newListingDate,newPurchaseDate,newIssuePrice,newPeIssueA,indvAimPriceT,indvAimPriceL,attachType,attachSize,attachPages,encodeUrl,sRatingName,sRatingCode,market,authorID,count])
    fout = open("test.csv", "a")
    for i in data:
        for j in i:
            fout.write(str(j).replace(",", "、") + ", ")
        fout.write("\n")
    fout.close()
    return data


def operate(begindate):
    etime = datetime.datetime.now().strftime('%Y-%m-%d')
    endtime = str(etime)
    page = 1
    vs = 1
    data = []
    while vs:
        pagee = str(page)
        url = "http://reportapi.eastmoney.com/report/list?industryCode=*&pageSize=50&industry=*&rating=&ratingChange=&beginTime=" + begindate + "&endTime=" + endtime + "&pageNo=" + pagee + "&fields=&qType=0"
        strr = paqu(page, url)
        if strr == -1:
            page += 1
            continue
        thisdata = datamining(strr)
        if thisdata == []:
            vs = 0
        else:
            print(page)
            print(thisdata[0])
            data = data + thisdata
            page += 1

    return data


if __name__ == '__main__':
    page = 1
    """
    fout = open("../../data/test.csv", "w")
    fout.write('title,stockName,stockCode,orgCode,orgName,orgSName,publishDate,predictNextTwoYearEps,predictNextTwoYearPe,predictNextYearEps,predictNextYearPe,predictThisYearEps,predictThisYearPe,predictLastYearEps,predictLastYearPe,actualLastTwoYearEps,actualLastYearEps,industryCode,industryName,emIndustryCode,indvInduCode,indvInduName,emRatingCode,emRatingValue,emRatingName,lastEmRatingCode,lastEmRatingValue,lastEmRatingName,ratingChange,reportType,author,indvIsNew,researcher,newListingDate,newPurchaseDate,newIssuePrice,newPeIssueA,indvAimPriceT,indvAimPriceL,attachType,attachSize,attachPages,encodeUrl,sRatingName,sRatingCode,market,authorID,count\n')
    fout.close()
    """
    data = operate("2022-03-31")
    
    fout2 = open("data/test2017-2.csv", "w")
    fout2.write('title,stockName,stockCode,orgCode,orgName,orgSName,publishDate,predictNextTwoYearEps,predictNextTwoYearPe,predictNextYearEps,predictNextYearPe,predictThisYearEps,predictThisYearPe,predictLastYearEps,predictLastYearPe,actualLastTwoYearEps,actualLastYearEps,industryCode,industryName,emIndustryCode,indvInduCode,indvInduName,emRatingCode,emRatingValue,emRatingName,lastEmRatingCode,lastEmRatingValue,lastEmRatingName,ratingChange,reportType,author,indvIsNew,researcher,newListingDate,newPurchaseDate,newIssuePrice,newPeIssueA,indvAimPriceT,indvAimPriceL,attachType,attachSize,attachPages,encodeUrl,sRatingName,sRatingCode,market,authorID,count\n')
    
    for i in data:
        for j in i:
            fout2.write(str(j).replace(",", "、") + ", ")
        fout2.write("\n")
    fout2.close()
    