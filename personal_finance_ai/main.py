# main.py
from src.assistant import Assistant

def main():
    assistant = Assistant()
    
    # Thêm dữ liệu ban đầu
    print(assistant.tro_ly_grok("Tôi vừa chi 200k ăn tối hôm nay"))
    print(assistant.tro_ly_grok("Trời ơi, mua đồ giày hết 299k mà không suy nghĩ gì hết! Tiền đâu mà năm nay qua cửa sổ nhanh thế, không tiết kiệm cho tương lai để chi chứ? Chi mua giày mà không mua thứ gì khác có ích hơn sao?"))

if __name__ == "__main__":
    main()