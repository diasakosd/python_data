import tkinter as tk
import requests
import pandas as pd
import calendar
import matplotlib.pyplot as plt
import mysql.connector

# we use the url value to store the url of our desired dataset
url = 'https://www.stats.govt.nz/assets/Uploads/Effects-of-COVID-19-on-trade/Effects-of-COVID-19-on-trade-At-15-December-2021-provisional/Download-data/effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv'

# In order to download the file we will need to send a get request
get_success = requests.get(url)

# If the request is successful the status  HTTP 200 OK will be returned as 200 that will mean that the request has succeeded.
if get_success.status_code == 200:

    # Save the dataset to a csv file
    with open('covid19.csv', 'wb') as csvfile:
        csvfile.write(get_success.content)

    print('File downloaded and saved successfully.')
else:
    # If the request didn't succeed 
    print(f'Request failed!')
    
# Load the csv into a pandas dataframe in order to extract information from it and filter it.
df = pd.read_csv('covid19.csv')

def case_1():
    # Extract month from 'Date' column
    df['Month'] = pd.to_datetime(df['Date'], dayfirst=True).dt.month
        # Group by month and measure and sum the column 'Value'
    df_month = df.groupby(['Month', 'Measure'])['Value'].sum().reset_index()


    #1 -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    # Filter for '$' measure and calculate total for each month
    dollar_months = []
    for month in range(1, 13):
        dollar_month = df_month[(df_month['Month'] == month) & (df_month['Measure'] == '$')]['Value'].sum()
        dollar_months.append(dollar_month)

    print("\n----------------Months and Dollars----------------\n")
    # Print the dollar amounts for each month
    month_names = list(calendar.month_name)[1:]
    for month_name, dollar_month in zip(month_names, dollar_months):
        print(f'{month_name} = {dollar_month}\n')


    # Filter for 'Tonnes' measure and calculate total for each month
    tonnes_months = []
    for month in range(1, 13):
        tonnes_month = df_month[(df_month['Month'] == month) & (df_month['Measure'] == 'Tonnes')]['Value'].sum()
        tonnes_months.append(tonnes_month)

    print("\n----------------Months and Tonnes----------------\n")
    # Print the tonnes amounts for each month
    month_names = list(calendar.month_name)[1:]
    for month_name, tonnes_month in zip(month_names, tonnes_months):
        print(f'{month_name} = {tonnes_month}\n')
        
    # Bar graph for dollars
    plt.bar(df_month[df_month['Measure'] == '$']['Month'], dollar_months)
    plt.xlabel('Month')
    plt.ylabel('Dollars')
    plt.title('Total Trade Value in Dollars by Month')

    # Add label to the top of the graph
    plt.text(0.97, 1.05, 'Dollars per Month', ha='center', va='center', transform=plt.gca().transAxes,
             bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))

    plt.show()
    # Bar graph for tonnes
    plt.bar(df_month[df_month['Measure'] == 'Tonnes']['Month'], tonnes_months)
    plt.xlabel('Month')
    plt.ylabel('Tonnes')
    plt.title('Total Trade Volume in Tonnes by Month')

    # Add label to the top of the graph
    plt.text(0.97, 1.05, 'Tonnes per Month', ha='center', va='center', transform=plt.gca().transAxes,
             bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))

    plt.show()

    
def case_2():
        # Group by country and measure and sum 'Value'
    df_country = df.groupby(['Country', 'Measure'])['Value'].sum().reset_index()

    # Filter for '$' measure and calculate total for each country
    dollar_countries = []
    for country in df_country[df_country['Measure'] == '$']['Country']:
        dollar_country = df_country[(df_country['Country'] == country) & (df_country['Measure'] == '$')]['Value'].sum()
        dollar_countries.append(dollar_country)

    print("\n----------------Countries and Dollars----------------\n")
    # Print the dollar amounts for each country
    for country, dollar_country in zip(df_country[df_country['Measure'] == '$']['Country'], dollar_countries):
        print(f'{country} = {dollar_country}\n')


    # Filter for 'Tonnes' measure and calculate total for each country
    tonnes_countries = []
    for country in df_country[df_country['Measure'] == 'Tonnes']['Country']:
        tonnes_country = df_country[(df_country['Country'] == country) & (df_country['Measure'] == 'Tonnes')]['Value'].sum()
        tonnes_countries.append(tonnes_country)

    print("\n----------------Countries and Tonnes----------------\n")
    # Print the tonnes amounts for each country
    for country, tonnes_country in zip(df_country[df_country['Measure'] == 'Tonnes']['Country'], tonnes_countries):
        print(f'{country} = {tonnes_country}\n')


    plt.bar(df_country[df_country['Measure'] == '$']['Country'], dollar_countries)
    plt.xlabel('Country')
    plt.ylabel('Dollars')
    plt.title('Total Trade Value in Dollars by Country')

    # Make x-axis labels smaller
    plt.xticks(fontsize=7, rotation=0)

    # Add label to the top of the graph
    plt.text(0.97, 1.05, 'Dollars per Country', ha='center', va='center', transform=plt.gca().transAxes,
             bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))

    plt.show()

    plt.bar(df_country[df_country['Measure'] == 'Tonnes']['Country'], tonnes_countries)
    plt.xlabel('Country')
    plt.ylabel('Tonnes')
    plt.title('Total Trade Value in Tones by Country')

    # Make x-axis labels smaller
    plt.xticks(fontsize=7, rotation=0)

    # Add label to the top of the graph
    plt.text(0.97, 1.05, 'Tonnes per Country', ha='center', va='center', transform=plt.gca().transAxes,
             bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))

    plt.show()

