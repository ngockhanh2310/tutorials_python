import json

employees = {
    "E001": {"name": "Alice Smith", "position": "Software Engineer", "department": ["Development"]},
    "E002": {"name": "Bob Johnson", "position": "Data Analyst", "department": ["Analytics", "Research"]},
    "E003": {"name": "Charlie Lee", "position": "Project Manager", "department": ["Management"]},
    "E004": {"name": "Diana King", "position": "UX Designer", "department": ["Design"]}
}

print(employees["E001"]["name"])
print(employees["E002"]["department"][1])
employees["E005"] = {"name": "Ethan Brown", "position": "DevOps Engineer",
                     "department": ["Operations"]}  # Thêm nhân viên mới
employees["E003"]["department"].append("Client Relations")  # Cập nhật phòng ban cho nhân viên E003

print(json.dumps(employees, indent=4))
