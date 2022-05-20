import pandas as pd
import bisect
import csv

# =================== process grid.csv =================== #
grid_df = pd.read_csv('grid.csv', encoding = 'utf-8')
grid_num = len(grid_df)

x_dic = {} # key = x_min, val = list of Id (each Id has x_min == key)
y_dic = {} # key = y_min, val = list of Id (each Id has y_min == key)
x_dic_keys = [] # list of x_min
y_dic_keys = [] # list of y_min

bottom_boundary = min(grid_df['y_min'])
top_boundary = max(grid_df['y_max'])
right_boundary = max(grid_df['x_max'])
left_boundary = min(grid_df['x_min'])

print('bottom = ', bottom_boundary)
print('top = ', top_boundary)
print('left = ', left_boundary)
print('right = ', right_boundary)

for i in range(grid_num):
    x = list(grid_df.loc[i])
    Id = x[0]
    x_min = x[1]
    y_min = x[3]
    if x_min in x_dic: x_dic[x_min].append(Id)
    else: x_dic[x_min] = [Id]
    if y_min in y_dic: y_dic[y_min].append(Id)
    else: y_dic[y_min] = [Id]   
 
x_dic_keys = list(x_dic.keys())
y_dic_keys = list(y_dic.keys())
x_dic_keys.sort()
y_dic_keys.sort()
# ==================== process data.csv ==================== #
r = [] # hold the data we want to write to data_grid.csv
df = pd.read_csv('data.csv', encoding = 'utf-8')
row_num = len(df)
for i in range(row_num):
    row = list(df.loc[i])
    x = row[1]
    y = row[2]
    if y <= top_boundary and y >= bottom_boundary and x <= right_boundary and x >= left_boundary:
        tmp1 = x_dic[x_dic_keys[bisect.bisect_left(x_dic_keys, x) - 1]]
        tmp2 = y_dic[y_dic_keys[bisect.bisect_left(y_dic_keys, y) - 1]]
        tmp2 = set(tmp2)
        for Id in tmp1:
            if Id in tmp2: 
                row = [Id] + row
                break
        r.append(row)
r.sort()
# ==================== processed_data.csv ==================== #
f = open('processed_data.csv', 'w', newline = '', encoding = 'BIG5')
writer = csv.writer(f)
for row in r: writer.writerow(row)
f.close()