def case_3():
        # Group by transport and measure and sum 'Value'
    df_transport = df.groupby(['Transport_Mode', 'Measure'])['Value'].sum().reset_index()

    # Filter for '$' measure and calculate total for each transport mode
    dollar_transports = []
    for transport in df_transport[df_transport['Measure'] == '$']['Transport_Mode']:
        dollar_transport = df_transport[(df_transport['Transport_Mode'] == transport) & (df_transport['Measure'] == '$')]['Value'].sum()
        dollar_transports.append(dollar_transport)

    print("\n----------------Transports and Dollars----------------\n")
    # Print the dollar amounts for each transport mode
    for transport, dollar_transport in zip(df_transport[df_transport['Measure'] == '$']['Transport_Mode'], dollar_transports):
        print(f'{transport} = {dollar_transport}\n')


    # Filter for 'Tonnes' measure and calculate total for each transport mode
    tonnes_transports = []
    for transport in df_transport[df_transport['Measure'] == 'Tonnes']['Transport_Mode']:
        tonnes_transport = df_transport[(df_transport['Transport_Mode'] == transport) & (df_transport['Measure'] == 'Tonnes')]['Value'].sum()
        tonnes_transports.append(tonnes_transport)

    print("\n----------------Transports and Tonnes----------------\n")
    # Print the tonnes amounts for each transport mode
    for transport, tonnes_transport in zip(df_transport[df_transport['Measure'] == 'Tonnes']['Transport_Mode'], tonnes_transports):
        print(f'{transport} = {tonnes_transport}\n')


    plt.bar(df_transport[df_transport['Measure'] == '$']['Transport_Mode'], dollar_transports)
    plt.xlabel('Transport Mode')
    plt.ylabel('Dollars')
    plt.title('Total Trade Value in Dollars by Transport Mode')

    # Make x-axis labels smaller
    plt.xticks(fontsize=7, rotation=0)

    # Add label to the top of the graph
    plt.text(0.97, 1.05, 'Dollars per Transport Mode', ha='center', va='center', transform=plt.gca().transAxes,
             bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))

    plt.show()

    plt.bar(df_transport[df_transport['Measure'] == 'Tonnes']['Transport_Mode'], tonnes_transports)
    plt.xlabel('Transport Mode')
    plt.ylabel('Tonnes')
    plt.title('Total Trade Value in Tonnes by Transport Mode')

    # Make x-axis labels smaller
    plt.xticks(fontsize=7, rotation=0)

    # Add label to the top of the graph
    plt.text(0.97, 1.05, 'Tonnes per Transport Mode', ha='center', va='center', transform=plt.gca().transAxes,
             bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))

    plt.show()
    
def case_4():
        #Group by weekday and measure and sum 'Value'
    df_weekday = df.groupby(['Weekday', 'Measure'])['Value'].sum().reset_index()

    #Filter for '$' measure and calculate total for each weekday
    dollar_weekdays = []
    for weekday in df_weekday[df_weekday['Measure'] == '$']['Weekday']:
        dollar_weekday = df_weekday[(df_weekday['Weekday'] == weekday) & (df_weekday['Measure'] == '$')]['Value'].sum()
        dollar_weekdays.append(dollar_weekday)

    print("\n----------------Weekdays and Dollars----------------\n")

    #Print the dollar amounts for each weekday
    for weekday, dollar_weekday in zip(df_weekday[df_weekday['Measure'] == '$']['Weekday'], dollar_weekdays):
        print(f'{weekday} = {dollar_weekday}\n')

    #Filter for Tonnes measure and calculate total for each weekday
    tonnes_weekdays = []
    for weekday in df_weekday[df_weekday['Measure'] == 'Tonnes']['Weekday']:
        tonnes_weekday = df_weekday[(df_weekday['Weekday'] == weekday) & (df_weekday['Measure'] == 'Tonnes')]['Value'].sum()
        tonnes_weekdays.append(tonnes_weekday)

    print("\n----------------Weekdays and Tonnes----------------\n")

    #Print the tonnes amounts for each weekday
    for weekday, tonnes_weekday in zip(df_weekday[df_weekday['Measure'] == 'Tonnes']['Weekday'], tonnes_weekdays):
        print(f'{weekday} = {tonnes_weekday}\n')

    plt.bar(df_weekday[df_weekday['Measure'] == '$']['Weekday'], dollar_weekdays)
    plt.xlabel('Weekday')
    plt.ylabel('Dollars')
    plt.title('Total Trade Value in Dollars by Weekday')

    #Make axis smaller to fit
    plt.xticks(fontsize=7, rotation=0)

    #Add label at the top of the graph
    plt.text(0.97, 1.05, 'Dollars per Weekday', ha='center', va='center', transform=plt.gca().transAxes,
            bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))

    plt.show()

    plt.bar(df_weekday[df_weekday['Measure'] == 'Tonnes']['Weekday'], tonnes_weekdays)
    plt.xlabel('Weekday')
    plt.ylabel('Tonnes')
    plt.title('Total Trade Value in Tonnes by Weekday')

    #Make x axis look smaller to fit
    plt.xticks(fontsize=7, rotation=0)

    #Add label to the top of the graph
    plt.text(0.97, 1.05, 'Tonnes per Weekday', ha='center', va='center', transform=plt.gca().transAxes,
            bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))

    plt.show()
    
