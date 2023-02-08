# import json
# import requests
#
# URL = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=05e0f108-8ba3-45cb-ab50-fba37acf322c"  # Webhook地址
#
#
# def message(content):
#     data = {
#         "msgtype": "text",
#         "text": {
#             "content": content
#         }
#     }
#     data = json.dumps(data, ensure_ascii=False)
#     data = data.encode(encoding="utf-8")
#     r = requests.post(url=URL, data=data)
#     r = json.loads(r.text)
#     return r
#
#
# if __name__ == "__main__":
#     print(message("Hello World!"))
#     # {'errcode': 0, 'errmsg': 'ok'}
