import re
from requests import Session
from lxml import html
import requests




def parsePhone(r):
    code_with_num = {}
    icons = re.findall('\.icon-(.*?):before',r.text)
    for icon in icons[:10]:
        try:
            code = re.search('\.icon-'+icon+':before\{content:"(.*?)"\}',r.text).group(1).replace('\\','')
            if code == '9d002':
                num = 0
            if code == '9d004':
                num = 1
            if code == '9d001':
                num = 2
            if code == '9d005':
                num = 3
            if code == '9d010':
                num = 4
            if code == '9d007':
                num = 5               
            if code == '9d009':
                num = 6
            if code == '9d003':
                num = 7
            if code == '9d006':
                num = 8                
            if code == '9d008':
                num = 9
            code_with_num[icon] = num
        except:
            pass
    # return code_with_num
    tree = html.fromstring(r.text)
    ph = ""
    for i in tree.xpath('//span[@class="telCntct"]//a[@class="tel ttel"]//span/@class'):
        p = code_with_num[i.split('-')[1]]
        ph+=str(p)
    return ph
    



def parseDetail(name,doc_id):
    headers = {'authority': 'www.justdial.com',
    'accept': '*/*',
    'accept-language': 'en-GB,en;q=0.9',
    'referer': 'https://www.justdial.com/Delhi/Jackson-Hospital-Opposite-Jain-Bharti-Model-School-Rohini-Sector-16/011PXX11-XX11-180327200446-C2G1_BZDET?catid=&checkin=&checkout=&vpfs=&stxt=General%2520Physician%2520Doctors&nid=10892680&stype=category_list&search=Medical-Practitioners&area=Opposite%20Jain%20Bharti%20Model%20School%20Rohini%20Sector%2016&type=Hospitals&totalJdReviews=undefined&bdmsgtype=7&bdcaptiontype=6&bdpage=rsltpge&bdText=Enquire%20Now&srcterm=Jackson%20Hospital',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/103.0.5060.53'}


    cookies = {'Continent': 'AS',
        'abtest': '1',
        'touch': '2450368704.11043.0000',
        'AKA_A2': 'A',
        'bm_sz': 'C5950AE799CD141B64BAD26959B6EAC2~YAAQj7YRYHug17KBAQAAegWSsxDb3oD6nAaqYcWZL/LxIwvqoOxt+AN2CPAZrzr5UNFOQ3YbWWWXQMsj9rooWuyBQig/WddR2KHHf6KfbKpr3jdUFJGxRe8RGwMNusHzVVysLBirnHZrwJVsmSu0gxqTOI0ano3ln/a+pr7u49Vu6VkM4FE14Ws/47hCjUVXcHGrn5KnSdOMtGGKMtU9H3qg6S0Z9J7RLj/iNQneOcdGuN+156kkyvKZOJMXfrKOh7GD18R+E/Am7iLAv2OgCfMjfuQWfGTAhUa9k1RHkG03WIAHGQ==~3553333~3684147',
        'sesidexp': 'Thu%20Jun%2030%202022%2014:15:00%20GMT+0530%20(India%20Standard%20Time)',
        'session_id': 'bmoPhZsdZS74yrWpBT7DL',
        'deviceId': '16565751007370026',
        'ak_bmsc': '66873AEFE1F76CF020519AB2B633F257~000000000000000000000000000000~YAAQj7YRYMCg17KBAQAAugmSsxD0HwyTq7n7xAJobNNPs5b0g8fKASzNz4mOY7lxc7uRiwNH7BAABvGcXAWaBgrPY6/4tLrLj7ogK7vBy5mOMtdrYf/DeQRHzJ0jJPfUNgPXNQjUFirNE8453para1ZPIgULVpifw6mLxbkwMWRvikcijERgj80AqhOQ4ImkjSY2pfV1eK+m9aIhcHZTvFZxZO9ul784pyNbYQlJgDzTLfAIQSgzpXjLL6kOGemz9G5AqLE5HDroCMmg+I0MxISHbw3GtucGcbfFmuabmcwFNQLgjuMgov6Zt3+7Ct4q8Fnbv3mo76vhRWpi+TbwCChe7C0GJA07QrBW2cS5Jy9tXFvE3Xzyt7lSwyBAoObvZxRT8UTfGpytiCYImL+lq5uKNVOo/S54g5KmdhUABq8KzH7pZ6qZuurGpra6mcg8uVZhu+11g8efCZXltvLEdupfcbDB21191b05rGF/J9+O3NiDoroMcSRezPad4yOso77zkUwyhrxbGg==',
        '_ga': 'GA1.2.1372415906.1656575103',
        '_gid': 'GA1.2.1442130677.1656575103',
        '_gat': '1',
        '_gat_UA-31027791-3': '1',
        '_fbp': 'fb.1.1656575103357.799939893',
        'ipdetect': '{%22area%22:%22Mahendra%20Park-jahangirpuri%22%2C%22city%22:%22Delhi%22%2C%22state%22:%22%22%2C%22pincode%22:%22110033%22%2C%22data_city%22:%22Delhi%22%2C%22ipdetect%22:true}',
        'PHPSESSID': 'ul3ko4j33ofurg1eh75oamp621',
        'isjdmv': '0',
        'jtkr0': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2NTY1NzUxMzcsImp0aSI6IkclMkJScU9WdjFET2VtUVZYJTJCZ0VwMFR5b1FpOGV0R29MTEh6dmRETlIyNlg0UDdaWTZKTzFhSWJQTjdZbm1uMlZ2ZmFLcElKQ2dYMlVGc1FyeHRERG5lZUI1cWlGJTJGbDk0SzJDUDFxbDRBYzk0JTNEIiwiaXNzIjoiMTkyLjE2OC4yMC4xMDEiLCJleHAiOjE2NTY1NzU3MzcsInNvdXJjZSI6IjIifQ.CCEBMbOhvM-UjIK1Tf9NxgoWA1dWHdchANMoPFBGqog',
        'apiHash': '16565751523778582',
        'jtkd': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2NTY1NzUxNTIsImp0aSI6Ik1JZUQlMkZuUUsyeWZOWHl0QWpWRGZyb0tLQzNQTHRNZTB5ZGdCcGxqUGhTWEJNJTJGTCUyQnZMQ01YZmw3bFl0ZlVjMU0iLCJpc3MiOiIxOTIuMTY4LjIwLjEwMSIsImV4cCI6MTY1NjU3NTc1Miwic291cmNlIjoiMiJ9.9ImTHw4WmQZokOxMHhwyYMKD9rYOtESQm_mNRHCH2z4',
        '_abck': '2057A7D464DF89266B90BC3EAADD33DC~0~YAAQj7YRYICp17KBAQAAjuOSswgSLICvf/lXjEWkbVkQUFy9eLGR55cg+z1o9YV3pWuVyIyz/wXAX+wwLd3aeau7eTIqTHKOphKyd43I1P9c4k0cqbHNIFXdL+1LlIbAKTzwS1PsFUyBmmMBVB/3jSa1tBwIDXv5WlsPuBHRpbPjUqjn37OWkJjW4kw8aAWASAmq4Qu5gF9ar/bB0w3KLLiMxe2DPr9dLlmr8VsLheGd8K4lJcupAq5sK64xY9MgD7xaZOxchD1gB6QbVYMjt8xoQjCjV9fGa5Hck50tt+bJLEhK9ZWzyUTSqL3e23w7seaZWgWph4DSpskWcffW6kBxNZo4rdjuMfJDljjYs9zOfS2HyG38/+SiDIvFYEINszzIuyayhee0Dz9x5eeUMoJOYdmnmmD9OZev~-1~-1~-1',
        'bm_sv': '54053225953FEF7480CA000AAF572545~YAAQj7YRYIGp17KBAQAAjuOSsxA2pciLZhoYzHD8oWQcMG9LWruDBWn8EfvlEaymx40t93TAmHJAU2hP1hWpze9WQva7573CHaFEFoCUbKIiG0F42PmjOnPJXHpOPEW2jbYPSXfkTb42Fepkm7ocu36W7ujQze5W0SaKMTgS+1zZSC/bSitoIcq1wHhbCVO43QCwsREfaJcjfZdQ7xt369/hjIxL17bF1AZ7Uh0yChn49Mu7DHF8sH3MzG+SGjz/DFk1~1',
        'RT': '"z=1&dm=justdial.com&si=7c5c7425-dbf5-4b61-a25b-5f316474979c&ss=l50q1jun&sl=2&tt=lm&rl=1&nu=1932oxzug&cl=1405&obo=1&ld=17s9&r=1932oxzug&ul=17sb&hd=18qi"'}



    params = {
        'search': name,
        'docid': doc_id,
        'prevdocid': '',
        'case': 'detail',
        'city': 'Delhi',
        'area': '',
        'usercity': 'Delhi',
        'wap': '2',
        'login_mobile': '',
        'mvbksrc': 'ft,pvr,cinemax,fc',
        'search_bdcatid': '',
        'bd_msgtype': '',
        'bd_captiontype': '',
        'bd_text': '',
        'vpfs': '8-100',
        'jdlite': '0',
        'keyword': '',
        'debugmode': '1',
        'dummy': '0',
        'querySieve': ['search', ''],
        'owner': '0',
        'freelist': '',
        'jde': '0',
        'new': '1',
        'b2b': '0',
        'national_catid': '',
        'catname': '',
        'sieve': '{"name":"detailModel","selector":"detail","runInit":false}',
        'trk': '0',
        'source': '2',
        'version': '2.7',
        'searchReferrer': 'gen',
        'utmCampaign': '',
        'utm_source': '',
        'utm_medium': ''
    }

    response = requests.get('https://www.justdial.com/api/india_api_write/20march2020/searchziva.php', params=params, cookies=cookies, headers=headers)
    js = response.json()
    phone = js['main']['maintab']['contactHtml']
    return phone




#https://www.justdial.com/Delhi/Dr-G-C-Singhal-Near-Shiv-Market-Paschim-Vihar/011PXX11-XX11-140619090451-L7P1_BZDET?xid=RGVsaGkgRG9jdG9ycw==



url = "https://www.justdial.com/Delhi/Fortis-Hospital-Near-Kela-Godam-Shalimar-Bagh/011PXX11-XX11-090408114842-K2Y4_BZDET"