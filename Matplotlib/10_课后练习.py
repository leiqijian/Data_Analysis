
# 使用附件中movie.csv数据集，进行以下计算（10分，每题一分）
#
# （1）按照导演进行分组，计算每位导演票房收入（gross列）总和
#
# （2）对上一步结果进行排序，求出票房前十的导演名称

import pandas as pd


def data_sum():
    movie_data = pd.read_csv("data/f54cfd9c94bb444695d90b89fa59c21b.csv")

    gross_sum = movie_data.groupby("director_name").agg({
        "gross": "sum",
    })
    print(gross_sum)

    print(gross_sum.sort_values(by = "gross", ascending=False).head(10).index)

if __name__ == '__main__':
    data_sum()