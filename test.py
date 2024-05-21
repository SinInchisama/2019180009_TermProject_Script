import requests
import xml.etree.ElementTree as ET
import tkinter

Url = 'http://apis.data.go.kr/B553662/top100FamtListBasiInfoService/getTop100FamtListBasiInfoList'
Service_Key = '+DVZiTSkzywDM1jkG5NXm3oFTBHWY56Fs1tVGjhCd3GJU7FoZLrvIhGvPeX4JIENdU7G1X5+e98+ah0nvP8OMw=='
params ={'serviceKey' : Service_Key,'pageNo' : '1','numOfRows' : '100', 'stdt' : '2024'}            # 100대 명산 파일 정보

response = requests.get(Url, params=params)
root = ET.fromstring(response.text)

header = ["frtrlNm", "ctpvNm", "addrNm", "lat","lot","aslAltide"]                                               # 산이름, 위치, 위치한 곳들, 경도, 위도, 고도

MoutainDict = dict()

for item in root.iter("item"):
    frtrlNm = item.findtext("frtrlNm")
    ctpvNm = item.findtext("ctpvNm")
    addrNm = item.findtext("addrNm")
    lat = item.findtext("lat")
    lot = item.findtext("lot")
    aslAltide = item.findtext("aslAltide")

    MoutainDict[frtrlNm] = [ctpvNm,addrNm,lat,lot,aslAltide]

Url = 'http://apis.data.go.kr/B553662/trnspPoiInfoService/getTrnspPoiInfoList'
for key,value in MoutainDict.items():
    params ={'serviceKey' : Service_Key,'pageNo' : '1','numOfRows' : '100', 'srchFrtrlNm' : key}
    response = requests.get(Url, params=params)
    root = ET.fromstring(response.text)

    for item in root.iter("item"):
        pass
        # lat,lot,placeNum,dscrtCn      경도 위도 이름 특이사항

Url = 'http://apis.data.go.kr/1400377/forestPoint/forestPointListGeongugSearch'
params ={'serviceKey' : Service_Key,'pageNo' : '1','numOfRows' : '100', 'excludeForecast' : '1'}


