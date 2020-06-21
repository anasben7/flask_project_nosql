from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import datetime
import json
import tweepy
from pymongo import MongoClient

client = MongoClient('127.0.0.1', 27017)
db = client.test1



#Variables that contains the user credentials to access Twitter API
ACCESS_TOKEN = "4518193835-XGOBCZibmnUdgkPZM3CGLL6JFKqoAktx1VimWYD"
ACCESS_TOKEN_SECRET = "GQrGPwhJehHwhQiw7pTC4CzXMioRLBFNWSpiwqIzkZAjA"
CONSUMER_KEY = "XRuZQD2Sq8Ojtvo3dbe1Z2U0M"
CONSUMER_SECRET = "FRjWoFHTSxWKIYfRZCsifD6jRJRjTJBunet8JUj4pJOiZp2y4x"

def clean_tweets(x):
    x = x.replace('#','')
    return x

def replace_null(x):
    if x is None:
        x=0 
    return x

if __name__ == '__main__':
        auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)
        tags = api.trends_place(23424977)
        print(tags)
        
        for a in tags :
             for b in a["trends"]:
                 db.tweets.insert_one({"tweet":clean_tweets(b["name"]),"url":b["url"],"tweet_volume":replace_null(b["tweet_volume"]),"Country":"USA","as_of":datetime.datetime.now()})
                
            



#Countries IDs

 # USA=23424977
 # UK=23424975
 # Canada=23424768
 # Australia=23424748



#USA States IDs

