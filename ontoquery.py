import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'application/x-www-form-urlencoded',
    'Ocp-Apim-Subscription-Key': 'f4359d55860f459193ab439fd3a5b34c',
}

params = urllib.parse.urlencode({
})

expr = "expr=Composite(AA.AuN='mike smith')"
model = "model=latest"
count = "count=10"
offset = "offset=0"

query = expr +'&' + model + '&' + count +'&' + offset

try:
    conn = http.client.HTTPSConnection('api.labs.cognitive.microsoft.com')
    conn.request("POST", "/academic/v1.0/calchistogram?%s" % params, query, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))