def case_5():
        # Group by commodity and measure and sum 'Value'
    df_commodity = df.groupby(['Commodity', 'Measure'])['Value'].sum().reset_index()

    # Filter for '$' measure and calculate total for each commodity
    dollar_commodities = []
    for commodity in df_commodity[df_commodity['Measure'] == '$']['Commodity']:
        dollar_commodity = df_commodity[(df_commodity['Commodity'] == commodity) & (df_commodity['Measure'] == '$')]['Value'].sum()
        dollar_commodities.append(dollar_commodity)

    print("\n----------------Commodities and Dollars----------------\n")
    # Print the dollar amounts for each commodity
    for commodity, dollar_commodity in zip(df_commodity[df_commodity['Measure'] == '$']['Commodity'], dollar_commodities):
        print(f'{commodity} = {dollar_commodity}\n')


    # Filter for 'Tonnes' measure and calculate total for each commodity
    tonnes_commodities = []
    for commodity in df_commodity[df_commodity['Measure'] == 'Tonnes']['Commodity']:
        tonnes_commodity = df_commodity[(df_commodity['Commodity'] == commodity) & (df_commodity['Measure'] == 'Tonnes')]['Value'].sum()
        tonnes_commodities.append(tonnes_commodity)

    print("\n----------------Commodities and Tonnes----------------\n")
    # Print the tonnes amounts for each commodity
    for commodity, tonnes_commodity in zip(df_commodity[df_commodity['Measure'] == 'Tonnes']['Commodity'], tonnes_commodities):
        print(f'{commodity} = {tonnes_commodity}\n')


    plt.bar(df_commodity[df_commodity['Measure'] == '$']['Commodity'], dollar_commodities)
    plt.xlabel('Commodity')
    plt.ylabel('Dollars')
    plt.title('Total Trade Value in Dollars by Commodity')

     #Make x axis look smaller to fit
    plt.xticks(fontsize=6, rotation=0)

    # Add label to the top of the graph
    plt.text(0.97, 1.05, 'Dollars per Commodity', ha='center', va='center', transform=plt.gca().transAxes,
             bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))

    plt.show()

    plt.bar(df_commodity[df_commodity['Measure'] == 'Tonnes']['Commodity'], tonnes_commodities)
    plt.xlabel('Commodity')
    plt.ylabel('Tonnes')
    plt.title('Total Trade Value in Tonnes by Commodity')

     #Make x axis look smaller to fit
    plt.xticks(fontsize=7, rotation=0)

    # Add label to the top of the graph
    plt.text(0.97, 1.05, 'Tonnes per Commodity', ha='center', va='center', transform=plt.gca().transAxes,
             bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))

    plt.show()
    
def case_6():

    # Extract month from 'Date' column
    df['Month'] = pd.to_datetime(df['Date'], dayfirst=True).dt.month

    # Group by month and measure and sum 'Value'
    df_month = df.groupby(['Month', 'Measure'])['Value'].sum().reset_index()

    # Filter for '$' measure and calculate total for each month
    dollar_months = []
    for month in range(1, 13):
        dollar_month = df_month[(df_month['Month'] == month) & (df_month['Measure'] == '$')]['Value'].sum()
        dollar_months.append(dollar_month)

    # Print the top 5 months by dollar amount
    month_names = list(calendar.month_name)[1:]
    dollar_top5 = sorted(zip(dollar_months, month_names), reverse=True)[:5]
    print("\n----------------Top 5 Months by Dollars----------------\n")
    for dollar_month, month_name in dollar_top5:
        print(f'{month_name} = {dollar_month}\n')

    # Filter for 'Tonnes' measure and calculate total for each month
    tonnes_months = []
    for month in range(1, 13):
        tonnes_month = df_month[(df_month['Month'] == month) & (df_month['Measure'] == 'Tonnes')]['Value'].sum()
        tonnes_months.append(tonnes_month)

    # Print the top 5 months by tonnes
    tonnes_top5 = sorted(zip(tonnes_months, month_names), reverse=True)[:5]
    print("\n----------------Top 5 Months by Tonnes----------------\n")
    for tonnes_month, month_name in tonnes_top5:
        print(f'{month_name} = {tonnes_month}\n')

    top5_dollar_months = [dollar_month for dollar_month, _ in dollar_top5]
    top5_month_names = [month_name for _, month_name in dollar_top5]

    plt.bar(top5_month_names, top5_dollar_months)
    plt.xlabel('Month')
    plt.ylabel('Dollars')
    plt.title('Total Trade Value in Dollars for Top 5 Months')

    plt.show()

    top5_tonnes_months = [tonnes_months for tonnes_months, _ in tonnes_top5]
    top5_month_names = [month_name for _, month_name in tonnes_top5]

    plt.bar(top5_month_names, top5_tonnes_months)
    plt.xlabel('Month')
    plt.ylabel('Tonnes')
    plt.title('Total Trade Value in Tonnes for Top 5 Months')

    plt.show()
