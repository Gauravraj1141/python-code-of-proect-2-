import requests
# x = requests.get("https://financialmodelingprep.com/api/v3/actives")
# print(x.text)
# print(x.url)
# print(x.status_code)
# print(x.headers)
# # print(x.encoding)
url = "https://automobilevintagespa.000webhostapp.com/apiforlink.php?token=74wwnnrum9ltd7xkttks"
data = {"name":"Gaurv Rajput",
        "password":"12345@321",
        "name2":"rdx",
        "psw":"312@R",}

requests.post(url=url,data=data)
x = requests.get("https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg")
# print(x.content)
# print(x.text)
# print(x.ok) # if it is true so all server response is ok if this is false so problem in server
# print(x.headers) #all about the link type and modification data all etc.

# with open("rajput.png","wb") as f:
#     f.write(x.content)

payloads = {"name":"gaurav"}
r  = requests.post('https://app.usertesting.com/users/sign_in?_gl=1*18ghwrn*_ga*NDAxODIxOTA0LjE2NTg1NzA5Nzk.*_ga_CDNE05D5FW*MTY1ODU3MDk3OS4xLjEuMTY1ODU3MTA5Mi40Mg..',data=payloads)
print(r.content)




import requests
# x = requests.get("https://financialmodelingprep.com/api/v3/actives")
# print(x.text) # code of this url is shown in this
# print(x.url) # it shown full url
# print(x.status_code) # it is for check status like 200 for sucess our request sucessfully run and some status code details in the web
# print(x.headers)
# # print(x.encoding)
# print(x.content) # it is for what we post in the api and in this api's record show in this comment
url = "https://automobilevintagespa.000webhostapp.com/apiforlink.php?token=74wwnnrum9ltd7xkttks"
data = {"name":"Gaurv Rajput",
        "password":"12345@321",
        "name2":"rdx",
        "psw":"312@R",}

requests.post(url=url,data=data)