d1 = {"a":10, "b":20, "c":30, "d":40}
d2 = {"b":20, "c":30, "d":40}
d3 = {}

# keys
d1_keys = d1.keys
d2_keys = d2.keys

if len(d1) >= len(d2):
    for i in range (len(d1_keys)):
        if d2[d2_keys[i]] in d1:
            d3[d2_keys[i]] = d2_keys[i] + d1_keys[d2_keys[i]]
print(d3)