def case_7():
            # Group by country commodity and measure and sum 'Value'
    df_country_commodity = df.groupby(['Country', 'Commodity', 'Measure'])['Value'].sum().reset_index()

    # Filter for '$' measure and calculate total for each country and commodity
    df_dollar = df_country_commodity[df_country_commodity['Measure'] == '$'].groupby(['Country', 'Commodity'])['Value'].sum().reset_index()
    df_dollar = df_dollar.sort_values(['Country', 'Value'], ascending=[True, False])
    df_dollar_top5 = df_dollar.groupby('Country').head(5)

    print("\n----------------Top 5 Commodities by Dollars----------------\n")
    # Print the top 5 commodities for each country based on their value in dollars
    for country in df_dollar_top5['Country'].unique():
        top5 = df_dollar_top5[df_dollar_top5['Country'] == country]
        print(f"{country}:")
        for i, row in top5.iterrows():
            print(f"{row['Commodity']} = {row['Value']}")
        print()

    # Filter for 'Tonnes' measure and calculate total for each country and commodity
    df_tonnes = df_country_commodity[df_country_commodity['Measure'] == 'Tonnes'].groupby(['Country', 'Commodity'])['Value'].sum().reset_index()
    df_tonnes = df_tonnes.sort_values(['Country', 'Value'], ascending=[True, False])
    df_tonnes_top5 = df_tonnes.groupby('Country').head(5)

    print("\n----------------Top 5 Commodities by Tonnes----------------\n")
    # Print the top 5 commodities for each country based on their value in tonnes
    for country in df_tonnes_top5['Country'].unique():
        top5 = df_tonnes_top5[df_tonnes_top5['Country'] == country]
        print(f"{country}:")
        for i, row in top5.iterrows():
            print(f"{row['Commodity']} = {row['Value']}")
        print()

  
        
def case_8():
        #Group by weekday, commodity, and measure and sum 'Value'
    df_weekday = df.groupby(['Weekday', 'Commodity', 'Measure'])['Value'].sum().reset_index()

    #Filter for '$' measure and find the weekday with the max value for each commodity
    print("\n----------------Max Dollar Weekdays by Commodity----------------\n")
    for commodity in df_weekday[df_weekday['Measure'] == '$']['Commodity'].unique():
        max_dollar_row = df_weekday[(df_weekday['Commodity'] == commodity) & (df_weekday['Measure'] == '$')].nlargest(1, 'Value')
        max_dollar_weekday = max_dollar_row['Weekday'].iloc[0]
        print(f'{commodity}: {max_dollar_weekday}')

    #Filter for 'Tonnes' measure and find the weekday with the max value for each commodity
    print("\n----------------Max Tonne Weekdays by Commodity----------------\n")
    for commodity in df_weekday[df_weekday['Measure'] == 'Tonnes']['Commodity'].unique():
        max_tonnes_row = df_weekday[(df_weekday['Commodity'] == commodity) & (df_weekday['Measure'] == 'Tonnes')].nlargest(1, 'Value')
        max_tonnes_weekday = max_tonnes_row['Weekday'].iloc[0]
        print(f'{commodity}: {max_tonnes_weekday}')


def exit_program():
    root.destroy()

# Creating the tkinter window
root = tk.Tk()

# Creating the text label
label = tk.Label(root, text="Choose your action:")

# Create the buttons
button1 = tk.Button(root, text="Overall turnover by month", command=case_1)
button2 = tk.Button(root, text="Overall turnover by country", command=case_2)
button3 = tk.Button(root, text="Overall turnover by transport", command=case_3)
button4 = tk.Button(root, text="Overall turnover by day", command=case_4)
button5 = tk.Button(root, text="Overall turnover by product", command=case_5)
button6 = tk.Button(root, text="Top 5 highest turnover by month", command=case_6)
button7 = tk.Button(root, text="Top 5 Commodities by country", command=case_7)
button8 = tk.Button(root, text="Top Commodity by day", command=case_8)

# Creating the exit button
exit_button = tk.Button(root, text="Exit", command=exit_program)

# we need to set the width of all the buttons to a desired width in order for them to fit
button_width = 25
button1.config(width=button_width)
button2.config(width=button_width)
button3.config(width=button_width)
button4.config(width=button_width)
button5.config(width=button_width)
button6.config(width=button_width)
button7.config(width=button_width)
button8.config(width=button_width)

# Add the buttons to the grid of our window
label.grid(row=0, column=0, columnspan=2, pady=10)
button1.grid(row=1, column=1, sticky="e", pady=5)
button2.grid(row=2, column=1, sticky="e", pady=5)
button3.grid(row=3, column=1, sticky="e", pady=5)
button4.grid(row=4, column=1, sticky="e", pady=5)
button5.grid(row=5, column=1, sticky="e", pady=5)
button6.grid(row=6, column=1, sticky="e", pady=5)
button7.grid(row=7, column=1, sticky="e", pady=5)
button8.grid(row=8, column=1, sticky="e", pady=5)
exit_button.grid(row=9, column=1, sticky="se", pady=10)

