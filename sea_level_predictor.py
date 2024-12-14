import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Import the dataset
df = pd.read_csv('epa-sea-level.csv')

# Create scatter plot
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

# Set labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')

# Perform linear regression on all data
slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

# Create the line of best fit for all data
years_extended = range(1880, 2051)  # Include years from 1880 to 2050
sea_level_fit = [slope * year + intercept for year in years_extended]

# Plot the line of best fit (all data)
plt.plot(years_extended, sea_level_fit, label='Best Fit Line (All Data)', color='blue')

# Filter the data for years from 2000 onwards
df_recent = df[df['Year'] >= 2000]

# Perform linear regression on the filtered data
slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

# Create the line of best fit for the recent data
sea_level_fit_recent = [slope_recent * year + intercept_recent for year in years_extended]

# Plot the line of best fit (2000 onwards)
plt.plot(years_extended, sea_level_fit_recent, label='Best Fit Line (2000 Onwards)', color='red')

# Display the legend
plt.legend()

# Save the plot as an image
plt.savefig('sea_level_rise.png')

# Show the plot
plt.show()
