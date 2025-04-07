# src/predictor.py
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

class Predictor:
    def __init__(self, giao_dich):
        self.giao_dich = giao_dich

    def chuan_bi_du_lieu(self):
        df = pd.DataFrame(self.giao_dich)
        if len(df) < 2:
            return None, None
        
        df["Ngày"] = pd.to_datetime(df["Ngày"])
        ngay_dau = df["Ngày"].min()
        df["Ngày_số"] = (df["Ngày"] - ngay_dau).dt.days
        
        df_agg = df.groupby("Ngày_số")["Số tiền"].sum().reset_index()
        X = df_agg[["Ngày_số"]].values
        y = df_agg["Số tiền"].values
        return X, y

    def du_doan_chi_tieu(self, so_ngay_tuong_lai=7):
        X, y = self.chuan_bi_du_lieu()
        if X is None:
            return None, "Chưa đủ dữ liệu để dự đoán. Hãy thêm ít nhất 2 giao dịch!"

        model = LinearRegression()
        model.fit(X, y)
        
        ngay_cuoi = X[-1][0]
        ngay_du_doan = np.array([[ngay_cuoi + so_ngay_tuong_lai]])
        chi_du_doan = model.predict(ngay_du_doan)[0]
        return chi_du_doan, None