# Run the window
root.mainloop()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="python"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase;")
mycursor.execute("USE mydatabase;")


mycursor.execute("CREATE TABLE IF NOT EXISTS month_dollars (Month VARCHAR(255) NOT NULL,Value bigint(10) NOT NULL,PRIMARY KEY(Month));")
mycursor.execute("INSERT INTO month_dollars (Month, Value) VALUES ('January', 244882000000);")
mycursor.execute("INSERT INTO month_dollars (Month, Value) VALUES ('February', 244682000000);")                
mycursor.execute("INSERT INTO month_dollars (Month, Value) VALUES ('March', 278497000000);")
mycursor.execute("INSERT INTO month_dollars (Month, Value) VALUES ('April', 266910000000);")
mycursor.execute("INSERT INTO month_dollars (Month, Value) VALUES ('May', 284768000000);")
mycursor.execute("INSERT INTO month_dollars (Month, Value) VALUES ('June', 273339000000);")
mycursor.execute("INSERT INTO month_dollars (Month, Value) VALUES ('July', 280879000000);")
mycursor.execute("INSERT INTO month_dollars (Month, Value) VALUES ('August', 253427000000);")
mycursor.execute("INSERT INTO month_dollars (Month, Value) VALUES ('September', 259601000000);")
mycursor.execute("INSERT INTO month_dollars (Month, Value) VALUES ('October', 285419000000);")
mycursor.execute("INSERT INTO month_dollars (Month, Value) VALUES ('November', 293291000000);")
mycursor.execute("INSERT INTO month_dollars (Month, Value) VALUES ('December', 272102000000);")


mycursor.execute("CREATE TABLE IF NOT EXISTS month_tonnes (Month VARCHAR(255) NOT NULL,Value bigint(10) NOT NULL,PRIMARY KEY(Month));")
mycursor.execute("INSERT INTO month_tonnes (Month, Value) VALUES ('January', 20022000);")
mycursor.execute("INSERT INTO month_tonnes (Month, Value) VALUES ('February', 25850000);")
mycursor.execute("INSERT INTO month_tonnes (Month, Value) VALUES ('March', 28334000);")
mycursor.execute("INSERT INTO month_tonnes (Month, Value) VALUES ('April', 24862000);")
mycursor.execute("INSERT INTO month_tonnes (Month, Value) VALUES ('May', 26527000);")
mycursor.execute("INSERT INTO month_tonnes (Month, Value) VALUES ('June', 27495000);")
mycursor.execute("INSERT INTO month_tonnes (Month, Value) VALUES ('July', 28326000);")
mycursor.execute("INSERT INTO month_tonnes (Month, Value) VALUES ('August', 25285000);")
mycursor.execute("INSERT INTO month_tonnes (Month, Value) VALUES ('September', 24033000);")
mycursor.execute("INSERT INTO month_tonnes (Month, Value) VALUES ('October', 28009000);")
mycursor.execute("INSERT INTO month_tonnes (Month, Value) VALUES ('November', 28244000);")
mycursor.execute("INSERT INTO month_tonnes (Month, Value) VALUES ('December', 25410000);")


mycursor.execute("CREATE TABLE IF NOT EXISTS country_dollars (Country VARCHAR(255) NOT NULL,Value bigint(10) NOT NULL,PRIMARY KEY(Country));")
mycursor.execute("INSERT INTO country_dollars (Country, Value) VALUES ('All', 2315204000000);")
mycursor.execute("INSERT INTO country_dollars (Country, Value) VALUES ('Australia', 107686000000);")
mycursor.execute("INSERT INTO country_dollars (Country, Value) VALUES ('China', 282650000000);")
mycursor.execute("INSERT INTO country_dollars (Country, Value) VALUES ('East Asia (excluding China)', 116556000000);")
mycursor.execute("INSERT INTO country_dollars (Country, Value) VALUES ('European Union (27)', 26644000000);")
mycursor.execute("INSERT INTO country_dollars (Country, Value) VALUES ('Japan', 23155000000);")
mycursor.execute("INSERT INTO country_dollars (Country, Value) VALUES ('Total (excluding China)', 291991000000);")
mycursor.execute("INSERT INTO country_dollars (Country, Value) VALUES ('United Kingdom', 21591000000);")
mycursor.execute("INSERT INTO country_dollars (Country, Value) VALUES ('United States', 52320000000);")

mycursor.execute("CREATE TABLE IF NOT EXISTS country_tonnes (Country VARCHAR(255) NOT NULL,Value bigint(10) NOT NULL,PRIMARY KEY(Country));")
mycursor.execute("INSERT INTO country_tonnes (Country, Value) VALUES ('All', 185349000);")
mycursor.execute("INSERT INTO country_tonnes (Country, Value) VALUES ('China', 119573000);")
mycursor.execute("INSERT INTO country_tonnes (Country, Value) VALUES ('East Asia (excluding China)', 6137000);")
mycursor.execute("INSERT INTO country_tonnes (Country, Value) VALUES ('United States', 1338000);")


