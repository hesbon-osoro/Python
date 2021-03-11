import speedtest
s =speedtest.Speedtest()
print("My Download Speed is :", s.download()/pow(10,6), " Mbps")
print("My Upload Speed is :", s.upload()/pow(10,6), " Mbps")
best_server = s.get_best_server()
for key, value in best_server.items():
    print("Best Servers: \n"+key, " : ",value)
closest_server = s.get_closest_server()
for key, value in closest_server[1].items():
    print("Closest Servers: \n"+key, " : ", value)