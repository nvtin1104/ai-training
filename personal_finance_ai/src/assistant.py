# src/assistant.py
from .data_manager import DataManager
from .nlp_processor import NLPProcessor
from .predictor import Predictor

class Assistant:
    def __init__(self):
        self.data_manager = DataManager()
        self.nlp_processor = NLPProcessor()
        self.predictor = Predictor(self.data_manager.giao_dich)
        self.cau_hinh = {
            "giong_dieu": "than_thien",
            "ngan_sach": 2000000,
            "ten_nguoi_dung": "Bạn"
        }

    def tro_ly_grok(self, cau_hoi=None):
        ten = self.cau_hinh["ten_nguoi_dung"]
        giong_dieu = self.cau_hinh["giong_dieu"]
        df = pd.DataFrame(self.data_manager.giao_dich)
        tong_chi = df["Số tiền"].sum() if not df.empty else 0
        ngan_sach = self.cau_hinh["ngan_sach"]

        if cau_hoi is None:
            if tong_chi == 0:
                return "Chưa có giao dịch nào cả. Bạn muốn tôi làm gì tiếp theo?"
            
            phan_tich = f"Tổng chi tiêu hiện tại: {tong_chi} VND.\n"
            if tong_chi > ngan_sach:
                phan_tich += f"Bạn đã vượt ngân sách {tong_chi - ngan_sach} VND rồi!"
            else:
                phan_tich += f"Bạn còn dư {ngan_sach - tong_chi} VND, tuyệt vời!"
            
            return f"Chào {ten}! {phan_tich} Có muốn tôi giúp gì thêm không?"

        cam_xuc = self.nlp_processor.phan_tich_cam_xuc(cau_hoi)
        so_tien, mo_ta, danh_muc = self.nlp_processor.trich_xuat_giao_dich(cau_hoi)
        if so_tien and ("chi" in cau_hoi.lower() or "mua" in cau_hoi.lower()):
            self.data_manager.them_giao_dich(so_tien, mo_ta, danh_muc)
            phan_hoi = f"Tôi đã thêm giao dịch: {so_tien} VND cho {danh_muc} ({mo_ta})."
        else:
            phan_hoi = ""

        if cam_xuc == "lo_lắng":
            tong_theo_danh_muc = df.groupby("Danh mục")["Số tiền"].sum().to_dict()
            danh_muc_max = max(tong_theo_danh_muc, key=tong_theo_danh_muc.get) if tong_theo_danh_muc else "chưa có"
            goi_y = f"Tôi thấy bạn chi nhiều cho {danh_muc_max} ({tong_theo_danh_muc.get(danh_muc_max, 0)} VND). Có thể thử giảm bớt và ưu tiên tiết kiệm hoặc mua thứ cần thiết hơn, như đồ dùng học tập. Đừng lo, tôi sẽ giúp bạn quản lý tốt hơn!"
            return f"Chào {ten}! Tôi hiểu bạn đang lo lắng. {phan_hoi} {goi_y} Cùng cố gắng nhé!"
        elif cam_xuc == "vui_vẻ":
            return f"Chào {ten}! Bạn đang vui nhỉ? {phan_hoi} Tiếp tục giữ tinh thần nhé, có cần tôi giúp gì không?"
        else:
            return f"Chào {ten}! {phan_hoi} Tôi có thể giúp gì thêm cho bạn?"