mycursor.execute("CREATE TABLE IF NOT EXISTS transport_dollars (Transport VARCHAR(255) NOT NULL,Value bigint(10) NOT NULL,PRIMARY KEY(Transport));")
mycursor.execute("INSERT INTO transport_dollars (Transport, Value) VALUES ('Air', 132602000000);")
mycursor.execute("INSERT INTO transport_dollars (Transport, Value) VALUES ('All', 2436795000000);")
mycursor.execute("INSERT INTO transport_dollars (Transport, Value) VALUES ('Sea', 668400000000);")

mycursor.execute("CREATE TABLE IF NOT EXISTS transport_tonnes (Transport VARCHAR(255) NOT NULL,Value bigint(10) NOT NULL,PRIMARY KEY(Transport));")
mycursor.execute("INSERT INTO transport_tonnes (Transport, Value) VALUES ('All', 312397000);")


mycursor.execute("CREATE TABLE IF NOT EXISTS weekday_dollars (Weekday VARCHAR(255) NOT NULL,Value bigint(10) NOT NULL,PRIMARY KEY(Weekday));")
mycursor.execute("INSERT INTO weekday_dollars (Weekday, Value) VALUES ('Friday', 533090000000);")
mycursor.execute("INSERT INTO weekday_dollars (Weekday, Value) VALUES ('Monday', 566712000000);")
mycursor.execute("INSERT INTO weekday_dollars (Weekday, Value) VALUES ('Saturday', 258225000000);")
mycursor.execute("INSERT INTO weekday_dollars (Weekday, Value) VALUES ('Sunday', 309677000000);")
mycursor.execute("INSERT INTO weekday_dollars (Weekday, Value) VALUES ('Thursday', 532286000000);")
mycursor.execute("INSERT INTO weekday_dollars (Weekday, Value) VALUES ('Tuesday', 520469000000);")
mycursor.execute("INSERT INTO weekday_dollars (Weekday, Value) VALUES ('Wednesday', 517338000000);")

mycursor.execute("CREATE TABLE IF NOT EXISTS weekday_tonnes (Weekday VARCHAR(255) NOT NULL,Value bigint(10) NOT NULL,PRIMARY KEY(Weekday));")
mycursor.execute("INSERT INTO weekday_tonnes (Weekday, Value) VALUES ('Friday', 47760000);")
mycursor.execute("INSERT INTO weekday_tonnes (Weekday, Value) VALUES ('Monday', 48527000);")
mycursor.execute("INSERT INTO weekday_tonnes (Weekday, Value) VALUES ('Saturday', 42241000);")
mycursor.execute("INSERT INTO weekday_tonnes (Weekday, Value) VALUES ('Sunday', 43239000);")
mycursor.execute("INSERT INTO weekday_tonnes (Weekday, Value) VALUES ('Thursday', 43047000);")
mycursor.execute("INSERT INTO weekday_tonnes (Weekday, Value) VALUES ('Tuesday', 42585000);")
mycursor.execute("INSERT INTO weekday_tonnes (Weekday, Value) VALUES ('Wednesday', 44998000);")


mycursor.execute("CREATE TABLE IF NOT EXISTS product_dollars (Product VARCHAR(255) NOT NULL,Value bigint(10) NOT NULL,PRIMARY KEY(Product));")
mycursor.execute("INSERT INTO product_dollars (Product, Value) VALUES ('All', 2386667000000);")
mycursor.execute("INSERT INTO product_dollars (Product, Value) VALUES ('Electrical machinery and equip', 51554000000);")
mycursor.execute("INSERT INTO product_dollars (Product, Value) VALUES ('Fish, crustaceans, and molluscs', 15445000000);")
mycursor.execute("INSERT INTO product_dollars (Product, Value) VALUES ('Fruit', 22197000000);")
mycursor.execute("INSERT INTO product_dollars (Product, Value) VALUES ('Logs, wood, and wood articles', 50381000000);")
mycursor.execute("INSERT INTO product_dollars (Product, Value) VALUES ('Meat and edible offal', 78512000000);")
mycursor.execute("INSERT INTO product_dollars (Product, Value) VALUES ('Mechanical machinery and equip', 72603000000);")
mycursor.execute("INSERT INTO product_dollars (Product, Value) VALUES ('Milk powder, butter, and cheese', 157284000000);")
mycursor.execute("INSERT INTO product_dollars (Product, Value) VALUES ('Non-food manufactured goods', 403154000000);")

mycursor.execute("CREATE TABLE IF NOT EXISTS product_tonnes (Product VARCHAR(255) NOT NULL,Value bigint(10) NOT NULL,PRIMARY KEY(Product));")
mycursor.execute("INSERT INTO product_tonnes (Product, Value) VALUES ('Fish, crustaceans, and molluscs', 1832000);")
mycursor.execute("INSERT INTO product_tonnes (Product, Value) VALUES ('Logs, wood, and wood articles', 264402000);")
mycursor.execute("INSERT INTO product_tonnes (Product, Value) VALUES ('Meat and edible offal', 10372000);")
mycursor.execute("INSERT INTO product_tonnes (Product, Value) VALUES ('Milk powder, butter, and cheese', 35791000);")


