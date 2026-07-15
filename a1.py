student_data = {
    "id1" : {"name": "Bhuwan", "class": "X", "subject_integration": "Maths, Science, English"},
    "id2" : {"name": "Krinjal", "class": "X", "subject_integration": "Maths, Science, English"},
    "id3" : {"name": "Pranit", "class": "X", "subject_integration": "Maths, Science, English"},
    "id4" : {"name": "Bhuwan", "class": "X", "subject_integration": "Maths, Science, English"},
    "id5" : {"name": "Krinjal", "class": "X", "subject_integration": "Maths, Science, English"},
    "id6" : {"name": "Pranit", "class": "X", "subject_integration": "Maths, Science, English"},
}

result = {}
seen_keys = []

for student_id, details in student_data.items():
    unique_key = (details["name"], details["class"], details["subject_integration"])
    
    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details

for k,v in result.items():
     print(k, ":", v)