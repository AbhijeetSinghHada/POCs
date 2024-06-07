import json
from pprint import pprint
json_string = '{"firstname":"givenName","lastName":"sn","userEmail":"mail","userLDAP":"objectGUID","userLogin":"sAMAccountName","contactPhone":"mobile","serviceAccount":"EnragedCow","serviceAccountPassword":"D5KHR86PZMeTr948A2mXrMBL","hostName":"EC2AMAZ-MQN178H","deviceId":"14f42582-2799-42bb-8673-09f29e3522fa","primaryServer":{"ip":"","id":"primaryIp"},"isEnabled":true,"domain":{"id":"authd_GbuR3x7A3xUU99Echd0qTs","name":"bravo.internal"},"syncStatus":"InProgress","advFilters":[]}'
parsed_json = json.loads(json_string)
pprint(parsed_json)