mycursor.execute("CREATE TABLE IF NOT EXISTS top5months_dollars (Month VARCHAR(255) NOT NULL,Value bigint(10) NOT NULL,PRIMARY KEY(Month));")
mycursor.execute("INSERT INTO top5months_dollars (Month, Value) VALUES ('November', 293291000000);")
mycursor.execute("INSERT INTO top5months_dollars (Month, Value) VALUES ('October', 285419000000);")
mycursor.execute("INSERT INTO top5months_dollars (Month, Value) VALUES ('May', 284768000000);")
mycursor.execute("INSERT INTO top5months_dollars (Month, Value) VALUES ('July', 280879000000);")
mycursor.execute("INSERT INTO top5months_dollars (Month, Value) VALUES ('March', 278497000000);")

mycursor.execute("CREATE TABLE IF NOT EXISTS top5months_tonnes (Month VARCHAR(255) NOT NULL,Value bigint(10) NOT NULL,PRIMARY KEY(Month));")
mycursor.execute("INSERT INTO top5months_tonnes (Month, Value) VALUES ('March', 28334000);")
mycursor.execute("INSERT INTO top5months_tonnes (Month, Value) VALUES ('July', 28326000);")
mycursor.execute("INSERT INTO top5months_tonnes (Month, Value) VALUES ('November', 28244000);")
mycursor.execute("INSERT INTO top5months_tonnes (Month, Value) VALUES ('October', 28009000);")
mycursor.execute("INSERT INTO top5months_tonnes (Month, Value) VALUES ('June', 27495000);")
mydb.commit()

mycursor.execute("CREATE TABLE IF NOT EXISTS top5products_by_country_dollars (Product VARCHAR(255) NOT NULL,Value bigint(10),id INT NOT NULL AUTO_INCREMENT ,PRIMARY KEY(id));")
mycursor.execute("INSERT INTO top5products_by_country_dollars (Product, Value) VALUES ('All-countries', null);")
mycursor.execute("INSERT INTO top5products_by_country_dollars (Product, Value) VALUES ('All-1', 1603472000000);")
mycursor.execute("INSERT INTO top5products_by_country_dollars (Product, Value) VALUES ('Non-food manufactured goods', 403154000000);")
mycursor.execute("INSERT INTO top5products_by_country_dollars (Product, Value) VALUES ('Milk powder, butter, and cheese-1', 98757000000);")
mycursor.execute("INSERT INTO top5products_by_country_dollars (Product, Value) VALUES ('Mechanical machinery and equip', 57567000000);")
mycursor.execute("INSERT INTO top5products_by_country_dollars (Product, Value) VALUES ('Meat and edible offal-1', 51206000000);")
mycursor.execute("INSERT INTO top5products_by_country_dollars (Product, Value) VALUES ('Australia', null);")
mycursor.execute("INSERT INTO top5products_by_country_dollars (Product, Value) VALUES ('All-2', 107686000000);")
mycursor.execute("INSERT INTO top5products_by_country_dollars (Product, Value) VALUES ('China', null);")
mycursor.execute("INSERT INTO top5products_by_country_dollars (Product, Value) VALUES ('All-3', 182406000000);")
mycursor.execute("INSERT INTO top5products_by_country_dollars (Product, Value) VALUES ('Milk powder, butter, and cheese-2', 31216000000);")
mycursor.execute("INSERT INTO top5products_by_country_dollars (Product, Value) VALUES ('Logs, wood, and wood articles', 17993000000);")
mycursor.execute("INSERT INTO top5products_by_country_dollars (Product, Value) VALUES ('Electrical machinery and equip', 16478000000);")
mycursor.execute("INSERT INTO top5products_by_country_dollars (Product, Value) VALUES ('Meat and edible offal-2', 15463000000);")
mycursor.execute("INSERT INTO top5products_by_country_dollars (Product, Value) VALUES ('East Asia (excluding China)', null);")
mycursor.execute("INSERT INTO top5products_by_country_dollars (Product, Value) VALUES ('All-4', 89245000000);")
mycursor.execute("INSERT INTO top5products_by_country_dollars (Product, Value) VALUES ('Milk powder, butter, and cheese-3', 27311000000);")
mycursor.execute("INSERT INTO top5products_by_country_dollars (Product, Value) VALUES ('European Union (27)', null);")
mycursor.execute("INSERT INTO top5products_by_country_dollars (Product, Value) VALUES ('All-5', 26644000000);")
mycursor.execute("INSERT INTO top5products_by_country_dollars (Product, Value) VALUES ('Japan', null);")
mycursor.execute("INSERT INTO top5products_by_country_dollars (Product, Value) VALUES ('All-6', 23155000000);")
mycursor.execute("INSERT INTO top5products_by_country_dollars (Product, Value) VALUES ('Total (excluding China)', null);")
mycursor.execute("INSERT INTO top5products_by_country_dollars (Product, Value) VALUES ('All-7', 291991000000);")
mycursor.execute("INSERT INTO top5products_by_country_dollars (Product, Value) VALUES ('United Kingdom', null);")
mycursor.execute("INSERT INTO top5products_by_country_dollars (Product, Value) VALUES ('All-8', 21591000000);")
mycursor.execute("INSERT INTO top5products_by_country_dollars (Product, Value) VALUES ('United States', null);")
mycursor.execute("INSERT INTO top5products_by_country_dollars (Product, Value) VALUES ('All-9', 40477000000);")
mycursor.execute("INSERT INTO top5products_by_country_dollars (Product, Value) VALUES ('Meat and edible offal-3', 11843000000);")