# New York, New York, 2459115
# Los Angeles, California, 2442047
# Chicago, Illinois, 2379574
# Houston, Texas, 2424766
# Phoenix, Arizona, 2471390
# Philadelphia, Pennsylvania, 2471217
# San Antonio, Texas, 2487796
# Dallas, Texas, 2388929
# San Diego, California, 2487889
# San Jose, California, 2488042
# Detroit, Michigan, 2391585
# San Francisco, California, 2487956
# Jacksonville, Florida, 2428344
# Indianapolis, Indiana, 2427032
# Austin, Texas, 2357536
# Columbus, Ohio, 2383660
# Fort Worth, Texas, 28340407
# Charlotte, North Carolina, 2378426
# Memphis, Tennessee, 2449323
# Baltimore, Maryland, 2358820
# Boston, Massachusetts, 2367105
# El Paso, Texas, 2397816
# Milwaukee, Wisconsin, 2451822
# Denver, Colorado, 2391279
# Seattle, Washington, 2490383
# Nashville, Tennessee, 2457170
# Washington, District of Columbia, 2514815
# Las Vegas, Nevada, 2436704
# Portland, Oregon, 2475687
# Louisville, Kentucky, 2442327
# Oklahoma City, Oklahoma, 2464592
# Tucson, Arizona, 2508428
# Atlanta, Georgia, 2357024
# Albuquerque, New Mexico, 2352824
# Kansas City, Missouri, 2430683
# Fresno, California, 2407517
# Sacramento, California, 2486340
# Long Beach, California, 2441472
# Mesa, Arizona, 2449808
# Omaha, Nebraska, 2465512
# Cleveland, Ohio, 2381475
# Virginia Beach, Virginia, 2512636
# Miami, Florida, 2450022
# Oakland, California, 2463583
# Raleigh, North Carolina, 2478307
# Tulsa, Oklahoma, 2508533
# Minneapolis, Minnesota, 2452078
# Colorado Springs, Colorado, 2383489
# Honolulu, Hawaii, 2423945
# Arlington, Texas, 2355944
# Wichita, Kansas, 2520077
# St. Louis, Missouri, 2486982
# Tampa, Florida, 2503863
# Santa Ana, California, 2488802
# New Orleans, Louisiana, 2458833
# Anaheim, California, 2354447
# Cincinnati, Ohio, 2380358
# Bakersfield, California, 2358492
# Aurora, Colorado, 2357473
# Pittsburgh, Pennsylvania, 2473224
# Riverside, California, 2482128
# Toledo, Ohio, 2506911
# Stockton, California, 2500105
# Corpus Christi, Texas, 2385304
# Lexington, Kentucky, 2438841
# St. Paul, Minnesota, 2487129
# Anchorage, Alaska, 2354490
# Newark, New Jersey, 2459269
# Buffalo, New York, 2371464
# Plano, Texas, 2473475
# Henderson, Nevada, 2419946
# Lincoln, Nebraska, 2439482
# Fort Wayne, Indiana, 2406008
# Glendale, Arizona, 2411084
# Greensboro, North Carolina, 2414469
# Chandler, Arizona, 2378015
# St. Petersburg, Florida, 2487180
# Jersey City, New Jersey, 2429187
# Scottsdale, Arizona, 2490057
# Norfolk, Virginia, 2460389
# Madison, Wisconsin, 2443945
# Orlando, Florida, 2466256
# Birmingham, Alabama, 2364559
# Baton Rouge, Louisiana, 2359991
# Durham, North Carolina, 2394734
# Laredo, Texas, 2436565
# Lubbock, Texas, 2442818
# Chesapeake, Virginia, 2379200
# Chula Vista, California, 2380213
# Garland, Texas, 2408976
# Winston-Salem, North Carolina, 2522292
# North Las Vegas, Nevada, 2461253
# Reno, Nevada, 2480201
# Gilbert, Arizona, 2410128
# Hialeah, Florida, 2420610
# Arlington, Virginia, 2355942
# Akron, Ohio, 2352491
# Irvine, California, 2427665
# Rochester, New York, 2482949
# Boise, Idaho, 2366355
# Modesto, California, 2452629
# Fremont, California, 2407405
# Montgomery, Alabama, 2453369
# Spokane, Washington, 2497646
# Richmond, Virginia, 2480894
# Yonkers, New York, 2524811
# Irving, Texas, 2427690
# Shreveport, Louisiana, 2493227
# San Bernardino, California, 2487870
# Tacoma, Washington, 2503523
# Glendale, California, 2411009
# Des Moines, Iowa, 2391446
# Augusta, Georgia, 2357383
# Grand Rapids, Michigan, 2412843
# Huntington Beach, California, 2425873
# Mobile, Alabama, 2452537
# Moreno Valley, California, 2453984
# Little Rock, Arkansas, 2440351
# Amarillo, Texas, 2354141
# Columbus, Georgia, 2383661
# Oxnard, California, 2467212
# Fontana, California, 2404850
# Knoxville, Tennessee, 2433662
# Fort Lauderdale, Florida, 2405797
# Worcester, Massachusetts, 2523945
# Salt Lake City, Utah, 2487610
# Newport News, Virginia, 2459618
# Huntsville, Alabama, 2426010
# Tempe, Arizona, 2504633
# Brownsville, Texas, 2370568
# Fayetteville, North Carolina, 2402726
# Jackson, Mississippi, 2428184
# Tallahassee, Florida, 2503713
# Aurora, Illinois, 2357467
# Ontario, California, 2465715
# Providence, Rhode Island, 2477058
# Overland Park, Kansas, 2466942
# Rancho Cucamonga, California, 2478522
# Chattanooga, Tennessee, 2378695
# Oceanside, California, 2464118
# Santa Clarita, California, 2488845
# Garden Grove, California, 2408784
# Vancouver, Washington, 2511258
# Grand Prairie, Texas, 2412837
# Peoria, Arizona, 2470457
# Rockford, Illinois, 2483357
# Cape Coral, Florida, 2374635
# Springfield, Missouri, 2498315
# Santa Rosa, California, 2488916
# Sioux Falls, South Dakota, 2494126
# Port St. Lucie, Florida, 2475492
# Dayton, Ohio, 2389876
# Salem, Oregon, 2487384
# Pomona, California, 2474876
# Springfield, Massachusetts, 2498304
# Eugene, Oregon, 2400539
# Corona, California, 2385250
# Pasadena, Texas, 2468963
# Joliet, Illinois, 2429708
# Pembroke Pines, Florida, 2470103
# Paterson, New Jersey, 2469081
# Hampton, Virginia, 2416847
# Lancaster, California, 2436084
# Alexandria, Virginia, 2353019
# Salinas, California, 2487460
# Palmdale, California, 2467721
# Naperville, Illinois, 2457000
# Pasadena, California, 2468964
# Kansas City, Kansas, 2430632
# Hayward, California, 2419175
# Hollywood, Florida, 2423467
# Lakewood, Colorado, 2435724
# Torrance, California, 2507261
# Syracuse, New York, 2503418
# Escondido, California, 2400183
# Fort Collins, Colorado, 2405641
# Bridgeport, Connecticut, 2368947
# Orange, California, 2465890
# Warren, Michigan, 2514383
# Elk Grove, California, 2398401
# Savannah, Georgia, 2489314
# Mesquite, Texas, 2449851
# Sunnyvale, California, 2502265
# Fullerton, California, 2408095
# McAllen, Texas, 2447466
# Cary, North Carolina, 2375810
# Cedar Rapids, Iowa, 2376926
# Sterling Heights, Michigan, 2499659
# Columbia, South Carolina, 2383552
# Coral Springs, Florida, 2384895
# Carrollton, Texas, 2375543
# Elizabeth, New Jersey, 2398316
# Hartford, Connecticut, 2418244
# Waco, Texas, 2512937
# Bellevue, Washington, 2362031
# New Haven, Connecticut, 2458410
# West Valley City, Utah, 2517863
# Topeka, Kansas, 2507158
# Thousand Oaks, California, 2505987
# El Monte, California, 2397796
# Independence, Missouri, 2426709
# McKinney, Texas, 2448187
# Concord, California, 2384020
# Visalia, California, 2512682
# Simi Valley, California, 2493889
# Olathe, Kansas, 2464639
# Clarksville, Tennessee, 2380893
# Denton, Texas, 2391230
# Stamford, Connecticut, 2498846
# Provo, Utah, 2477080
# Springfield, Illinois, 2498306
# Killeen, Texas, 2432286
# Abilene, Texas, 2351598
# Evansville, Indiana, 2400767
# Gainesville, Florida, 2408354
# Vallejo, California, 2510744
# Ann Arbor, Michigan, 2354842
# Peoria, Illinois, 2470456
# Lansing, Michigan, 2436453
# Lafayette, Louisiana, 2434560
# Thornton, Colorado, 2505922
# Athens, Georgia, 2356940
# Flint, Michigan, 2404367
# Inglewood, California, 2427199
# Roseville, California, 2484861
# Charleston, South Carolina, 2378319
# Beaumont, Texas, 2360899
# Victorville, California, 2512106
# Santa Clara, California, 2488836
# Costa Mesa, California, 2385447
# Miami Gardens, Florida, 2450083
# Manchester, New Hampshire, 2444674
# Miramar, Florida, 2452272
# Downey, California, 2393444
# Arvada, Colorado, 2356381
# Allentown, Pennsylvania, 2353412
# Westminster, Colorado, 2518344
# Waterbury, Connecticut, 2515048
# Norman, Oklahoma, 2460448
# Midland, Texas, 2450465
# Elgin, Illinois, 2398255
# West Covina, California, 2516864
# Clearwater, Florida, 2381303
# Cambridge, Massachusetts, 2373572
# Pueblo, Colorado, 2477147
# West Jordan, Utah, 2517245
# Round Rock, Texas, 2485177
# Billings, Montana, 2364254
# Erie, Pennsylvania, 2400052
# South Bend, Indiana, 2495968
# San Buenaventura (Ventura), California, 23417225
# Fairfield, California, 2401427
# Lowell, Massachusetts, 2442564
# Norwalk, California, 2462248
# Burbank, California, 2371863
# Richmond, California, 2480904
# Pompano Beach, Florida, 2474897
# High Point, North Carolina, 2421250
# Murfreesboro, Tennessee, 2456416
# Lewisville, Texas, 2438795
# Richardson, Texas, 2480733
# Daly City, California, 2389087
# Berkeley, California, 2362930
# Gresham, Oregon, 2414913
# Wichita Falls, Texas, 2520100
# Green Bay, Wisconsin, 2413753
# Davenport, Iowa, 2389559
# Palm Bay, Florida, 2467662
# Columbia, Missouri, 2383559
# Portsmouth, Virginia, 2475747
# Rochester, Minnesota, 2482950
# Antioch, California, 2355124
# Wilmington, North Carolina, 2521361



 

