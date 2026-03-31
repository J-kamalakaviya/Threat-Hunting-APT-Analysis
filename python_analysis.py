import pandas as pd

data = pd.read_csv("sample_logs.csv")
print(data.head())

failed = data[data['status'] == 'failed']
print(failed)

ip_counts = failed['ip'].value_counts()
print(ip_counts)
