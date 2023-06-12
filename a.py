# url=open("/home/runner/work/telepot3/telepot3/ultralytics",mode='r')
# url=open("http://hanh0984426858.github.io/telepot3/ultralytics",mode='r')
# # url=open("hanh0984426858/home/runner/work/telepot3/telepot3/ultralytics",mode='r')
# url=open("/usr/bin/hanh0984426858/home/runner/work/telepot3/telepot3/ultralytics",mode='r')
# from url import YOLO
# from model import YOLO
# from ultralytics import YOLO
# import a,ab,ac,ad,ae,af,ag,ah,aj,ak,al,am,an,ao,ap,ar,mk,at,au,av,aw,ay,az,b,ba,bc,bd,be,bf,bg,bh,bi,bj,bk,bl,bm
# import bn,bo,bq,bp,br,bs,bt,bv,bu,bư,bx,by,bz,c,ca,cb,cd,ce,cf,cg,ch,ci,cj,ck,cl,cm,cn,cq,cr,cr,cs,ct,cu,cư,cv,cx,cy
# import cz,d,de,dq,dr,e,f,g,h,i,j,k,l,m,n,o,q,r,s,t,u,ư,v,w,x,y,z,kj
import cv2
# from telepot7.vc16 import cv2
import telepot
import numpy
from ultralytics import YOLO
model = YOLO("yolov8n.pt")
results = model("rtsp://admin:admin1234@192.168.1.15:554/cam/realmonitor?channel=1&subtype=0",stream=True,show=True)
def show_frame():
    cv2.rectangle(frame,(0,0),(800,500),(255,0,0),10)
    cv2.imshow("show",frame)
    cv2.waitKey(1)
for result,frame in results:
    show_frame()
    boxes=result[0].boxes
    for box in boxes.numpy():
        x=(box.xyxy[0][0]+box.xyxy[0][2])/2
        y=int(box.xyxy[0][1])+int(box.xyxy[0][3])/2
        b=(0,0)[0]<x<(800,500)[0] and (0,0)[1]<y<(800,500)[1]
        if b:
            token = "6275415240:AAF3yDdT45-VIn8GdBrQUHH0XmtMXo0MC28"
            receiver_id=5877612764
            bot = telepot.Bot(token)
            bot.sendPhoto(receiver_id,photo=open("a121.jpg", "rb"),caption="Có xâm nhập, nguy hiêm!")
