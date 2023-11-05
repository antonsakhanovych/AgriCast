import os
import xarray as xr
import matplotlib.pyplot as plt

# Create a list to store all datasets
datasets = []

# Open the NetCDF files and append them to the list
files = ["climate/" + file for file in os.listdir("climate")]
for file in files:
    ds = xr.open_dataset(file)
    datasets.append(ds)


# Iterate through the datasets and plot the chosen variable
# for ds in datasets:
#     Print variables of dataset
    # print()
    # for var in ds.data_vars:
    #     print(ds[var].plot())

ds = datasets[0]
print(ds.data_vars)
# ds["BEDD"].plot()

# plt.savefig('plot.png')

#dataframe = ds.to_dataframe()
#dataframe.to_csv("my_dataset.csv")
