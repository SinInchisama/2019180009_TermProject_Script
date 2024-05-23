import requests
import xml.etree.ElementTree as ET
import tkinter

class Mountain:
    def __init__(self):
        print(1111)
        self.MoutainDict = dict()  # 산정보를 입력받음
        self.Danger_Dict = dict()  # 위험 데이터를 입력받음

        Url = 'http://apis.data.go.kr/B553662/top100FamtListBasiInfoService/getTop100FamtListBasiInfoList'
        Service_Key = '+DVZiTSkzywDM1jkG5NXm3oFTBHWY56Fs1tVGjhCd3GJU7FoZLrvIhGvPeX4JIENdU7G1X5+e98+ah0nvP8OMw=='
        params ={'serviceKey' : Service_Key,'pageNo' : '1','numOfRows' : '100', 'stdt' : '2024'}            # 100대 명산 파일 정보

        response = requests.get(Url, params=params)
        root = ET.fromstring(response.text)

        for item in root.iter("item"):
            frtrlNm = item.findtext("frtrlNm")
            ctpvNm = item.findtext("ctpvNm")
            addrNm = item.findtext("addrNm")
            lat = item.findtext("lat")
            lot = item.findtext("lot")
            aslAltide = item.findtext("aslAltide")

            self.MoutainDict[frtrlNm] = [ctpvNm,addrNm,lat,lot,aslAltide,[]]

        Url = 'http://apis.data.go.kr/B553662/trnspPoiInfoService/getTrnspPoiInfoList'      # 대중교통 xml

        for key,value in self.MoutainDict.items():
            params ={'serviceKey' : Service_Key,'pageNo' : '1','numOfRows' : '100', 'srchFrtrlNm' : key}
            response = requests.get(Url, params=params)
            root = ET.fromstring(response.text)

            for item in root.iter("item"):      # lat,lot,placeNum,dscrtCn      경도 위도 이름 특이사항
                List = list()
                List.append(item.findtext("lat"))
                List.append(item.findtext("lot"))
                List.append(item.findtext("placeNm"))
                List.append(item.findtext("dscrtCn"))
                value[5].append(List)


        Url = 'http://apis.data.go.kr/1400377/forestPoint/forestPointListSidoSearch'
        params ={'serviceKey' : Service_Key,'pageNo' : '1','numOfRows' : '100', 'excludeForecast' : '1'}
        response = requests.get(Url, params=params)
        root = ET.fromstring(response.text)

        for item in root.iter("item"):
            List = list()
            List.append(item.findtext("maxi"))
            List.append(item.findtext("meanavg"))
            List.append(item.findtext("mini"))
            self.Danger_Dict[item.findtext("doname")] = List
