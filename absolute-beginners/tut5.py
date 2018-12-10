# Dictionary and its Functions.

# d1 = { }
# # print(type(d1))
# print(d1)

d2 = { "2017": "Maaya",
       "2016": "Naagin",
       "web-series": {"1":"Sacred Games", "2":"Mirzapur", "3":"GOT 7"}}
d2["2018"] = "Simba"
# print(d2["web-series"])
# print(d2)
# del d2 ['2018']
# print(d2)
# print(d2["2018"])
# d3 = d2.copy()
# del d3["2017"]
# print(d2)
# print(d2.copy())
# print(d2.get("2017"))

d2.update({"Rahul":"Linux Noob"})
# print(d2)
# print(d2.keys())
print(d2.items())
