from xml.dom.minidom import TypeInfo
import requests
import xml.etree.ElementTree as ET

url = "http://openapi.seoul.go.kr:8088/4e4a5476466a616e31303676484f4c42/xmlf/CardSubwayStatsNew/1/500/20220701"
response = requests.get(url)
result = response.content
#print(result)
#tree = ET.parse(result)
root = ET.fromstring(result) #xml 문자를 이용한 파싱 (문자열에서 직접)
#ET.dump(root)
#print(type(root))
#print(root.tag)

count = 6
station = "역 이름"
pssnger = 0
sr_list = [[],[]]

#i = 0
ST_array = []
array = []

#root == <CardSubwayStatsNew>
for child in root: #root 태그로 for 문 돌리면 자식 엘리먼트 전체가 추출
    #print(child.tag, child.attrib)
    #total_count가 0이면 데이터가 없으므로 break
    if child.tag == 'list_total_count':
        print("total_cnt:" + child.text)
        if child.text == '0':
            break
    #CODE가 INFO-000이 아니면 정상 처리된 것이 아니므로 break    
    elif child.tag == 'RESULT': 
        for gchild in child:
            if gchild.tag == 'CODE':
                print("code :" + gchild.text)
                if(gchild.text != 'INFO-000'):
                    break
                print("------------------------")
    #else:
    elif child.tag == 'row':
        for gchild in child:
            if gchild.tag == 'LINE_NUM':
                if gchild.text == '2호선':
                    print("line : " + gchild.text)
                else:
                    break
            elif gchild.tag == 'SUB_STA_NM':
                print("station : " + gchild.text)
                station = gchild.text
                #ST_array.append(gchild.text)
            elif gchild.tag == 'RIDE_PASGR_NUM':
                print("#_of_pssnger : " + gchild.text)
                pssnger = int(gchild.text)
                #array.append(int(gchild.text))
                print("------------------------")
                #maxValue = int(array[0])
                
        sr_list.append([pssnger, station])

#print(array)
#result_array = sorted(array)
#print(result_array)

re_sr_list = sorted(sr_list)
print(re_sr_list)

for i in range(count):
    if i == 0:
        continue
    print(str(i)+"번 째로 유동인구 많은 역 : "+str(re_sr_list[-i][1])+"역")
    print("유동 인구 수 : "+str(re_sr_list[-i][0])+"명")
    print("------------------------")
    
#print("배열 길이 : "+str(len(array)))
#print("배열 i번째 : "+array[10])
#print(type(maxValue))
#print(type(array))

#for i in range(1, len(array)):
   #if maxValue < int(array[i]):
       #maxValue = int(array[i])
       #maxstation = i

#print("최고 유동인구 수 : "+str(maxValue))
#print("최고 유동인구 수 역 : "+str(ST_array[maxstation]))

#for usedt in root.findall("USE_DT"):
#print("tt")