import numpy as np
import matplotlib.pyplot as plt

years = np.array([1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014])
usaGDP = np.array([543300000000.,563300000000.,605100000000.,638600000000.,685800000000.,743700000000.,815000000000.,861700000000.,942500000000.,1019900000000.,1075884000000.,1167770000000.,1282449000000.,1428549000000.,1548825000000.,1688923000000.,1877587000000.,2085951000000.,2356571000000.,2632143000000.,2862505000000.,3210956000000.,3344991000000.,3638137000000.,4040693000000.,4346734000000.,4590155000000.,4870217000000.,5252629000000.,5657693000000.,5979589000000.,6174043000000.,6539299000000.,6878718000000.,7308755000000.,7664060000000.,8100201000000.,8608515000000.,9089168000000.,9660624000000.,10284779000000.,10621824000000.,10977514000000.,11510670000000.,12274928000000.,13093726000000.,13855888000000.,14477635000000.,14718582000000.,14418739000000.,14964372000000.,15517926000000.,16163158000000.,16768053000000.,17419000000000.])
#   GDP data from the worldbank http://data.worldbank.org/indicator/NY.GDP.MKTP.CD/countries/US?display=graph

#   CPI data from bureau of labor statistics http://data.bls.gov/pdq/SurveyOutputServlet
usaCPI = np.array([29.6, 29.9, 30.2, 30.6, 31.0, 31.5, 32.4, 33.4, 34.8, 36.7, 38.8, 40.5, 41.8, 44.4, 49.3, 53.8, 56.9, 60.6, 65.2, 72.6, 82.4, 90.9, 96.5, 99.6, 103.9, 107.6, 109.6, 113.6, 118.3, 124.0, 130.7, 136.2, 140.3, 144.5, 148.2, 152.4, 156.9, 160.5, 163.0, 166.6, 172.2, 177.1, 179.9, 184.0, 188.9, 195.3, 201.6, 207.342, 215.303, 214.537, 218.056, 224.939, 229.594, 232.957, 236.736])

plt.figure()
plt.plot(years, usaGDP)
plt.xlabel('Year')
plt.ylabel('GDP in Current USD')
plt.grid(True)
plt.show()

#   Adjust GDP for 1960 USD
usaGDP1960 = usaGDP / (usaCPI / usaCPI[0])

plt.figure()
plt.plot(years, usaGDP1960)
plt.xlabel('Year')
plt.ylabel('GDP adjusted for inflation in 1960 USD')
plt.grid(True)
plt.show()

#   Adjust GDP for 2014 USD
usaGDP2014 = usaGDP / (usaCPI / usaCPI[-1])

plt.figure()
plt.plot(years, usaGDP2014)
plt.xlabel('Year')
plt.ylabel('GDP adjusted for inflation in 2014 USD')
plt.grid(True)
plt.show()

#   population from world bank
usaPop = np.array([180671000,183691000,186538000,189242000,191889000,194303000,196560000,198712000,200706000,202677000,205052000,207661000,209896000,211909000,213854000,215973000,218035000,220239000,222585000,225055000,227225000,229466000,231664000,233792000,235825000,237924000,240133000,242289000,244499000,246819000,249623000,252981000,256514000,259919000,263126000,266278000,269394000,272657000,275854000,279040000,282162411,284968955,287625193,290107933,292805298,295516599,298379912,301231207,304093966,306771529,309347057,311721632,314112078,316497531,318857056])
usaGDPpercapita = usaGDP / usaPop

plt.figure()
plt.plot(years, usaGDPpercapita)
plt.xlabel('Year')
plt.ylabel('GDP per capita in Current USD')
plt.grid(True)
plt.show()

#   adjust GDP per Capita to 1960s numbers
usaGDPpercapita1960 = usaGDPpercapita / (usaCPI / usaCPI[0])
plt.figure()
plt.plot(years, usaGDPpercapita1960)
plt.xlabel('Year')
plt.ylabel('GDP per capita adjusted for inflation in 1960 USD')
plt.grid(True)
plt.show()

#   adjust GDP per Capita to 2014s numbers
usaGDPpercapita2014 = usaGDPpercapita / (usaCPI / usaCPI[-1])
plt.figure()
plt.plot(years, usaGDPpercapita2014)
plt.xlabel('Year')
plt.ylabel('GDP per capita adjusted for inflation to 2014 USD')
plt.grid(True)
plt.show()

#   define a function to adjust the CPI based on an over or under estimation of 
#   the inflation rate, where rate is the percent increase or decrease change
#   where a precentage overesimate of 5% would be inputted as 1.05
def adjustCPI(cpi, rate):
    demo = []
    for i, j in enumerate(cpi):
        demo.append(j * (rate**i))
    return demo
#   what if we underestimated inflation?
cpiOverFive = adjustCPI(usaCPI, 1.005)
#   what if we underestimated inflation? 
cpiUnderFive = adjustCPI(usaCPI, 0.995)

#   adjust GDP per Capita to 2014s numbers
usaGDPpercapita2014OverFive = usaGDPpercapita / (cpiOverFive / cpiOverFive[-1])
usaGDPpercapita2014UnderFive = usaGDPpercapita / (cpiUnderFive / cpiUnderFive[-1])

plt.figure()
plt.plot(years, usaGDPpercapita2014, label='normal')
plt.plot(years, usaGDPpercapita2014OverFive, label='under')
plt.plot(years, usaGDPpercapita2014UnderFive, label='over')
plt.legend()
plt.xlabel('Year')
plt.ylabel('GDP per capita adjusted for inflation to 2014 USD')
plt.grid(True)
plt.show()

