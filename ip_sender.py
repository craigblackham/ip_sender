import urllib

my_ip = urllib.urlopen("http://ipinfo.io/ip").read().strip()
#print (my_ip)

#adding local mac address to prevent spam
my_mac = open("/sys/class/net/wlan0/address").readline().strip()
#print (my_mac)

url = "http://cogsix.com/ip_listener/" + my_ip + "/" + my_mac
print (url)

result = urllib.urlopen(url)
#print (result)
