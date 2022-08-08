data = [{'date': '2022/10/05', 'jumlah': 1}, {'date': '2022/10/04', 'jumlah': 1}, {'date': '2022/10/03', 'jumlah': 10}, {'date': '2022/10/02', 'jumlah': 9}, {'date': '2022/10/01', 'jumlah': 9}]

# get terbanyak
newlist = sorted(data, key=lambda d: d['jumlah'],reverse=True)
terbanyak = newlist[0].get('date')
terendah = newlist[-1].get('date')

print(f'laporan terbanyak {terbanyak}')
# get min
print(f'laporan terendah {terendah}')

# get average
average =  sum(item['jumlah'] for item in data) / len(data) if data else [None]
print(average)