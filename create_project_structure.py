# create_project_structure.py
import os

def create_project_structure():
    # Định nghĩa cấu trúc thư mục
    project_structure = {
        "personal_finance_ai": {
            "data": {
                "models": {
                    "regression_model.pkl": ""
                },
                "chi_tieu.csv": ""
            },
            "src": {
                "__init__.py": "",
                "data_manager.py": "",
                "nlp_processor.py": "",
                "predictor.py": "",
                "assistant.py": ""
            },
            "tests": {
                "__init__.py": "",
                "test_data_manager.py": "",
                "test_nlp_processor.py": "",
                "test_predictor.py": ""
            },
            "main.py": "",
            "requirements.txt": "pandas\nscikit-learn\ntransformers\ntorch\nnumpy\n",
            "README.md": "# Personal Finance AI\nMột AI quản lý tài chính cá nhân với khả năng phân tích cảm xúc và dự đoán chi tiêu.\n\n## Cài đặt\n1. Cài đặt Python 3.8+\n2. Cài đặt các thư viện: `pip install -r requirements.txt`\n\n## Cách chạy\nChạy file `main.py`: `python main.py`\n\n## Chức năng\n- Theo dõi và phân tích chi tiêu.\n- Phân tích cảm xúc từ câu hỏi.\n- Dự đoán chi tiêu tương lai.\n"
        }
    }

    def create_structure(base_path, structure):
        for name, content in structure.items():
            path = os.path.join(base_path, name)
            if isinstance(content, dict):
                # Tạo thư mục
                os.makedirs(path, exist_ok=True)
                create_structure(path, content)
            else:
                # Tạo file
                with open(path, "w", encoding="utf-8") as f:
                    f.write(content)

    # Tạo cấu trúc
    create_structure(".", project_structure)
    print("Cấu trúc thư mục đã được tạo thành công!")

if __name__ == "__main__":
    create_project_structure()