mycursor.execute("CREATE TABLE IF NOT EXISTS top5products_by_country_tonnes (Product VARCHAR(255) NOT NULL,Value bigint(10),id INT NOT NULL AUTO_INCREMENT ,PRIMARY KEY(id));")
mycursor.execute("INSERT INTO top5products_by_country_tonnes (Product, Value) VALUES ('All-countries', null);")
mycursor.execute("INSERT INTO top5products_by_country_tonnes (Product, Value) VALUES ('Logs, wood, and wood articles-1', 154650000);")
mycursor.execute("INSERT INTO top5products_by_country_tonnes (Product, Value) VALUES ('Milk powder, butter, and cheese-1', 22118000);")
mycursor.execute("INSERT INTO top5products_by_country_tonnes (Product, Value) VALUES ('Meat and edible offal-1', 6749000);")
mycursor.execute("INSERT INTO top5products_by_country_tonnes (Product, Value) VALUES ('Fish, crustaceans, and molluscs', 1832000);")
mycursor.execute("INSERT INTO top5products_by_country_tonnes (Product, Value) VALUES ('China', null);")
mycursor.execute("INSERT INTO top5products_by_country_tonnes (Product, Value) VALUES ('Logs, wood, and wood articles-2', 109752000);")
mycursor.execute("INSERT INTO top5products_by_country_tonnes (Product, Value) VALUES ('Milk powder, butter, and cheese-2', 7536000);")
mycursor.execute("INSERT INTO top5products_by_country_tonnes (Product, Value) VALUES ('Meat and edible offal-2', 2285000);")
mycursor.execute("INSERT INTO top5products_by_country_tonnes (Product, Value) VALUES ('East Asia (excluding China)', null);")
mycursor.execute("INSERT INTO top5products_by_country_tonnes (Product, Value) VALUES ('Milk powder, butter, and cheese-3', 6137000);")
mycursor.execute("INSERT INTO top5products_by_country_tonnes (Product, Value) VALUES ('United States', null);")
mycursor.execute("INSERT INTO top5products_by_country_tonnes (Product, Value) VALUES ('Meat and edible offal-3', 1338000);")


mycursor.execute("CREATE TABLE IF NOT EXISTS top5products_by_day_dollars (Product VARCHAR(255) NOT NULL,Day VARCHAR(255) ,PRIMARY KEY(Product));")
mycursor.execute("INSERT INTO top5products_by_day_dollars (Product, Day) VALUES ('All', 'Monday');")
mycursor.execute("INSERT INTO top5products_by_day_dollars (Product, Day) VALUES ('Electrical machinery and equip', 'Thursday');")
mycursor.execute("INSERT INTO top5products_by_day_dollars (Product, Day) VALUES ('Fish, crustaceans, and molluscs', 'Thursday');")
mycursor.execute("INSERT INTO top5products_by_day_dollars (Product, Day) VALUES ('Fruit', 'Friday');")
mycursor.execute("INSERT INTO top5products_by_day_dollars (Product, Day) VALUES ('Logs, wood, and wood articles', 'Friday');")
mycursor.execute("INSERT INTO top5products_by_day_dollars (Product, Day) VALUES ('Meat and edible offal', 'Sunday');")
mycursor.execute("INSERT INTO top5products_by_day_dollars (Product, Day) VALUES ('Mechanical machinery and equip', 'Thursday');")
mycursor.execute("INSERT INTO top5products_by_day_dollars (Product, Day) VALUES ('Milk powder, butter, and cheese', 'Monday');")
mycursor.execute("INSERT INTO top5products_by_day_dollars (Product, Day) VALUES ('Non-food manufactured goods', 'Thursday');")

mycursor.execute("CREATE TABLE IF NOT EXISTS top5products_by_day_tonnes (Product VARCHAR(255) NOT NULL,Day VARCHAR(255) ,PRIMARY KEY(Product));")
mycursor.execute("INSERT INTO top5products_by_day_tonnes (Product, Day) VALUES ('Fish, crustaceans, and molluscs', 'Monday');")
mycursor.execute("INSERT INTO top5products_by_day_tonnes (Product, Day) VALUES ('Logs, wood, and wood articles', 'Friday');")
mycursor.execute("INSERT INTO top5products_by_day_tonnes (Product, Day) VALUES ('Meat and edible offal', 'Sunday');")
mycursor.execute("INSERT INTO top5products_by_day_tonnes (Product, Day) VALUES ('Milk powder, butter, and cheese', 'Monday');")


mydb.commit()


# Close the cursor and database connection
mycursor.close()
mydb.close()
print("tes")
