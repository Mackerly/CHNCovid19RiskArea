# 获取 gov.cn 发布的疫情风险地区

import hashlib,time,requests

e = n = str(time.time())[:10]
a = "23y0ufFl5YxIyGrI8hWRUZmKkvtSjLQA"
i = "123456789abcdefg"
s = "zdww"

signatureHeader = hashlib.sha256((e + a + i + e).encode("utf-8")).hexdigest().upper()
o = hashlib.sha256((n + "fTN2pfuisxTavbTuYVSsNJHetwq5bJvCQkjjtiLM2dCratiA" + n).encode("utf-8")).hexdigest().upper()

a = {
    "appId": "NcApplication",
    "paasHeader": s,
    "timestampHeader": e,
    "nonceHeader": i,
    "signatureHeader": signatureHeader,
    "key":"3C502C97ABDA40D0A60FBEE50FAAD1DA"
}

headers={
    "x-wif-nonce": "QkjjtiLM2dCratiA",
    "x-wif-paasid": "smt-application",
    "x-wif-signature": o,
    "x-wif-timestamp": n,
    "Content-Type": "application/json; charset=utf-8"
}

url = "http://103.66.32.242:8005/zwfwMovePortal/interface/interfaceJson"

r = requests.post(url,headers=headers,json=a)
risks = r.json()

end_time = risks['data']['end_update_time']
high_count = risks['data']['hcount']
middle_count = risks['data']['mcount']

str1 = '截止到 {end_time}，全国共有高风险地区 {high_count} 个；中风险地区 {middle_count} 个'.format(end_time=end_time,high_count=high_count,middle_count=middle_count)
print(str1)

print("高风险地区有：")
# 取消注释可以获取详细区域
# for x in risks['data']['highlist']:
#     print(x['area_name'] + '\n   ' + '\n   '.join(x['communitys']) + '\n')

# 简略显示
for x in risks['data']['highlist']:
    print(x['area_name'])

print()
print("中风险地区有：")
# 取消注释可以获取详细区域
# for x in risks['data']['middlelist']:
#     print(x['area_name'] + '\n   ' + '\n   '.join(x['communitys']) + '\n')

# 简略显示
for x in risks['data']['middlelist']:
    print(x['area_name'])
