import geojson
import csv
import pandas as pd
import sys

sales = pd.read_csv('d3_dat.csv')
sales = sales.iloc[:,2:].set_index(sales['ZIP CODE'])

sales['median_unit'] = sales['median_unit'].fillna(0)
sales = sales.round(3)
s_dict = sales.to_dict('dict')


with open("data_raw.geojson", 'r+') as f:
	#with open("sales.json", 'r+') as g:
	data = geojson.load(f)

#number of neighbours in NY
for i in range(0, 262):
	postal = int(data['features'][i]['properties']['postalCode'])
	#print(postal)
	if ('cuisines' in data['features'][i]['properties']):
		c = s_dict['count'][postal]
		mid = s_dict['median_unit'][postal]
		a = s_dict['amount'][postal]
		#print(data['features'][0])

		data['features'][i]['properties']['count'] = c
		data['features'][i]['properties']['median_unit'] = mid
		data['features'][i]['properties']['amount'] = a
		
		del data['features'][i]['properties']['cuisines']
		print(data['features'][i])
with open('data_processed.geojson', 'w+') as f:
    geojson.dump(data, f)

		