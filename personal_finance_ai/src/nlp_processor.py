# src/nlp_processor.py
from transformers import pipeline

class NLPProcessor:
    def __init__(self):
        self.sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

    def phan_tich_cam_xuc(self, cau_hoi):
        result = self.sentiment_analyzer(cau_hoi)[0]
        label = result["label"]
        score = result["score"]
        if label == "NEGATIVE" and score > 0.7:
            return "lo_lắng"
        elif label == "POSITIVE":
            return "vui_vẻ"
        return "bình_thường"

    def trich_xuat_giao_dich(self, cau_hoi):
        cau_hoi = cau_hoi.lower()
        so_tien = None
        mo_ta = None
        danh_muc = "Khác"

        for token in cau_hoi.split():
            if "k" in token:
                try:
                    so_tien = float(token.replace("k", "")) * 1000
                    break
                except:
                    continue

        if "ăn" in cau_hoi or "uống" in cau_hoi:
            danh_muc = "Ăn uống"
            mo_ta = "Ăn uống"
        elif "mua" in cau_hoi:
            danh_muc = "Mua sắm"
            if "giày" in cau_hoi:
                mo_ta = "Mua giày"
            else:
                mo_ta = "Mua sắm"
        else:
            mo_ta = cau_hoi

        return so_tien, mo_ta, danh_muc