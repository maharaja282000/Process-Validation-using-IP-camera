import cv2 #10.74.15.2
import pyautogui as p
import snap7
from snap7.util import *
from snap7.types import *
client=snap7.client.Client()
cap = cv2.VideoCapture("rtsp://admin:rane@123@10.74.15.39/1")
print(bool(cap),"  Camera OK")
client.connect("10.74.15.2",0,1,102)
print(bool(client.get_connected),"PLC communication OK")
#cap = cv2.VideoCapture(1)
from skimage.metrics import structural_similarity as compare_ssim
import argparse
import imutils
import numpy as np
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
seq1=0
seq2=0
seq3=0
seq4=0   #blade
tp1=100
tp2=100
tp3=100
string="0"
count=0
tli=0
tapeuw=0######
#plc_tapepresence_variable=1
#bv5=plc_tapepresence_variable.to_bytes(2,"big")
#client.db_write(51,14,bv5)
import time
l=[]
cbar=0
model="RH"
while True:
    cjicon="New---shift"
    dummytime=time.time()
    realtime=time.ctime(dummytime)
    hour=realtime[11:13]
    mins=realtime[14:16]
    secs=realtime[17:19]
    if(hour=="06" and mins=="00" and secs=="00" and cbar==0):
        l.append(count)
        l.append(model)
        l.append(hour)
        l.append(realtime)
        import csv
        csvfile= open("Hour_report.csv",'a+',newline="")
        writer= csv.writer(csvfile)
        writer.writerow(l)
        writer.writerow(cjicon)
        l.clear()
        csvfile.close()
        #import smtplib as s
        #ob=s.SMTP("smtp.gmail.com",587)
        #ob.starttls()
        #ob.login("s.maharajan@ranegroup.com","henqoezfuxohsign")
        #print("login successful")
        #subject="Mini-me Bot message! - ATTENTION"
        #body="Z101 CAB output Folding Machine"
        #message="subject:{}\n\n{}".format(subject,body)
        #print(message)
        #loa=["s.maharaja282000@gmail.com","maharaja282000@outlook.com",]
        #ob.sendmail("s.maharajan@ranegroup.com",loa,message)
        #print("process completed")
        #ob.quit()
        cbar=1
    if(hour=="07" and mins=="00" and secs=="00" and cbar==0):
        l.append(count)
        l.append(model)
        l.append(hour)
        l.append(realtime)
        import csv
        csvfile= open("Hour_report.csv",'a+',newline="")
        writer= csv.writer(csvfile)
        writer.writerow(l)
        l.clear()
        csvfile.close()
        cbar=1
    if(hour=="08" and mins=="00" and secs=="00" and cbar==0):
        l.append(count)
        l.append(model)
        l.append(hour)
        l.append(realtime)
        import csv
        csvfile= open("Hour_report.csv",'a+',newline="")
        writer= csv.writer(csvfile)
        writer.writerow(l)
        l.clear()
        csvfile.close()
        cbar=1
    if(hour=="09" and mins=="00" and secs=="00" and cbar==0):
        l.append(count)
        l.append(model)
        l.append(hour)
        l.append(realtime)
        import csv
        csvfile= open("Hour_report.csv",'a+',newline="")
        writer= csv.writer(csvfile)
        writer.writerow(l)
        l.clear()
        csvfile.close()
        cbar=1
    if(hour=="10" and mins=="00" and secs=="00" and cbar==0):
        l.append(count)
        l.append(model)
        l.append(hour)
        l.append(realtime)
        import csv
        csvfile= open("Hour_report.csv",'a+',newline="")
        writer= csv.writer(csvfile)
        writer.writerow(l)
        l.clear()
        csvfile.close()
        cbar=1
    if(hour=="11" and mins=="00" and secs=="00" and cbar==0):
        l.append(count)
        l.append(model)
        l.append(hour)
        l.append(realtime)
        import csv
        csvfile= open("Hour_report.csv",'a+',newline="")
        writer= csv.writer(csvfile)
        writer.writerow(l)
        l.clear()
        csvfile.close()
        cbar=1
    if(hour=="12" and mins=="00" and secs=="00" and cbar==0):
        l.append(count)
        l.append(model)
        l.append(hour)
        l.append(realtime)
        import csv
        csvfile= open("Hour_report.csv",'a+',newline="")
        writer= csv.writer(csvfile)
        writer.writerow(l)
        l.clear()
        csvfile.close()
        cbar=1
    if(hour=="13" and mins=="00" and secs=="00" and cbar==0):
        l.append(count)
        l.append(model)
        l.append(hour)
        l.append(realtime)
        import csv
        csvfile= open("Hour_report.csv",'a+',newline="")
        writer= csv.writer(csvfile)
        writer.writerow(l)
        l.clear()
        csvfile.close()
        cbar=1
    if(hour=="14" and mins=="00" and secs=="00" and cbar==0):
        l.append(count)
        l.append(model)
        l.append(hour)
        l.append(realtime)
        import csv
        csvfile= open("Hour_report.csv",'a+',newline="")
        writer= csv.writer(csvfile)
        writer.writerow(l)
        l.clear()
        csvfile.close()
        cbar=1
    if(hour=="15" and mins=="00" and secs=="00" and cbar==0):
        l.append(count)
        l.append(model)
        l.append(hour)
        l.append(realtime)
        import csv
        csvfile= open("Hour_report.csv",'a+',newline="")
        writer= csv.writer(csvfile)
        writer.writerow(l)
        l.clear()
        csvfile.close()
        cbar=1
    if(hour=="16" and mins=="00" and secs=="00" and cbar==0):
        l.append(count)
        l.append(model)
        l.append(hour)
        l.append(realtime)
        import csv
        csvfile= open("Hour_report.csv",'a+',newline="")
        writer= csv.writer(csvfile)
        writer.writerow(l)
        l.clear()
        csvfile.close()
        cbar=1
    if(hour=="17" and mins=="00" and secs=="00" and cbar==0):
        l.append(count)
        l.append(model)
        l.append(hour)
        l.append(realtime)
        import csv
        csvfile= open("Hour_report.csv",'a+',newline="")
        writer= csv.writer(csvfile)
        writer.writerow(l)
        l.clear()
        csvfile.close()
        cbar=1
    if(hour=="18" and mins=="00" and secs=="00" and cbar==0):
        l.append(count)
        l.append(model)
        l.append(hour)
        l.append(realtime)
        import csv
        csvfile= open("Hour_report.csv",'a+',newline="")
        writer= csv.writer(csvfile)
        writer.writerow(l)
        writer.writerow(cjicon)
        l.clear()
        csvfile.close()
        #import smtplib as s
        #ob=s.SMTP("smtp.gmail.com",587)
        #ob.starttls()
        #ob.login("s.maharajan@ranegroup.com","henqoezfuxohsign")
        #print("login successful")
        #subject="PROBLEM MESSAGE(Auto-emailserver)!!! - ATTENTION"
        #body="Problem in machine.Address this and rectify the problem!"
        #message="subject:{}\n\n{}".format(subject,body)
        #print(message)
        #loa=["s.maharaja282000@gmail.com","maharaja282000@outlook.com",]
        #ob.sendmail("s.maharajan@ranegroup.com",loa,message)
        #print("process completed")
        #ob.quit()
        cbar=1
    if(hour=="19" and mins=="00" and secs=="00" and cbar==0):
        l.append(count)
        l.append(model)
        l.append(hour)
        l.append(realtime)
        import csv
        csvfile= open("Hour_report.csv",'a+',newline="")
        writer= csv.writer(csvfile)
        writer.writerow(l)
        l.clear()
        csvfile.close()
        cbar=1
    if(hour=="20" and mins=="00" and secs=="00" and cbar==0):
        l.append(count)
        l.append(model)
        l.append(hour)
        l.append(realtime)
        import csv
        csvfile= open("Hour_report.csv",'a+',newline="")
        writer= csv.writer(csvfile)
        writer.writerow(l)
        l.clear()
        csvfile.close()
        cbar=1
    if(hour=="21" and mins=="00" and secs=="00" and cbar==0):
        l.append(count)
        l.append(model)
        l.append(hour)
        l.append(realtime)
        import csv
        csvfile= open("Hour_report.csv",'a+',newline="")
        writer= csv.writer(csvfile)
        writer.writerow(l)
        l.clear()
        csvfile.close()
        cbar=1
        
    if(hour=="22" and mins=="00" and secs=="00" and cbar==0):
        l.append(count)
        l.append(model)
        l.append(hour)
        l.append(realtime)
        import csv
        csvfile= open("Hour_report.csv",'a+',newline="")
        writer= csv.writer(csvfile)
        writer.writerow(l)
        l.clear()
        csvfile.close()
        cbar=1
    if(hour=="23" and mins=="00" and secs=="00" and cbar==0):
        l.append(count)
        l.append(model)
        l.append(hour)
        l.append(realtime)
        import csv
        csvfile= open("Hour_report.csv",'a+',newline="")
        writer= csv.writer(csvfile)
        writer.writerow(l)
        l.clear()
        csvfile.close()
        cbar=1
    if(hour=="00" and mins=="00" and secs=="00" and cbar==0):
        l.append(count)
        l.append(model)
        l.append(hour)
        l.append(realtime)
        import csv
        csvfile= open("Hour_report.csv",'a+',newline="")
        writer= csv.writer(csvfile)
        writer.writerow(l)
        l.clear()
        csvfile.close()
        cbar=1
    else:
        pass
    #p.moveTo(100,101,0.001)
    tb=client.db_read(51,4,4)
    lc=client.db_read(51,0,3)
    #rb=client.db_read(51,16,16)
    servofeedback=client.db_read(51,2,2)
    lcv=(lc[1])
    sf=servofeedback[1]
    tbv=tb[1]
    #email=client.db_read(51,16,16)###################################################################################
    #emailv=email[1]
    #if(emailv==1):
        #import smtplib as s
        #ob=s.SMTP("smtp.gmail.com",587)
        #ob.starttls()
        #ob.login("s.maharajan@ranegroup.com","josaozubiwjkvpdd")
        #print("login successful")
        #subject="Mini-me Bot message! - ATTENTION"
        #body="Z101 CAB output Folding Machine --> AI Connection Error" ,"\n", "1.)Check Ethernet connectivity  2.)Check Z101 CAB OP30 machine Status  3.)Check if IP of the Camera-10.74.15.39 is active" 
        #message="subject:{}\n\n{}".format(subject,body)
        #print(message)
        #loa=["s.maharaja282000@gmail.com","maharaja282000@outlook.com",]
        #ob.sendmail("s.maharajan@ranegroup.com",loa,message)
        #print("process completed")
        #ob.quit()
    #else:
        #pass################################################################################################################
    #feedback controls:
    #gripper=client.db_read(51,6,8)
    #gripper_variable=gripper[1]
    #folding_cylinder_variable=gripper[3]
    #print(folding_cylinder_variable)
    #print(gripper_variable)
    #rbv=rb[1]
    #print(rbv)
    #print(tbv)
    #print(sf)
    #print(lcv)
    #if(rbv==1):#reset action
        #score1=-1
        #score2=-1
        #score3=-1
        #inside_rollblade= " "
        #blade_presence = " "
        #Downfold = " "
        #Stretch = " "
        #tape1rh=" "
        #tape2rh=" "
        #tape3rh=" "
        #cv2.putText(cf,"STATUS BAR  ",(121,294-50), 3, 1,(138,43,226), 2)
        #cv2.putText(cf,"Cushion loading : "+Stretch, (121,294), 2, 1,(0,165,255), 2)
        #cv2.putText(cf,"Blade-Presence : "+blade_presence, (121,294+50), 2, 1,(0,255,255), 2)
        #cv2.putText(cf,"Down-fold : "+Downfold, (121,294+100), 2, 1,(147,112,219), 2)
        #cv2.putText(cf,"Inside-rollblade : "+inside_rollblade, (121,294+150), 2, 1,(0,255,255), 2)
        #cv2.rectangle(cf, (85, 788), (403, 593), (0, 0, 0), -1)
        #cv2.putText(cf,"Tape 1 RH : "+tape1rh, (121,294+350), 2, 1,(255,255,0), 2)
        #cv2.putText(cf,"Tape 2 RH : "+tape2rh, (121,294+350+50), 2, 1,(0,255,255), 2)
        #cv2.putText(cf,"Tape 3 RH : "+tape3rh, (121,294+350+100), 2, 1,(185,255,0), 2)
        #plc_loading_variable=0
        #bv1=plc_loading_variable.to_bytes(2,"big")
        #client.db_write(51,6,bv1)
        #plc_bladepresence_variable=0
        #bv2=plc_bladepresence_variable.to_bytes(2,"big")
        #client.db_write(51,8,bv2)
        #plc_downfold_variable=0
        #bv3=plc_downfold_variable.to_bytes(2,"big")
        #client.db_write(51,10,bv3)
        #plc_insiderollblade_variable=0
        #bv4=plc_insiderollblade_variable.to_bytes(2,"big")
        #client.db_write(51,12,bv4)
        #plc_tapepresence_variable=0
        #bv5=plc_tapepresence_variable.to_bytes(2,"big")
        #client.db_write(51,14,bv5)#EOreset action
    all_set="WAITING..."
    _, frame = cap.read()
    cf=cv2.resize(frame,(1920,1080),fx=0,fy=0,interpolation=cv2.INTER_AREA)
    hsv_frame = cv2.cvtColor(cf, cv2.COLOR_BGR2HSV)
    height, width, _ = cf.shape
    #print(p.position())
    px1= 1131-25
    py1= 831-6-14
    px2= 1304
    py2=483
    px3= 1217-15-3-1
    py3= 755-10-30
    px4= 811-80
    py4= 936-20
    bbpx=811+30+2-65
    bbpy=936-20
    #tpx2=1212
    #tpy2=406-25
    #tpx3=1194+2
    #tpy3=288-25
    score1=-1
    score2=-1
    score3=-1
    score11=-5
    score22=-5
    score33=-5
    inside_rollblade= " "
    blade_presence = " "
    Downfold = " "
    Stretch = " "
    tape1rh=" "
    tape2rh=" "
    tape3rh=" "
    cv2.rectangle(cf, (101, 505), (522, 262), (0, 0, 0), -1)
    #cv2.rectangle(cf, (1454, 919), (1726+9, 751-4), (0, 0, 255), -1)###
    #cv2.putText(cf,"sequence NOK ", (1488,847), 2, 1,(255,255,255), 2)
    cv2.putText(cf,"STATUS BAR  ",(121,294-50), 3, 1,(138,43,226), 2)
    cv2.putText(cf,"Cushion loading : "+Stretch, (121,294), 2, 1,(0,165,255), 2)
    cv2.putText(cf,"Blade-Presence : "+blade_presence, (121,294+50), 2, 1,(0,255,255), 2)
    cv2.putText(cf,"Down-fold : "+Downfold, (121,294+100), 2, 1,(147,112,219), 2)
    cv2.putText(cf,"Inside-rollblade : "+inside_rollblade, (121,294+150), 2, 1,(0,255,255), 2)
    cv2.rectangle(cf, (85, 788), (403, 593), (0, 0, 0), -1)
    cv2.putText(cf,"Tape 1 RH : "+tape1rh, (121,294+350), 2, 1,(255,255,0), 2)
    cv2.putText(cf,"Tape 2 RH : "+tape2rh, (121,294+350+50), 2, 1,(0,255,255), 2)
    cv2.putText(cf,"Tape 3 RH : "+tape3rh, (121,294+350+100), 2, 1,(185,255,0), 2)
    #cv2.circle(cf, (px1, py1), 5, (0, 0, 255), 3)
    #cv2.circle(cf, (px2, py2), 5, (0, 0, 255), 3)
    #cv2.circle(cf, (px3, py3), 5, (0, 0, 255), 3)
    #cv2.circle(cf, (px4, py4), 5, (0, 0, 255), 3)
    #cv2.circle(cf, (bbpx, bbpy), 5, (0, 0, 255), 3)
    #cv2.circle(cf, (tpx1, tpy1), 2, (255, 0, 0), 2)
    #cv2.circle(cf, (tpx2, tpy2), 2, (255, 0, 0), 2)
    #cv2.circle(cf, (tpx3, tpy3), 2, (255, 0, 0), 2)
    #cv2.rectangle(cf, (82, 514), (445, 235), (255, 255, 255), -1)
    #cv2.rectangle(cf, (px1, py1), (px11, py11), (0, 0, 255), -1)
    #cv2.rectangle(cf, (1223, 767), (1280, 668), (0, 0, 255), 1)#for blade
    #cv2.rectangle(cf, (1296, 541), (1411, 366), (0, 0, 255), 1)#for downfold
        #cv2.rectangle(frame, (18,613), (267,465), (0, 0, 0), -1)
        #cv2.putText(frame,"4", (994, 289), 2, 1,(0,0,0), 1)
        #cv2.putText(frame,"3", (845, 289), 2, 1,(0,0,0), 1)
        #cv2.putText(frame,"2", (462, 289), 2, 1,(0,0,0), 1)
        #cv2.putText(frame,"1", (182, 289), 2, 1,(0,0,0), 1)
    pixel_c1 = hsv_frame[py1, px1]
    pixel_c2 = hsv_frame[py2, px2]
    pixel_c3 = hsv_frame[py3, px3]
    pixel_c4 = hsv_frame[py4, px4]
    pixel_c5 = hsv_frame[bbpy,bbpx]
    #pixel_tape1= hsv_frame[tpy1, tpx1]
    #pixel_tape2=hsv_frame[tpy2, tpx2]
    #pixel_tape3=hsv_frame[tpy3,tpx3]
    #print(pixel_c1)
    #print(pixel_c3)
    #print(pixel_c2)
    #print(pixel_c4)
    #print(pixel_c5)
    #print( pixel_tape1)
    #print( pixel_tape2)
    #print( pixel_tape3)
    
    

        #hues
    hue_value1 = pixel_c1[0]
    hue_value2 = pixel_c2[0]
    hue_value3 = pixel_c3[0]
    hue_value4 = pixel_c4[0]
    hue_value5 = pixel_c5[0]
    
    #hue_tp1 = pixel_tape1[0]
    #hue_tp2 = pixel_tape2[0]

        #saturations
    sat_value1=pixel_c1[1]
    sat_value2=pixel_c2[1]
    sat_value3=pixel_c3[1]
    sat_value4=pixel_c4[1]
    sat_value5=pixel_c5[1]
    #sat_tp1 = pixel_tape1[1]
    #sat_tp2 = pixel_tape2[1]

        #vibrance
    vib_value1=pixel_c1[2]
    vib_value2=pixel_c2[2]
    vib_value3=pixel_c3[2]
    vib_value4=pixel_c4[2]
    vib_value5=pixel_c5[2]
    #vib_tp1=pixel_tape1[2]
    #vib_tp2=pixel_tape2[2]

    if(lcv==1 and sf==0):
            if ((hue_value1>=160 and hue_value1<=185)or(hue_value1>=0 and hue_value1<=20)):
                #if(sat_value1>=9):
                if(vib_value1>=180 and vib_value1<=240):
                    stretch="OK"
                    seq1=1
                    cv2.circle(cf, (px1, py1), 5, (0,255,0), 3)
                    #cv2.rectangle(cf, (px1, py1), (px11, py11), (0, 255, 0), -1)
                
    if(lcv==1):   
        if(hue_value3>=25 and hue_value3<=40):
        #if(sat_value3>=120):
            if(vib_value3>=100 and vib_value3<=260 ):
                if(seq1==1):
                    seq4=1
                    blade_presence="OK"
                    cv2.circle(cf, (px3, py3), 5, (0,255,0), 3)
                    cv2.rectangle(cf, (1155, 779), (1215, 669), (255, 0, 0), 3)
                    cv2.putText(cf,"CP1: Blade present", (1200,767+50), 2, 0.7,(100,140,0), 2)
                    
    if(lcv==1):    
        if(hue_value2>=5 and hue_value2<=20):
        #if(sat_value2>=9):
            if(vib_value2>=150 and vib_value2<=280):
                if(seq1==1):
                    if(seq4==1):
                        seq2=1
                        Downfold="OK"
                        cv2.circle(cf, (px2, py2), 5, (0,255,0), 3)
                        cv2.rectangle(cf, (1276, 541), (1411, 366), (255, 0, 0), 3)
                        cv2.putText(cf,"CP2: Downfold", (1296,541+50), 2, 0.7,(100,140,0), 2)
    if(lcv==1):   
        if(((hue_value4>=3 and hue_value4<=20) or (hue_value1>=160 and hue_value1<=185))and (hue_value5>=80 and hue_value5<=120)) :
        #if(sat_value4>=9):
            if(vib_value4>=20 and vib_value4<=240):
                if(seq2==1):
                    seq3=1
                    inside_rollblade="OK"
                    cv2.circle(cf, (px4, py4), 5, (0,255,0), 3)
                    cv2.circle(cf, (bbpx, bbpy), 5, (0,255,0), 3)
                    #cv2.rectangle(cf, (754, 1004), (1015, 277), (255, 0, 0), 3)
                    cv2.putText(cf,"CP3: Inside rollblade", (984,553), 2, 0.7,(100,140,0), 2)
    if(seq1==1 and seq2==1 and seq3==1 and seq4==1):
        tli=1
    elif(seq1==0 and seq2==0 and seq3==0 and seq4==0):
        tli=-1
    else:
        tli=0
    if(lcv==1 and sf==1 and tbv==1 and tli==1):
        r1=(1198, 706, 19, 22) 
        r2=(1153, 397, 12, 16) 
        r3=(1119, 260, 12, 12) 
        print(r1,"tp1")
        print(r2,"tp2")
        print(r3,"tp3")
        imgtp1=cf[int(r1[1]):int(r1[1]+r1[3]),int(r1[0]):int(r1[0]+r1[2])]
        cv2.imwrite("testtp1.jpg",imgtp1)
        imgtp2=cf[int(r2[1]):int(r2[1]+r2[3]),int(r2[0]):int(r2[0]+r2[2])]
        cv2.imwrite("testtp2.jpg",imgtp2)
        imgtp3=cf[int(r3[1]):int(r3[1]+r3[3]),int(r3[0]):int(r3[0]+r3[2])]
        cv2.imwrite("testtp3.jpg",imgtp3)
        img1=cv2.imread("mastertp1.jpg")
        img2=cv2.imread("testtp1.jpg")
        gray1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
        gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
        score1,diff1=compare_ssim(gray1,gray2,full=True)
        diff1=(diff1*255).astype("uint8")
        print("SSIM:{}".format(score1))
        img3=cv2.imread("mastertp2.jpg")
        img4=cv2.imread("testtp2.jpg")
        gray3=cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
        gray4=cv2.cvtColor(img4,cv2.COLOR_BGR2GRAY)
        score2,diff2=compare_ssim(gray3,gray4,full=True)
        diff2=(diff2*255).astype("uint8")
        print("SSIM:{}".format(score2))
        img5=cv2.imread("mastertp3.jpg")
        img6=cv2.imread("testtp3.jpg")
        gray5=cv2.cvtColor(img5,cv2.COLOR_BGR2GRAY)
        gray6=cv2.cvtColor(img6,cv2.COLOR_BGR2GRAY)
        score3,diff3=compare_ssim(gray5,gray6,full=True)
        diff3=(diff3*255).astype("uint8")
        print("SSIM:{}".format(score3))
        ###################
        r4=(1229, 976, 18, 28) 
        r5=(1184, 577, 18, 16) 
        r6=(1141, 332, 11, 12) 
        print(r4,"tpuw1")
        print(r5,"tpuw2")
        print(r6,"tpuw3")
        imguwtp1=cf[int(r4[1]):int(r4[1]+r4[3]),int(r4[0]):int(r4[0]+r4[2])]
        cv2.imwrite("testuwtp1.jpg",imguwtp1)
        imguwtp2=cf[int(r5[1]):int(r5[1]+r5[3]),int(r5[0]):int(r5[0]+r5[2])]
        cv2.imwrite("testuwtp2.jpg",imguwtp2)
        imguwtp3=cf[int(r6[1]):int(r6[1]+r6[3]),int(r6[0]):int(r6[0]+r6[2])]
        cv2.imwrite("testuwtp3.jpg",imguwtp3)
        img11=cv2.imread("masterlhtp1.jpg")
        img22=cv2.imread("testuwtp1.jpg")
        gray11=cv2.cvtColor(img11,cv2.COLOR_BGR2GRAY)
        gray22=cv2.cvtColor(img22,cv2.COLOR_BGR2GRAY)
        score11,diff11=compare_ssim(gray11,gray22,full=True)
        diff11=(diff11*255).astype("uint8")
        print("SSIM:{}".format(score11))
        img33=cv2.imread("masterlhtp2.jpg")
        img44=cv2.imread("testuwtp2.jpg")
        gray33=cv2.cvtColor(img33,cv2.COLOR_BGR2GRAY)
        gray44=cv2.cvtColor(img44,cv2.COLOR_BGR2GRAY)
        score22,diff22=compare_ssim(gray33,gray44,full=True)
        diff22=(diff22*255).astype("uint8")
        print("SSIM:{}".format(score22))
        img55=cv2.imread("masterlhtp3.jpg")
        img66=cv2.imread("testuwtp3.jpg")
        gray55=cv2.cvtColor(img55,cv2.COLOR_BGR2GRAY)
        gray66=cv2.cvtColor(img66,cv2.COLOR_BGR2GRAY)
        score33,diff33=compare_ssim(gray55,gray66,full=True)
        diff33=(diff33*255).astype("uint8")
        print("SSIM:{}".format(score33))
    elif(lcv==1 and sf==1 and tbv==1 and tli==0):
        cv2.rectangle(cf, (1454, 919), (1726+9, 751-4), (0, 0, 255), -1)###
        cv2.putText(cf,"Sequence NOK ", (1488,847), 2, 1,(255,255,255), 2)
    elif(lcv==1 and sf==1 and tbv==1 and tli==-1):
        cv2.rectangle(cf, (1454, 919), (1726+9, 751-4), (0, 255, 0), -1)
        cv2.putText(cf,"   ALL OK", (1488,847-50), 2, 1,(255,255,255), 2)
        cv2.putText(cf,"   Homing", (1488,847), 2, 1,(255,255,255), 2)
    else:
        pass
            
    if(score1>=0.08):
        #print("tape1-------> OK")
        tape1rh="OK"
        tapev1=1
        if(tapev1==1):
            cv2.putText(cf,"Tape 1 RH : "+tape1rh, (121,294+350), 2, 1,(255,255,0), 2)
    elif(score1==-1):
        tape1rh=" "
        tapev1=100
        if(tapev1==100):
            cv2.putText(cf,"Tape 1 RH : "+tape1rh, (121,294+350), 2, 1,(255,255,0), 2)
    else:
        #print("tape1-------> NOK")
        tape1rh="NOK"
        tapev1=0
        if(tapev1==0):
            cv2.putText(cf,"Tape 1 RH : "+tape1rh, (121,294+350), 2, 1,(255,255,0), 2)
    if(score2>=0.06):
        #print("tape2-------> OK")
        tape2rh="OK"
        tapev2=1
        if(tapev2==1):
            cv2.putText(cf,"Tape 2 RH : "+tape2rh, (121,294+350+50), 2, 1,(0,255,255), 2)
    elif(score2==-1):
        tape2rh=" "
        tapev2=100
        if(tapev2==100):
            cv2.putText(cf,"Tape 2 RH : "+tape2rh, (121,294+350+50), 2, 1,(0,255,255), 2)  
    else:
        #print("tape2-------> NOK")
        tape2rh="NOK"
        tapev2=0
        if(tapev2==0):
            cv2.putText(cf,"Tape 2 RH : "+tape2rh, (121,294+350+50), 2, 1,(0,255,255), 2)
    if(score3>=0.1):
        #print("tape3-------> OK")
        tape3rh="OK"
        tapev3=1
        if(tapev3==1):
            cv2.putText(cf,"Tape 3 RH : "+tape3rh, (121,294+350+100), 2, 1,(185,255,0), 2)
    elif(score3==-1):
        tape3rh=" "
        tapev3=100
        if(tapev3==100):
            cv2.putText(cf,"Tape 3 RH : "+tape3rh, (121,294+350+100), 2, 1,(185,255,0), 2)  
    else:
        #print("tape3-------> NOK")
        tape3rh="NOK"
        tapev3=0
        if(tapev3==0):
            cv2.putText(cf,"Tape 3 RH : "+tape3rh, (121,294+350+100), 2, 1,(185,255,0), 2)
    if(score11>=0.18 or score22>=0.06 or score33>=0.08):
        cv2.rectangle(cf, (1454, 919), (1726+9, 751-4), (0, 0, 255), -1)###
        cv2.putText(cf,"LH tape", (1488,847-50), 2, 1,(255,255,255), 2)
        cv2.putText(cf,"Present!", (1488,847), 2, 1,(255,255,255), 2)
        tapeuw=1
    elif(score11==-5 and score22==-5 and score33==-5):
        pass
    else:
        tapeuw=0
          
    if(seq1==1):
        Stretch="OK"
        cv2.putText(cf,"Cushion loading : "+Stretch, (121,294), 2, 1,(0,165,255), 2)
        plc_loading_variable=1
        #bv1=plc_loading_variable.to_bytes(2,"big")
        #client.db_write(51,6,bv1) 
        
    if(seq1==1):
        if(seq4==1):
            blade_presence ="OK"
            cv2.putText(cf,"Blade-Presence : "+blade_presence, (121,294+50), 2, 1,(0,255,255), 2)
            plc_bladepresence_variable=1
            #bv2=plc_bladepresence_variable.to_bytes(2,"big")
            #client.db_write(51,8,bv2) 
    if(seq1==1):
        if(seq4==1):
            if(seq2==1):
                Downfold="OK"
                cv2.putText(cf,"Down-fold : "+Downfold, (121,294+100), 2, 1,(147,112,219), 2)
                plc_downfold_variable=1
                #bv3=plc_downfold_variable.to_bytes(2,"big")
                #client.db_write(51,10,bv3) 
    if(seq1==1):
        if(seq4==1):
            if(seq2==1):
                if(seq3==1):
                    inside_rollblade="OK"
                    cv2.putText(cf,"Inside-rollblade : "+inside_rollblade, (121,294+150), 2, 1,(0,255,255), 2)
                    plc_insiderollblade_variable=1
                    #bv4=plc_insiderollblade_variable.to_bytes(2,"big")
                    #client.db_write(51,12,bv4)
    #if(tapev1==1 and tapev2==1 and tapev3==1):  #18.07.22 plc communication
            #plc_tapepresence_variable=1
            #bv5=plc_tapepresence_variable.to_bytes(2,"big")
            #client.db_write(51,14,bv5)
            #tapev1=100
            #tapev2=100
            #tapev3=100
    #print("Cushion loading:",seq1)
    #print("blade presence:",seq4)
    #print("Downfold:",seq2)
    #print("Inside-rollblade:",seq3)
    if(seq1==1 and seq2==1 and seq3==1 and seq4==1 and sf==1):
        if(tapev1==1 and tapev2==1 and tapev3==1 and tapeuw==0):
            plc_tapepresence_variable=1
            bv5=plc_tapepresence_variable.to_bytes(2,"big")
            client.db_write(51,14,bv5)
            all_set="Process-OK"
            #cv2.putText(cf,"STATUS : "+all_set, (881,300+77), 2, 1,(0,0,255), 2)
            count=count+1
            #cv1=count.to_bytes(2,"big")
            #client.db_write(51,6,bv1)#count loaded
            string=str(count)
            time.sleep(0)
            seq1=0
            seq2=0
            seq3=0
            seq4=0
            tapev1=100
            tapev2=100
            tapev3=100
            cbar=0
            plc_loading_variable=0
            #bv1=plc_loading_variable.to_bytes(2,"big")
            #client.db_write(51,6,bv1)
            plc_bladepresence_variable=0
            #bv2=plc_bladepresence_variable.to_bytes(2,"big")
            #client.db_write(51,8,bv2)
            plc_downfold_variable=0
            #bv3=plc_downfold_variable.to_bytes(2,"big")
            #client.db_write(51,10,bv3)
            plc_insiderollblade_variable=0
            #bv4=plc_insiderollblade_variable.to_bytes(2,"big")
            #client.db_write(51,12,bv4)
            plc_tapepresence_variable=0
            #bv5=plc_tapepresence_variable.to_bytes(2,"big")
            #client.db_write(51,14,bv5)
    cv2.rectangle(cf, (754, 110), (1120, 47), (255, 255, 255), -1)
    cv2.putText(cf,"Z101- CAB Folding", (80+700, 35+55), 4,1,(255,0,255), 2)
    cv2.putText(cf,"OK-part : "+string, (121,294+200), 2, 1,(0,255,0), 2)
    cv2.imshow("Z101-Folding", cf)
    key = cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()





#rli1=100
#bv1=rli1.to_bytes(2,"big")
#client.db_write(62,2,bv1) 
