import json
import math

# File gốc
input_file = "E:/NLP_project/annotation/data_ner_copy.json"

# Số file muốn chia
num_files = 12

# Đọc file gốc
with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

total = len(data)
print(f"Tổng số câu trong file gốc: {total}")

# Số lượng câu mỗi file
per_file = math.ceil(total / num_files)
print(f"Mỗi file sẽ có khoảng {per_file} câu")

# Chia và lưu từng file
for i in range(num_files):
    start_idx = i * per_file
    end_idx = min(start_idx + per_file, total)
    chunk = data[start_idx:end_idx]

    output_file = f"data_ner_labels_part{i+1}.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(chunk, f, ensure_ascii=False, indent=2)

    print(f"Đã lưu {output_file} với {len(chunk)} câu")

print("\n✅ Chia file hoàn tất!")
