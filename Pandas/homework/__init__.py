
import pandas as pd

# 准备动作
house_data = pd.read_csv("data/LJdata.csv")
# print(house_data)

# 0. 修改列名为英文名
house_data.columns = ['district', 'address', 'title', 'house_type', 'area', 'price', 'floor', 'build_time', 'direction', 'update_time', 'view_num', 'extra_info', 'link']
print(house_data)

# 1. 查看数据前5行
print(house_data.head(5))

# 2. 查看列数据分布
print(house_data.describe(include='all'))

# 3. 查看列统计指标
print(house_data.describe())

# 4. 查看数据形状
print(house_data.shape)


# 具体的需求
# 1. 找到租金最低，和租金最高的房子
print(house_data['price'].max())
print(house_data['price'].idxmax())
print(house_data.loc[house_data['price'].idxmax()])

print(house_data['price'].min())
print(house_data['price'].idxmin())
print(house_data.loc[house_data['price'].idxmin()])

# 2. 找到最近新上的10套房源
house_data.sort_values(by='update_time', ascending=False, inplace=True)
print(house_data[['update_time', 'price']].head(10))


# 3. 查看所有更新时间
print(house_data['update_time'])

# 4. 查看看房人数的平均值, 最大值, 最小值
print(house_data['view_num'].max())
print(house_data['view_num'].min())
print(house_data['view_num'].mean())

# 5. 查看不同看房人数的房源数量，as_index = False 分组字段不作为行索引（默认为True)
# print(house_data.groupby('view_num', as_index=False).get_group('view_num'))
view_num_group =  house_data.groupby('view_num', as_index=False)
print(view_num_group.size())

# 6. 查看房租价格的分布, 例如: 平均值, 标准差, 中位数...
print(house_data.describe())

print("-----")
# 7. 找到看房人数最多的朝向
print(house_data.groupby('direction', as_index=False).agg({
    'view_num': 'sum'
}).sort_values(by='view_num', ascending=False).head(1))


# 8. 查找最受欢迎的房型
print(house_data.groupby('house_type', as_index=False).agg({
    'view_num': 'sum'
}).sort_values(by='view_num', ascending=False).head(1))

# 9. 查找房子的平均租房价格 （元/平米）
house_data['price_per_sqm'] = house_data['price'] / house_data['area']
print(house_data['price_per_sqm'].mean())

# 10. 找到出租房源最多的小区
print(house_data.groupby('address', as_index=False).size().sort_values(by='size', ascending=False).head(1))



