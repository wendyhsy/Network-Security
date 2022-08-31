import http.client, urllib.parse, sys
from pymd5 import md5,padding
url = sys.argv[1]

# token=0c6edcc81c7714b37a87cee7bb1f3d89&
# m + padding(len(m)*8) + suffix
token = url[url.index("=") +1: url.index("&")]
# user=aturing&command1=ListSquirrels&command2=NoOp
m=url[url.index("&")+1:]
# add 10-character password at the beginning
len_m=len(m)+10
bits = (len_m + len(padding(len_m * 8))) * 8
suffix = "&command3=UnlockAllSafes"

# h = m.encode() + padding(len(m)*8) + suffix.encode()
h = md5(state=bytes.fromhex(token), count=bits)
h.update(suffix.encode())
newToken=str(h.hexdigest())
url=url[:url.index("=")+1]+newToken+url[url.index("&"):]+urllib.parse.quote(padding(len_m * 8))+suffix
parsedUrl = urllib.parse.urlparse(url)
conn = http.client.HTTPConnection(parsedUrl.hostname,parsedUrl.port)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print(conn.getresponse().read())
