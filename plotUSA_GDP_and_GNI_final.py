import numpy as np
import matplotlib.pyplot as plt

#   close all figures
plt.close('all')

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


years2 = np.array([1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014])
usaGNI = np.array([612178550047.646,646233886826.65,692328219512.945,753294530375.941,824183577234.192,868295290971.962,952033980993.251,1027990251284.03,1098553055567.61,1183038457083.86,1320921418184.74,1548458249174.67,1711839855738.22,1842214711486.27,1958767403397.59,2117456144199.84,2401109359261.26,2751769589536.9,3048093901726.34,3303883972259.98,3297652203866.24,3411202239818.87,3828479505092.12,4164905103485.73,4601500378186.56,5200354088055.45,5765196251790.1,5888830786924.1,6029529322891.06,6164277951121.71,6612706041742.15,6883086506452.91,7302781827892.38,7760854970064.45,8184808773787.28,8558708987900.82,8869581532268.98,9425292191447.05,10178500697503.7,10498594829042.2,10776200783181,11589035965657.3,12790914724399.8,13693955258225.3,14345564947204.5,14651211130474,15002428215985,14740580035992.9,15143137264678.1,15727290871234.6,16501015978642.4,17001290051112.6,17611490812741.3])
#   GNI data atlas method from the worldbank http://databank.worldbank.org/data/reports.aspx?source=2&country=USA&series=&period=#
#   CPI data from bureau of labor statistics http://data.bls.gov/pdq/SurveyOutputServlet
usaCPI2 = np.array([30.2, 30.6, 31.0, 31.5, 32.4, 33.4, 34.8, 36.7, 38.8, 40.5, 41.8, 44.4, 49.3, 53.8, 56.9, 60.6, 65.2, 72.6, 82.4, 90.9, 96.5, 99.6, 103.9, 107.6, 109.6, 113.6, 118.3, 124.0, 130.7, 136.2, 140.3, 144.5, 148.2, 152.4, 156.9, 160.5, 163.0, 166.6, 172.2, 177.1, 179.9, 184.0, 188.9, 195.3, 201.6, 207.342, 215.303, 214.537, 218.056, 224.939, 229.594, 232.957, 236.736])

plt.figure()
plt.plot(years2, usaGNI)
plt.xlabel('Year')
plt.ylabel('GNI in Current USD')
plt.grid(True)
plt.show()

#   Adjust GNI for 1962 USD
usaGNI1962 = usaGNI / (usaCPI2 / usaCPI2[0])

plt.figure()
plt.plot(years2, usaGNI1962)
plt.xlabel('Year')
plt.ylabel('GNI adjusted for inflation to 1962 USD')
plt.grid(True)
plt.show()

#   Adjust GNI for 2014 USD
usaGNI2014 = usaGNI / (usaCPI2 / usaCPI2[-1])

plt.figure()
plt.plot(years2, usaGNI2014)
plt.xlabel('Year')
plt.ylabel('GNI adjusted for inflation to 2014 USD')
plt.grid(True)
plt.show()

#   population from world bank
usaPop = np.array([186538000,189242000,191889000,194303000,196560000,198712000,200706000,202677000,205052000,207661000,209896000,211909000,213854000,215973000,218035000,220239000,222585000,225055000,227225000,229466000,231664000,233792000,235825000,237924000,240133000,242289000,244499000,246819000,249623000,252981000,256514000,259919000,263126000,266278000,269394000,272657000,275854000,279040000,282162411,284968955,287625193,290107933,292805298,295516599,298379912,301231207,304093966,306771529,309347057,311721632,314112078,316497531,318857056])
usaGNIpercapita = usaGNI / usaPop

plt.figure()
plt.plot(years2, usaGNIpercapita)
plt.xlabel('Year')
plt.ylabel('GNI per capita in Current USD')
plt.grid(True)
plt.show()

#   adjust GNI per Capita to 1962s numbers
usaGNIpercapita1962 = usaGNIpercapita / (usaCPI2 / usaCPI2[0])
plt.figure()
plt.plot(years2, usaGNIpercapita1962)
plt.xlabel('Year')
plt.ylabel('GNI per capita adjusted for inflation to 1962 USD')
plt.grid(True)
plt.show()

#   adjust GNI per Capita to 2014s numbers
usaGNIpercapita2014 = usaGNIpercapita / (usaCPI2 / usaCPI2[-1])
plt.figure()
plt.plot(years2, usaGNIpercapita2014)
plt.xlabel('Year')
plt.ylabel('GNI per capita adjusted for inflation to 2014 USD')
plt.grid(True)
plt.show()

