import requests
import pandas
import matplotlib


# read pandas dataframe from url

base_url = 'http://www.espn.com/nfl/history'
leaders_df = pandas.read_html(f"{base_url}/leaders", attrs={'class': 'tablehead'})[0]


winners_df = pandas.read_html(f"http://www.espn.com/nfl/superbowl/history/winners", attrs={'class': 'tablehead'})[0]


mvp_df = pandas.read_html("http://www.espn.com/nfl/superbowl/history/mvps", attrs={'class': 'tablehead'})[0]


print(leaders_df.head())
print(winners_df.head())
print(mvp_df.head())

# grab 4th column
# pandas drop first row of winners_df and change column names
# save winners_df to csv
winners_df.to_csv('winners_raw.csv', index=False)
winners_df = winners_df.iloc[1:]
winners_df.columns = winners_df.iloc[0]
winners_df = winners_df.iloc[1:]
print(winners_df.columns)
winners_df.to_csv('winners.csv', index=False)
print(winners_df.head())

sites_of_superbowl = winners_df['SITE'].unique()

print(sites_of_superbowl)
# for date column find the number of instances of Orange Bowl and plot it
# adjust all site to drop content in () and save to csv

winners_df_adjusted = winners_df.copy()
winners_df_adjusted['SITE'] = winners_df_adjusted['SITE'].str.replace(r'\(.*\)', '')
fig =  winners_df_adjusted.groupby('SITE').size().plot(kind='bar', figsize=(10, 18)).get_figure()
fig.savefig('winners.png')