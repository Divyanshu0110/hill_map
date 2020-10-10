import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import cartopy.crs as ccrs
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import cartopy.feature as cfeature

if __name__ == '__main__':
    dataframe = pd.read_csv("scottish_hills.csv")
    # let the relation be between height and latitude,as latitude goes up height goes up as well
    x = dataframe.Height
    y = dataframe.Latitude
    plt.figure(figsize=(10, 10))
    ax = plt.axes(projection=ccrs.Mercator())
    ax.coastlines('10m')
    ax.xaxis.set_visible(True)
    ax.yaxis.set_visible(True)
    ax.set_yticks([56, 57, 58, 59], crs=ccrs.PlateCarree())
    ax.set_xticks([-8, -6, -4, -2], crs=ccrs.PlateCarree())
    stats = linregress(x, y)
    longitude_formatter = LongitudeFormatter(zero_direction_label=True)
    latitude_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(longitude_formatter)
    ax.yaxis.set_major_formatter(latitude_formatter)
    ax.set_extent([-8, -1.5, 55.3, 59])
    plt.scatter(dataframe["Longitude"], dataframe["Latitude"], color="red", marker="^", transform=ccrs.PlateCarree())
    plt.show()
    m = stats.slope
    c = stats.intercept
    # y = mx+c
    plt.scatter(x, y)
    plt.plot(x, m * x + c, color="red", linewidth=3)
    plt.xlabel("Height", fontsize=20)
    plt.ylabel("Latitude", fontsize=20)
    plt.show()
