import urllib2

url = "http://127.0.0.1:5000/api/v1/task/hello"

print urllib2.urlopen(url).read()