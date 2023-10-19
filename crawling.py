import spotify
import sys
import requests
import base64
import json
import logging

client_id = '2630eea3c01645fb85fa9ac51b96ac66'
client_secret = '0ed3794b588f4a36b4c1aae90c6e08c5'


endpoint = "https://accounts.spotify.com/api/token"

# python 3.x 버전
encoded = base64.b64encode("{}:{}".format(client_id, client_secret).encode('utf-8')).decode('ascii')

headers = {"Authorization": "Basic {}".format(encoded)}

payload = {"grant_type": "client_credentials"}

response = requests.post(endpoint, data=payload, headers=headers)

access_token = json.loads(response.text)['access_token']

headers = {"Authorization": "Bearer {}".format(access_token)}

# headers = {client_id, client_secret}

params = {
        "q": "SF9",          # 검색하려고 하는 str (필수)
        "type": "artist",    # q의 type (필수)
        "limit": "5",         # 불러오는 데이터 개수
        "market" : "KR"
        # "offset" 몇 번째부터 불러올 건지
    }


r = requests.get("https://api.spotify.com/v1/search", params=params, headers=headers)
    # 값 확인
print(r.status_code)    # 실행상태: 200(정상)
print(r.text)