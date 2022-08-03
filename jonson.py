import json

# data = '{"name":"gaurav","rollno.":22}'


#json.loads ye string  ko dictonary me change krta h
# pasrad = json.loads(data)
# print(pasrad["rollno."])



# there is json.load function is for any files details show by the key of data

with open("jsonfile.json","r") as f:
    i = json.load(f)
    for data in i:
        print(data)

#json.dumb
# data1 = {"name":"Gaurav","roll no.":56,"age":22,"cars":( "farrari","jaguar","randson","alto"),"clothes":["peeter england","cobe","denim"],"vergin":False}
# dta = json.dumps(data1) # it provide us javescript compatable object , this is change False in to false because in javascript small false is compatble for js .
# print(dta)
# # to ye hmne ek javascript compatable object dega to iska output abjavascript me bhi aram se chlrha h



# # what is sort_keys parameter in dumps ?
# x  = {"name":"gaurav",
#       "hobbies":["playing","learning","traveling"],
#       "childs":None,
#     "cars":("alto","jaguar","thar"),}
# sortedwith_indent = json.dumps(x,indent=2,sort_keys=True)
# unsorted = json.dumps(x)
# print("when sort_keys is on and indent is 2 yani space code k bich me 2 space ise ham kitne bhi de skte h l :",sortedwith_indent)
# print("when sort_keys is off:",unsorted)

import json

my_details = {"name":"gaurav",
              "Address":"najibabad",
              "Email":"gauravrajput2771@gmail.com",
              "job":"Python Developer","Vergin":True}
with open("gr.json","w") as file:

    json.dump(my_details,file,sort_keys=True)

