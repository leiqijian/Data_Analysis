import pandas as pd

def handle_data(header, year = '2018'):
    # 1. load data
    sales_data = pd.read_excel("data/sales.xlsx", sheet_name = year)

    sales_data.columns = ["UserId", "OrderId", "OrderDate", "Amount"]

    sales_data.set_index("UserId", inplace = True)

    # print(sales_data[sales_data["Amount"] > 1])
    # filter na data
    drop_na_sales_data = sales_data[sales_data["Amount"] > 1].dropna()

    # 2. calculate R M F value
    # R
    dead_line = pd.to_datetime(f'{year}-12-31')
    user_last_date = drop_na_sales_data["OrderDate"].groupby(drop_na_sales_data.index).max()
    r_value = (dead_line - user_last_date).dt.days

    # M
    m_value = drop_na_sales_data["Amount"].groupby(drop_na_sales_data.index).sum()

    # F
    f_value = drop_na_sales_data["OrderDate"].groupby(drop_na_sales_data.index).count()

    r_value = pd.cut(r_value, bins = 5 , labels = [5, 4, 3, 2, 1])

    m_value = pd.cut(m_value, bins = 5 , labels = [1, 2, 3, 4, 5])

    f_value = pd.cut(f_value, bins = 5 , labels = [1, 2, 3, 4, 5])
    # print(r_value, m_value, f_value)

    data_dict = {
        "r_value" : r_value,
        "m_value" : m_value,
        "f_value" : f_value
    }

    rfm_data = pd.DataFrame(data_dict, dtype = 'int32')
    # rfm_data = pd.DataFrame(data_dict)
    # print(rfm_data.describe())

    # calculate value
    rfm_modle = rfm_data["r_value"].astype("string") + rfm_data["m_value"].astype("string") + rfm_data["f_value"].astype("string")

    rfm_score = rfm_data["r_value"] * 0.2 + rfm_data["m_value"] * 0.6 + rfm_data["f_value"] * 0.2

    rfm_data["year"] = year
    rfm_data["rfm_score"] = rfm_score
    rfm_data["rfm_modle"] = rfm_modle

    rfm_data.to_csv("data/rfm_result.csv", header = header, index = True, mode = 'a', encoding = "utf-8")


if __name__ == '__main__':
    year_list = ["2018", "2015", "2016", "2017"]

    for index, year in enumerate(year_list):
        header = False
        if index == 0:
            header = True
        handle_data(header, year)