import urllib.request

# acquire the public ip
external_ip = urllib.request.urlopen('http://ident.me').read().decode('utf8')

print(external_ip)