import pandas as pd 
import matplotlib.pyplot as plt

climate= pd.read_csv("E:\data\climate.csv")
print(climate)


plt.figure()
plt.plot(climate["date"],climate["wind_speed"],color="red",label="wind speed")
plt.plot(climate["date"],climate["humidity"],color="green",label='humidity')
plt.xticks(rotation = 90)
plt.legend()
plt.show()


plt.bar(climate["date"],climate["wind_speed"],color="violet",label="wind speed")
plt.xticks(rotation = 90)
plt.legend()
plt.show()


plt.scatter(climate["humidity"],climate["meantemp"],color="black",label="mean temp")
plt.xticks(rotation = 90)
plt.legend()
plt.show()


