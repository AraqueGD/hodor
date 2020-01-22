import requests
page = "http://158.69.76.135/level0.php"
my_id = {
    "id": "1229",
    "holdthedoor": "submit"
}
for i in range(0, 1024):
    requests.post(page, data=my_id)
