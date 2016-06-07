#/usr/bin/python
#! coding = gbk

import urllib2, json, csv

url = 'http://apis.baidu.com/showapi_open_bus/showapi_joke/joke_text?page=1'
req = urllib2.Request(url)
req.add_header("apikey", "8cbdc46ade09e505fd44c06a8d5eaae8")

resp = urllib2.urlopen(req)
content = resp.read()

json_result = json.loads(content)
content_list = json_result['showapi_res_body']['contentlist']

# output to a csv file
output_file = open("jokes,csv", "wb")
for item in content_list :
    # codec is  wrong
    print item['title']
    output_file.write("%s\t%s\n" % (item['text'].decode('gbk'), item['ct']))

    