import requests
from bs4 import BeautifulSoup


url = "https://kns.cnki.net/kns8/Brief/GetGridTableHtml"

datas = {
    'IsSearch': 'true',
    'QueryJson': '{"Platform":"","DBCode":"CFLS","KuaKuCode":"CJFQ,CDMD,CIPD,CCND,CISD,SNAD,BDZK,CCJD,CCVD,CJFN","QNode":{"QGroup":[{"Key":"Subject","Title":"","Logic":4,"Items":[],"ChildItems":[{"Key":"input[data-tipid=gradetxt-3]","Title":"文献来源","Logic":1,"Items":[{"Key":"","Title":"管理世界","Logic":1,"Name":"LY","Operate":"=","Value":"管理世界","ExtendType":1,"ExtendValue":"中英文对照","Value2":""}],"ChildItems":[]}]},{"Key":"ControlGroup","Title":"","Logic":1,"Items":[],"ChildItems":[]}]}}',
    'PageName': 'AdvSearch',
    'DBCode': 'CFLS',
    'KuaKuCodes': 'CJFQ,CDMD,CIPD,CCND,CISD,SNAD,BDZK,CCJD,CCVD,CJFN',
    'CurPage': '1',
    'RecordsCntPerPage': '20',
    'CurDisplayMode': 'listmode',
    'CurrSortFieldType': 'desc',
    'IsSentenceSearch': 'false',
    }
headers = {
    'Accept': 'text/html, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '1227',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'cangjieConfig_NZKPT2=%7B%22status%22%3Atrue%2C%22startTime%22%3A%222021-12-23%22%2C%22endTime%22%3A%222022-04-12%22%2C%22orginHosts%22%3A%22kns.cnki.net%22%2C%22type%22%3A%22mix%22%2C%22poolSize%22%3A%2210%22%2C%22intervalTime%22%3A10000%2C%22persist%22%3Afalse%7D; ASP.NET_SessionId=kniydevgw4tvieonv13oa4cg; SID_kns8=015123155; dblang=ch; _pk_id=109e9711-1720-49b3-b25d-62a1781db33c.1650512686.1.1650512686.1650512686.; _pk_ses=*; SID_kns_new=kns123106; Ecp_ClientId=2220421114403679955; Ecp_IpLoginFail=22042136.113.112.98; knsLeftGroupSelectItem=1%3B2%3B',
    'Host': 'kns.cnki.net',
    'Origin': 'https://kns.cnki.net',
    'Referer': 'https://kns.cnki.net/kns8/AdvSearch?dbprefix=CFLS&&crossDbcodes=CJFQ%2CCDMD%2CCIPD%2CCCND%2CCISD%2CSNAD%2CBDZK%2CCCJD%2CCCVD%2CCJFN',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    }

resp = requests.post(url, data=datas, headers=headers)

page = BeautifulSoup(resp.text, "html.parser")

titles = []
ytitles = page.find_all("a", class_="fz14")
for ytitle in ytitles:
    titles.append(ytitle.text)
print(titles)
