filename = 'download/GSL_C3S-glob-agric_gfdl-esm2m_rcp4p5_yr_20410101-20701231_v1.0.nc'

import netCDF4
nc_file = netCDF4.Dataset(filename, "r")

variable_names = list(nc_file.variables.keys())

# Print the variable names
for name in variable_names:
    print(name)

gsl_data = nc_file.variables["GSL"]
print(gsl_data)
nc_file.close()

data = gsl_data[:]  # Use the [:] slice notation to get the entire array
print(data)