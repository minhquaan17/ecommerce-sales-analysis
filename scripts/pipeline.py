import pandas as pd
import os

# lấy đường dẫn gốc project
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
raw_path = os.path.join(BASE_DIR, "data", "raw")
output_path = os.path.join(BASE_DIR, "data", "processed")

os.makedirs(output_path, exist_ok=True)  # tạo folder processed nếu chưa có

# đọc dữ liệu gốc
df = pd.read_csv(os.path.join(raw_path, "Amazon Sale Report.csv"), low_memory=False)

print("Raw shape:", df.shape)  # kiểm tra dữ liệu ban đầu


# CLEAN DATA
# chuẩn hóa tên cột (tránh lỗi do khoảng trắng / viết thường)
df.columns = df.columns.str.strip().str.upper()

# bỏ dòng không có amount (không có giá trị phân tích)
df = df.dropna(subset=['AMOUNT'])

# chuyển DATE sang datetime
df['DATE'] = pd.to_datetime(df['DATE'], errors='coerce')

# chuẩn hóa text
df['STATUS'] = df['STATUS'].astype(str).str.upper()  # chuẩn hóa status
df['CATEGORY'] = df['CATEGORY'].astype(str).str.upper().str.strip()  # chuẩn hóa category


# BUSINESS LOGIC
# phân loại đơn hàng (sales / cancel / other)
def map_order_type(x):
    if 'CANCEL' in x:
        return 'CANCEL'
    elif 'SHIP' in x:
        return 'SALES'
    else:
        return 'OTHER'

df['ORDER_TYPE'] = df['STATUS'].apply(map_order_type)

# doanh thu (AMOUNT đã là total → không nhân QTY)
df['REVENUE'] = df['AMOUNT']

# đơn CANCEL → revenue = 0 (tránh sai dashboard)
df.loc[df['ORDER_TYPE'] == 'CANCEL', 'REVENUE'] = 0

# FEATURE ENGINEERING
# tạo tháng và năm
df['MONTH'] = df['DATE'].dt.month
df['YEAR'] = df['DATE'].dt.year

# phân khúc đơn hàng (bao gồm cả cancel)
df['ORDER_SIZE'] = pd.cut(
    df['REVENUE'],
    bins=[-1, 0, 500, 1000, 2000, float('inf')],
    labels=['CANCEL', 'SMALL', 'MEDIUM', 'LARGE', 'VIP']
)

# REMOVE DUPLICATE
# loại bỏ trùng theo ORDER ID + SKU (chuẩn hơn drop toàn bộ)
df = df.drop_duplicates(subset=['ORDER ID', 'SKU'])

print("After clean:", df.shape)

# kiểm tra khoảng thời gian dataset
print("Date range:", df['DATE'].min(), "→", df['DATE'].max())

# VALIDATION (rất quan trọng khi demo)
print("\nOrder type distribution:")
print(df['ORDER_TYPE'].value_counts())

# SELECT COLUMN
columns_keep = [
    'ORDER ID',     # định danh đơn
    'DATE',         # thời gian
    'STATUS',       # trạng thái chi tiết
    'ORDER_TYPE',   # loại đơn
    'SKU',          # mã sản phẩm
    'CATEGORY',     # ngành hàng
    'QTY',          # số lượng
    'AMOUNT',       # giá trị đơn
    'REVENUE',      # doanh thu (đã xử lý đúng)
    'ORDER_SIZE',   # phân khúc đơn hàng
    'MONTH',        # tháng
    'YEAR'          # năm
]

df = df[[col for col in columns_keep if col in df.columns]]

print("Final shape:", df.shape)
print(df.head())

# ==============================
# SAVE FILE
# ==============================

df.to_csv(os.path.join(output_path, "all_orders.csv"), index=False)

print("DONE - saved at data/processed/all_orders.csv")