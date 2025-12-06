import polars

numbers_column = list(range(22))
numbers_column.remove(5)
numbers_column.remove(3)

table = polars.read_excel("lab5.xlsx", columns=numbers_column)
table = table.filter([False] * 2 + [True] * 12 + [False] * (len(table) - 14))

names_column = ["X", "Formula", "Value", "B", "15", "14", "13", "12", "11", "10", "9", "8", "7", "6",
                "5", "4", "3", "2", "1", "0"]

table.columns = names_column

with polars.Config(tbl_cols=-1, tbl_rows=-1, tbl_width_chars=-1):
    print(table)
