import pandas as pd
import re

def data_cleaning():
    df=pd.read_excel('commits.xlsx')


    # 将时间列（time）、日期列（date）和作者列（author）的类型改为字符串类型
    df['time'] = df['time'].astype(str)
    df['date'] = df['date'].astype(str)
    df['author'] = df['author'].astype(str)

    # 将作者列（author）中的所有值转换为小写，再按照作者进行升序排序，然后按照日期进行升序排序，最后按照时间进行升序排序
    df = df.sort_values(['author', 'date', 'time'], key=lambda x: x.astype(str).str.lower(),
                        ascending=[True, True, True])

    df.to_excel('update_commits.xlsx', index=False)
if __name__ == "__main__":
    data_cleaning()
