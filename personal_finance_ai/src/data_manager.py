# src/data_manager.py
import pandas as pd
from datetime import datetime

class DataManager:
    def __init__(self, file_path="data/chi_tieu.csv"):
        self.file_path = file_path
        self.giao_dich = self.load_data()

    def load_data(self):
        try:
            return pd.read_csv(self.file_path).to_dict("records")
        except FileNotFoundError:
            return []

    def save_data(self):
        df = pd.DataFrame(self.giao_dich)
        df.to_csv(self.file_path, index=False)

    def them_giao_dich(self, so_tien, mo_ta, danh_muc="Khác", ngay=None):
        if ngay is None:
            ngay = datetime.now().strftime("%Y-%m-%d")
        giao_dich_moi = {
            "Ngày": ngay,
            "Số tiền": so_tien,
            "Mô tả": mo_ta,
            "Danh mục": danh_muc
        }
        self.giao_dich.append(giao_dich_moi)
        self.save_data()
        return "Đã thêm giao dịch thành công!"