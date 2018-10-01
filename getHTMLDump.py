import json, requests, sys, os

headers = {"authority": "www.zomato.com", "method": "GET", "path": "/bangalore/restaurants", "scheme": "https", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "accept-encoding": "gzip, deflate, br", "accept-language": "en-US,en;q=0.9", "cache-control": "no-cache", "pragma": "no-cache", "upgrade-insecure-requests": "1",  "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}


cities = [#("ahmedabad", 218),
          #("chandigarh", 169),
          #("goa", 138),
          #("indore", 98 ),
          #("gangtok",  8),
          #("nashik", 39),
          #("ooty", 15),
          #("shimla",10),
          #("ludhiana", 83),
          ("guwahati", 62),
          ("amritsar", 39),
          ("kanpur", 48),
          ("allahabad", 27),
          ("aurangabad", 43),
          ("bhopal", 67),
          ("ranchi", 29),
          ("visakhapatnam", 55),
          ("bhubaneswar", 69),
          ("coimbatore", 113),
          ("mangalore", 35),
          ("vadodara", 80),
          ("nagpur", 137),
          ("agra", 47),
          ("dehradun", 67),
          ("mysore", 44),
          ("puducherry", 37),
          ("surat", 63),
          ("varanasi", 33),
          ("patna", 36),
          ("udaipur", 45),
          ("srinagar", 8),
          ("neemrana", 2),
          ("cuttack", 15),
          ("trivandrum", 39),
          ("haridwar", 12),
          ("pushkar", 8),
          ("rajkot", 17),
          ("madurai", 31),
          ("alappuzha", 15),
          ("thrissur", 17),
          ("vijayawada", 35),
          ("jodhpur", 23),
          ("kota", 14),
          ("ajmer", 17),
          ("mussoorie", 10),
          ("rishikesh", 12),
          ("jalandhar", 16),
          ("jammu", 12),
          ("manali", 16),
          ("manipal", 12),
          ("dharamshala", 12),
          ("raipur", 47),
          ("gorakhpur", 15),
          ("udupi", 10),
          ("palakkad", 8),
          ("darjeeling", 8),
          ("siliguri", 22),
          ("nainital", 8),
          ("meerut", 18),
          ("vellore", 13),
          ("salem", 14),
          ("trichy", 18),
          ("patiala", 9),
          ("jabalpur", 15),
          ("gwalior", 20),
          ("jamshedpur", 18),
          ("guntur", 17),
          ("jhansi", 9)]

for ci in cities:
    print(ci)
    city = ci[0]
    city_no = ci[1]
    try:
        os.mkdir(city)
    except:
        pass
    for i in range(1, city_no):
        url = "https://www.zomato.com/" + city + "/restaurants?page=" + str(i)
        with open(city + "/file-" + str(i), "w") as outfile:
            try:
                json.dump(requests.get(url, headers= headers).text, outfile)
            except:
                print("Failed city: " + city + " at: " + str(i))
