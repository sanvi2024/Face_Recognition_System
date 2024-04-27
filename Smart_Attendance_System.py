from datetime import datetime                             
import pyttsx3 as textSpeach                               
Def MarkAttendence(name):                                      
   with open(‘attendance.csv’,‘r+’) as f:                                                                       
         myDataList=f.readlines()                              
         nameList=[] 
         for line in myDataList: 
         entry=line.split(‘,’) 
          nameList.append(entry[0]) 
          
          If name not in nameList: 
            now=datetime.now() 
            timestr=now.strftime(‘%H : %M’) 
            f.writelines(f ’\n{name} , {timestr}’) 
            statement=str(‘Welcome to class’ + name) 
            engine.say(statement) 
            engine.runAndWait() 
MarkAttendance(name)





