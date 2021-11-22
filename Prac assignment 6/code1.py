d1 = {"a":10, "b":20, "c":30, "d":40}
d2 = {"b":20, "c":30, "d":40}
d3 = {}

# keys
d1_keys = d1.keys()
d2_keys = d2.keys()

for key in d1_keys & d2_keys:
    d3[key] = d1[key] + d2[key]

print(d3)