#   close all figs
plt.close('all')

#   save the final plots
#   plot of the GDP and GNI in current USD
plt.figure()
plt.plot(years, usaGDP / 1.e12, '-k', label='GDP')
plt.plot(years2, usaGNI / 1.e12, '--b', label='GNI')
plt.xlabel('Year')
plt.ylabel('Trillion USD')
plt.legend(loc=4)
plt.grid(True)
plt.show()
plt.savefig('images/usaGDPandGNI.png')
#   plot of GDP and GNI per capita in current USD
plt.figure()
plt.plot(years, usaGDPpercapita, '-k', label='GDP')
plt.plot(years2, usaGNIpercapita, '--b', label='GNI')
plt.xlabel('Year')
plt.ylabel('USD per capita')
plt.legend(loc=4)
plt.grid(True)
plt.show()
plt.savefig('images/usaGDPandGNI_perCapita.png')
#   plot of GDP and GNI per capita in 2014 USD
plt.figure()
plt.plot(years, usaGDPpercapita2014, '-k', label='GDP')
plt.plot(years2, usaGNIpercapita2014, '--b', label='GNI')
plt.xlabel('Year')
plt.ylabel('USD per capita adjusted for inflation to 2014 levels')
plt.legend(loc=4)
plt.grid(True)
plt.show()
plt.savefig('images/usaGDPandGNI_perCapita_2014.png')
#   plot of GDP at 0.5, 1, and 2 perecent estimations
#   what if CPI has underestimated inflation?
cpiUnderHalf = adjustCPI(usaCPI, 1.005)
cpiUnderOne = adjustCPI(usaCPI, 1.01)
cpiUnderTwo = adjustCPI(usaCPI, 1.02)
#   what if CPI has overestimated inflation? 
cpiOverHalf = adjustCPI(usaCPI, 0.995)
cpiOverOne = adjustCPI(usaCPI, 0.99)
cpiOverTwo = adjustCPI(usaCPI, 0.98)
#   recalculate GDP basedd on the CPI values
usaGDPpercapita2014UnderHalf = usaGDPpercapita / (cpiUnderHalf / cpiUnderHalf[-1])
usaGDPpercapita2014UnderOne = usaGDPpercapita / (cpiUnderOne / cpiUnderOne[-1])
usaGDPpercapita2014UnderTwo = usaGDPpercapita / (cpiUnderTwo / cpiUnderTwo[-1])
usaGDPpercapita2014OverHalf = usaGDPpercapita / (cpiOverHalf / cpiOverHalf[-1])
usaGDPpercapita2014OverOne = usaGDPpercapita / (cpiOverOne / cpiOverOne[-1])
usaGDPpercapita2014OverTwo  = usaGDPpercapita / (cpiOverTwo  / cpiOverTwo[-1])
plt.figure()
plt.plot(years, usaGDPpercapita2014, '-k', label='Adjusted to 2014 CPI')
plt.plot(years, usaGDPpercapita2014UnderHalf, '--k', label='CPI each year adjusted +0.5%')
plt.plot(years, usaGDPpercapita2014OverHalf, '-.k', label='CPI each year adjusted -0.5%')
plt.xlabel('Year')
plt.ylabel('GDP per capita adjusted for inflation (USD)')
plt.legend(loc=4)
plt.grid(True)
plt.show()
plt.savefig('images/usaGDPandGNI_perCapita_2014_half.png')
plt.figure()
plt.plot(years, usaGDPpercapita2014, '-k', label='Adjusted to 2014 CPI')
plt.plot(years, usaGDPpercapita2014UnderOne, '--k', label='CPI each year adjusted +1.0%')
plt.plot(years, usaGDPpercapita2014OverOne, '-.k', label='CPI each year adjusted -1.0%')
plt.xlabel('Year')
plt.ylabel('GDP per capita adjusted for inflation (USD)')
plt.legend(loc=4)
plt.grid(True)
plt.show()
plt.savefig('images/usaGDPandGNI_perCapita_2014_one.png')
plt.figure()
plt.plot(years, usaGDPpercapita2014, '-k', label='Adjusted to 2014 CPI')
plt.plot(years, usaGDPpercapita2014UnderTwo, '--k', label='CPI each year adjusted +2.0%')
plt.plot(years, usaGDPpercapita2014OverTwo, '-.k', label='CPI each year adjusted -2.0%')
plt.xlabel('Year')
plt.ylabel('GDP per capita adjusted for inflation (USD)')
plt.legend(loc=4)
plt.grid(True)
plt.show()
plt.savefig('images/usaGDPandGNI_perCapita_2014_two.png')