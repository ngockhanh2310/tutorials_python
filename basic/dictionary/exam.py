import json

lop_hoc = [
    {"ten": "Nam", "diem": 7.5},
    {"ten": "Lan", "diem": 9.0},
    {"ten": "Hung", "diem": 8.2}
]
lop_hoc.extend([
    {"ten": "Khanh", "diem": 9.5}
])


def tim_sinh_vien_gioi(ds):
    return [sv for sv in ds if sv["diem"] >= 8.0]


print(json.dumps(lop_hoc, indent=4))
for s_vien in tim_sinh_vien_gioi(lop_hoc):
    print(s_vien["ten"], " Đạt loại giỏi")
