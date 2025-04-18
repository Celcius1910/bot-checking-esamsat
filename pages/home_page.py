from playwright.sync_api import Page
from playwright_stealth import stealth_sync
from utils.config import *
import allure
import pyautogui
import time


class HomePage_PKB_JKT:
    def __init__(self, page: Page):
        self.page = page
        
        # element-locator
        self.element_nopol = '[name="nopa"]'
        self.element_noph = '[name="noph"]'
        self.element_button_find = "#submit"
        
        # vehicle identity
        self.vehicle_identity = {
            "nopol": "",
            "kendaraan_ke": "",
            "nama": "",
            "nik": "",
            "alamat": "",
            "no_rangka_mesin": "",
            "no_bpkb": "",
            "merek_type": "",
            "model_pembuatan": "",
            "warna_kendaraan": "",
            "warna_tnkb": "",
            "bhn_bakar_cylinder": "",
            "masa_berlaku_stnk": "",
            "nilai_jual": "",
            "jatuh_tempo_pajak": "",
            "pkb_pokok": "",
            "swdkllj": "",
            "pkb_denda": "",
            "swdkllj_denda": "",
            "pnbp_cetak_stnk": "",
            "pnbp_plat_tnkb": "",
            "pnbp_nrkb_pilihan": "",
            "total": "",
            "status": ""
        }
        
    def load(self, domicile):
        with allure.step(title="Open browser"):
            if domicile == "jkt":
                stealth_sync(self.page)
                self.page.goto(pkb_jkt)
            else:
                 raise ValueError(f"Domicile '{domicile}' tidak dikenali")

    def maximize_browser(self):
        with allure.step(title="Maximize browser"):
            screen_width, screen_height = pyautogui.size()
            self.page.set_viewport_size(
                {"width": screen_width, "height": screen_height}
            )
    
    def fill_nopol(self, nopol: str):
        with allure.step(title="Fill Nopol field"):
            self.page.locator(self.element_nopol).fill(nopol)
    
    def fill_noph(self, noph: str):
        with allure.step(title="Fill Noph field"):
            self.page.locator(self.element_noph).fill(noph)
            
    def click_find(self):
        with allure.step(title="Click button 'Cari'"):
            self.page.locator(self.element_button_find).click("")

    def get_vehicle_identity(self):
        
        # row 1
        nopol_text = self.page.locator("div.row").nth(0).locator("div.col-sm-7").text_content()
        kendaraan_ke_text = self.page.locator("div.row").nth(0).locator("div.col").text_content()
        # row 2
        nama_text = self.page.locator("div.row").nth(1).locator("div.col-sm-7").text_content()
        nik_text = self.page.locator("div.row").nth(1).locator("div.col").text_content()
        # row 3
        alamat_text = self.page.locator("div.row").nth(2).locator("div.col-sm-7").text_content()
        # row 4
        no_rangka_mesin_text = self.page.locator("div.row").nth(3).locator("div.col-sm-7").text_content()
        no_bpkb_text = self.page.locator("div.row").nth(3).locator("div.col").text_content()
        # row 5
        merek_type_text = self.page.locator("div.row").nth(4).locator("div.col-sm-7").text_content()
        model_pembuatan_not_cleaned = self.page.locator("div.row").nth(4).locator("div.col").nth(0).all_inner_texts()
        model_pembuatan_cleaned_text = " ".join(t.strip().replace('\xa0', '') for t in model_pembuatan_not_cleaned)
        # row 6
        warna_kendaraan_text = self.page.locator("div.row").nth(5).locator("div.col-sm-7").text_content()
        warna_tnkb_text = self.page.locator("div.row").nth(5).locator("div.col").text_content()
        # row 7
        bhn_bakar_cylinder_text = self.page.locator("div.row").nth(6).locator("div.col-sm-7").text_content()
        masa_berlaku_stnk_text = self.page.locator("div.row").nth(6).locator("div.col").text_content()
        # row 8
        nilai_jual_text = self.page.locator("div.row").nth(7).locator("div.col-sm-7").text_content()
        jatuh_tempo_pajak_text = self.page.locator("div.row").nth(7).locator("div.col").text_content()
        # row 9
        pkb_pokok_text = self.page.locator("div.row").nth(8).locator("div.col-sm-7").text_content()
        swdkllj_text = self.page.locator("div.row").nth(8).locator("div.col").text_content()
        # row 10
        pkb_denda_text = self.page.locator("div.row").nth(9).locator("div.col-sm-7").text_content()
        swdkllj_denda_text = self.page.locator("div.row").nth(9).locator("div.col").text_content()
        # row 11
        pnbp_cetak_stnk_text = self.page.locator("div.row").nth(10).locator("div.col-sm-7").text_content()
        pnbp_plat_tnkb_text = self.page.locator("div.row").nth(10).locator("div.col").text_content()
        # row 12
        pnbp_nrkb_pilihan_text = self.page.locator("div.row").nth(11).locator("div.col-sm-7").text_content()
        total_text = self.page.locator("div.row").nth(11).locator("div.col").text_content()
        # row 13
        status_text = self.page.locator("div.row").nth(12).locator("div.col-sm-7").text_content()
        
        with allure.step(title="Get vehicle identity"):
            self.vehicle_identity["nopol"] = nopol_text
            self.vehicle_identity["kendaraan_ke"] = kendaraan_ke_text
            self.vehicle_identity["nama"] = nama_text
            self.vehicle_identity["nik"] = nik_text
            self.vehicle_identity["alamat"] = alamat_text
            self.vehicle_identity["no_rangka_mesin"] = no_rangka_mesin_text
            self.vehicle_identity["no_bpkb"] = no_bpkb_text
            self.vehicle_identity["merek_type"] = merek_type_text
            self.vehicle_identity["model_pembuatan"] = model_pembuatan_cleaned_text
            self.vehicle_identity["warna_kendaraan"] = warna_kendaraan_text
            self.vehicle_identity["warna_tnkb"] = warna_tnkb_text
            self.vehicle_identity["bhn_bakar_cylinder"] = bhn_bakar_cylinder_text
            self.vehicle_identity["masa_berlaku_stnk"] = masa_berlaku_stnk_text
            self.vehicle_identity["nilai_jual"] = nilai_jual_text
            self.vehicle_identity["jatuh_tempo_pajak"] = jatuh_tempo_pajak_text
            self.vehicle_identity["pkb_pokok"] = pkb_pokok_text
            self.vehicle_identity["swdkllj"] = swdkllj_text
            self.vehicle_identity["pkb_denda"] = pkb_denda_text
            self.vehicle_identity["swdkllj_denda"] = swdkllj_denda_text
            self.vehicle_identity["pnbp_cetak_stnk"] = pnbp_cetak_stnk_text
            self.vehicle_identity["pnbp_plat_tnkb"] = pnbp_plat_tnkb_text
            self.vehicle_identity["pnbp_nrkb_pilihan"] = pnbp_nrkb_pilihan_text
            self.vehicle_identity["total"] = total_text
            self.vehicle_identity["status"] = status_text
            return self.vehicle_identity
            
            