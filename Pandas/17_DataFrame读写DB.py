'''
dataframe的db读写
    read_sql()
    to_sql()
'''
import pandas as pd
from sqlalchemy import create_engine
"""
    index_col：指定使用文件中哪个索引的字段作为DataFrame的索引
"""
df = pd.read_csv('data/csv示例文件.csv', sep=',', index_col=[0], encoding='gbk')

# print(df)

engine = create_engine('mysql+pymysql://root:Aa123456.@192.168.88.161:3306/db4?charset=utf8')

# sql 读取
sqlData = pd.read_sql('select * from students', engine)
print(sqlData)


#sql 写入 读出的数据的dataframe对象，调用to_sql方法写入db
"""
    参数解释：
        name：要写入的表名。如果不存在，自动创建
        con：connection，数据库连接
        if_exists：如果表或者数据已经存在的处理方式
            append：追加写
            replace：覆盖写
            fail：如果表存在，直接报错
"""
# df.to_sql(name="sql_test",con=engine,if_exists="replace",index=False)

# df.to_sql(name="sql_test",con=engine,if_exists="append",index=False)

df.to_sql(name="sql_test",con=engine,if_exists="fail",index=False)
