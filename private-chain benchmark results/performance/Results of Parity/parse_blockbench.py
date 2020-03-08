import pandas as pd
import numpy as np
import re 
import csv
from io import StringIO

# parse blockbench output and transform to csv 


def convertToCSV(filenames, numNodes, csv=True):        
    csvOutput = []                
    if csv:
        csvOutput.append("nodes,pollIntervall,txCount,latency,avgLatency,queue")

    for filename in filenames:   
        #nodes = re.search('nodes(\d+)_', filename)
        #numNodes = nodes.group(1) if nodes else 2
        with open(filename) as f:
            for l in f:

                if "tx count" in l:
                    m = re.search('last (\d+)s, tx count = (\d+) latency = (\d+\.?\d*) outstanding request = (\d+)', l)
                    if m:
                        avgLatency = (float(m.group(3)) / float(m.group(2))) if m.group(2) != '0' else 0
                        line = [str(numNodes),m.group(1),m.group(2),m.group(3),str(avgLatency),m.group(4)]
                        if csv:
                            csvOutput.append(','.join(line))
                        else:
                            csvOutput.append([ float(x) for x in line ])
    return csvOutput                                           # ["nodes,pollIntervall,txCount,latency,avgLatency,queue","231,2312,1231,3123,2143"]

csvOut = convertToCSV(['./client_212.64.127.148','./client_115.159.112.46','./client_123.206.183.88','./client_123.206.176.177','./client_123.206.176.177','./client_123.206.183.180','./client_123.206.181.56','./client_123.206.176.245','./client_123.206.181.161','./client_123.206.181.14','./client_123.206.180.206'], 10, False)             # './ycsb_blockchainkv_exp/client_0_n1_nodes2_20180329',

with open('blockbench.csv', 'w') as csvfile:                                                     
    writer = csv.writer(csvfile, delimiter='\n')#,quoting=csv.QUOTE_ALL)
    writer.writerow(csvOut)

df = pd.read_csv('blockbench.csv')                                                                     

df = pd.DataFrame.from_records(csvOut, columns=['nodes','pollIntervall','txCount','latency','avgLatency','queue'])   

#df.loc[df['txCount'] != 0]                                                                                      
#print(df[df.txCount != 0])
#print(df)
#df.describe()                                                                                                       

#print(df.agg(['min', 'max', 'mean', 'sum', 'count']))

csvOut = convertToCSV(['./client_212.64.127.148','./client_115.159.112.46','./client_123.206.183.88','./client_123.206.176.177','./client_123.206.176.177','./client_123.206.183.180','./client_123.206.181.56','./client_123.206.176.245','./client_123.206.181.161','./client_123.206.181.14','./client_123.206.180.206'], 10, False)             # './ycsb_blockchainkv_exp/client_0_n1_nodes2_20180329',
with open('blockbench.csv', 'w') as csvfile:                                                   
    writer = csv.writer(csvfile, delimiter='\n')#,quoting=csv.QUOTE_ALL)
    writer.writerow(csvOut)

df = pd.read_csv('blockbench.csv')                                                                   
df = pd.DataFrame.from_records(csvOut, columns=['nodes','pollIntervall','txCount','latency','avgLatency','queue']) 
print(df.agg(['min', 'max', 'mean', 'sum', 'count']))

csvOut_overall = convertToCSV(['./client_212.64.127.148','./client_115.159.112.46','./client_123.206.183.88','./client_123.206.176.177','./client_123.206.176.177','./client_123.206.183.180','./client_123.206.181.56','./client_123.206.176.245','./client_123.206.181.161','./client_123.206.181.14','./client_123.206.180.206'], 10, False)
df_overall = pd.DataFrame.from_records(csvOut_overall, columns=['nodes','pollIntervall','txCount','latency','avgLatency','queue'])
df_overall.agg(['min', 'max', 'mean', 'sum', 'count'])


overall_txCount = df_overall['txCount'].sum()
overall_pollIntervall = df['pollIntervall'].sum()
print("Overall throughput was", overall_txCount, "/", overall_pollIntervall, "=", overall_txCount/overall_pollIntervall*5)
