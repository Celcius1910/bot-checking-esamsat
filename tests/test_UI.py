import pytest
from pages import HomePage_PKB_JKT
import allure
from faker import Faker
import openpyxl
import pandas as pd
from datetime import datetime
import os

def read_excel_data(path):
    wb = openpyxl.load_workbook(path)
    sheet = wb.active
    data = []

    for row in sheet.iter_rows(min_row=2, values_only=True):
        first = row[0]
        middle = str(row[1])
        last = row[2]
        domicile = row[3]
        data.append((first, middle, last, domicile))  # simpan tuple
    return data

@allure.feature("Input vehicle identity")
@allure.story("Input test data")
@pytest.mark.parametrize("first, middle, last, domicile", read_excel_data("./data-test/test-data.xlsx"))
def test_search_vehicle_identity(page, first, middle, last, domicile):
    homepage_pkb_jkt = HomePage_PKB_JKT(page)
    if domicile == "jkt":
        homepage_pkb_jkt.load(domicile) 
        homepage_pkb_jkt.fill_nopol(middle)
        homepage_pkb_jkt.fill_noph(last)
        homepage_pkb_jkt.click_find()
        homepage_pkb_jkt.get_vehicle_identity()
        now = datetime.now()
        formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
        os.makedirs("data-test-result", exist_ok=True)
        df = pd.DataFrame([homepage_pkb_jkt.vehicle_identity()])
        print(df.head())
        df.to_excel(f"data-test-result/{formatted_date}-{first} {middle} {last}.xlsx", index=False)
        
    
        


