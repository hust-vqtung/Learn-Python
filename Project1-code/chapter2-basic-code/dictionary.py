dict1 = {
    "name": "Vu Quang Tung",
    "age": 22,
    "gpa": 2.76
}
dict2 = {           #dictionary lồng nhau
    "id": 1,
    "info": dict1
}
print(dict1)
dict1["gpa"] = 4.0
print(dict1)
print(dict2)
print(dict2["info"]["age"])