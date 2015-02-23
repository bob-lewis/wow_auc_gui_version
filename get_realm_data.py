__author__ = 'Bob'
import json
import httplib2,json

def realm_checker(server):
    pass



def api_page_get(server):
    print(str('http://eu.battle.net/api/wow/auction/data/' + server))
    request = str('http://eu.battle.net/api/wow/auction/data/' + server)
    h = httplib2.Http(".cache")
    content_headers, content = h.request(request,"GET")
    content = content.decode()
    obj = json.loads(content)
    for key, value in obj.items():
        x = (value[0])
        return (x['url'])

