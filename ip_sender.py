import urllib

my_ip = urllib.urlopen("http://ipinfo.io/ip").read()
#print (site)
result = urllib.urlopen("http://cogsix.com/ip_listener/" + my_ip)
 

