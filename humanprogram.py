import os       
import pyttsx3
x="0"
print("____________-_____________-___________||...........S U P R A B H A A T ...........||_________-_____________-____________")
print()
pyttsx3.speak("Suprabhaat")
print()
print("If You Like To Go With Menu Card       : press 1")
print("If You Like To Go With Your Own Choice : press 2")
print("If You Like To Close Our Program       : press 3")
print()
print("Type",end=":")
u=input()
while True:
 if(("not" in x) or ("cannot" in x) or ("exit" in x) or ("terminate " in x) or ("dont" in x) or ("did not" in x)):    
        print("Have A Nice Day")
        break
 elif("2" in u):
    while True:
     print("~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~W h a t    C a n    I    Do    For   You~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~~  ~")       
     print("")
     pyttsx3.speak("What Can I Do For. You.")
     print()
     print("N O T E :- If You Want To Terminate The program Type exit")
     print()
     print("Type Your Requirement ",end=":")
     x=input()
     pyttsx3.speak(x)
     if(("run" in x) or ("execute" in x) or ("open" in x) or ("chalu karo" in x) or ("chalukaro" in x) or ("perform" in x)) and (("notepad++" in x) or ("texteditor" in x)):
        os.system("notepad++")
     elif(("run" in x) or ("execute" in x) or ("open" in x) or ("chalu karo" in x) or ("chalukaro" in x) or ("perform" in x)) and (("zoomapp" in x) or ("zoom" in x)):
        os.system("zoom")
     elif(("run" in x) or ("execute" in x) or ("open" in x) or ("chalu karo" in x) or ("chalukaro" in x) or ("perform" in x))and (("chrome" in x)or("browser" in x)):
        print("which site you want to open in chrome browser",end=":")
        site=input()
        os.system("chrome www."+site+".com")
     elif(("run" in x) or ("execute" in x) or ("open" in x) or ("chalu karo" in x) or ("chalukaro" in x) or ("perform" in x)) and ("notepad" in x):
        os.system("notepad")
     elif(("run" in x) or ("execute" in x) or ("open" in x) or ("chalu karo" in x) or ("chalukaro" in x) or ("perform" in x)) and ("vlc" in x):
        os.system("vlc")
     elif (("run" in x) or ("execute" in x) or ("open" in x) or ("chalu karo" in x) or ("chalukaro" in x) or ("perform" in x)) and ("jupyter notebook" in x):
        os.system("jupyter notebook")
     elif (("run" in x) or ("execute" in x) or ("open" in x) or ("chalu karo" in x) or ("chalukaro" in x) or ("perform" in x)) and ("msedge" in x):
        print("which site you want to open in microsoft edge browser",end=":")
        site=input()
        os.system("msedge www."+site+".com")
     elif (("run" in x) or ("execute" in x) or ("open" in x) or ("chalu karo" in x) or ("chalukaro" in x) or ("perform" in x)) and ("teamviewer" in x):
        os.system("teamviewer")
     elif (("run" in x) or ("execute" in x) or ("open" in x) or ("chalu karo" in x) or ("chalukaro" in x) or ("perform" in x)) and ("steam" in x):
        os.system("steam")
     elif (("run" in x) or ("execute" in x) or ("open" in x) or ("chalu karo" in x) or ("chalukaro" in x) or ("perform" in x)) and ("wmplayer" in x):
        os.system("wmplayer")
     elif (("run" in x) or ("execute" in x) or ("open" in x) or ("chalu karo" in x) or ("chalukaro" in x) or ("perform" in x)) and ("safeexambrowser" in x):
        os.system("safeexambrowser")
     elif (("run" in x) or ("execute" in x) or ("open" in x) or ("chalu karo" in x) or ("chalukaro" in x) or ("perform" in x)) and ("powerpnt" in x):
        os.system("powerpnt")
     elif (("run" in x) or ("execute" in x) or ("open" in x) or ("chalu karo" in x) or ("chalukaro" in x) or ("perform" in x)) and ("excel" in x):
        os.system("excel")
     elif (("run" in x) or ("execute" in x) or ("open" in x) or ("chalu karo" in x) or ("chalukaro" in x) or ("perform" in x)) and ("msaccess" in x):
        os.system("msaccess")
     elif (("run" in x) or ("execute" in x) or ("open" in x) or ("chalu karo" in x) or ("chalukaro" in x) or ("perform" in x)) and ("outlook" in x):
        os.system("outlook")
     elif (("run" in x) or ("execute" in x) or ("open" in x) or ("chalu karo" in x) or ("chalukaro" in x) or ("perform" in x)) and ("rainmeter" in x):
        os.system("rainmeter")
     elif (("run" in x) or ("execute" in x) or ("open" in x) or ("chalu karo" in x) or ("chalukaro" in x) or ("perform" in x)) and ("control" in x):
        os.system("control")
     elif (("run" in x) or ("execute" in x) or ("open" in x) or ("chalu karo" in x) or ("chalukaro" in x) or ("perform" in x)) and ("winword" in x):
        os.system("winword")
     elif (("run" in x) or ("execute" in x) or ("open" in x) or ("chalu karo" in x) or ("chalukaro" in x) or ("perform" in x)) and ("startexplorer" in x):
        os.system("start explorer")
     elif (("make"in x) or ("create" in x) or ("mkdir"in x)) and (("directory"in x) or ("dir"in x) or ("mkdir" in x) or ("make the directory" in x) or ("make the folder" in x)):
        print("Name The Folder You Want To Make",end=":")
        fname=input()
        os.system("mkdir "+fname)
     elif (("open"in x) or ("run" in x) or ("perform"in x)) and (("calc"in x) or ("calculator"in x)):
        os.system("calc")
     elif (("exit" in x) or ("quit" in x) or ("close" in x) or ("terminate" in x) or ("band" in x) or ("bandkaro" in x)):
        break
     else:
        print("The System Cannot Find The File Specified->"+x) 
 elif("1" in u):
     print("M e n u  C a r d   F o r  U s e r :")
     print()
     print("N O T E:-If You Want To Terminate The program press 10")     
     print()
     print("for open a browser         : press 1")
     print("for open a texteditor      : press 2")
     print("for open a video player    : press 3")     
     print("for open a Calculator      : press 4")     
     print("Want to create a Folder    : press 5")     
     print("for open a Meeting App     : press 6")     
     print("for open a Whatsapp App    : press 7")     
 elif("3" in u) :
     print("Have A Nice Day ")
     pyttsx3.speak("Have A Nice Day")
     break
 m=input()
 if("10" in m):
   print("Have A Nice Day")
   break
 elif("1" in m):
   print("Which Browser You Would Like To Prefer....")
   print("for Chrome type Chrome")   
   print("for microsoftedge type msedge")   
   print("Type",end=":")
   b=input()
   os.system(b)
 elif("2" in m):
   print("Which TextEditor You Would Like To Prefer....")
   print("for Notepad type Notepad")   
   print("for Notepad++ type Notepad++")   
   print("Type",end=":")
   n=input()
   os.system(n)
 elif("3" in m):
   print("Which Windows media player You Would Like To Prefer....")
   print("for vlc type vlc")   
   print("for windows media player type wmplayer")   
   print("Type",end=":")
   w=input()
   os.system(w)
 elif("4" in m):
   os.system("calc")
 elif("5" in m):
   print("What Name Would You Like To Prefer For A New Folder")
   f=input()
   os.system("mkdir "+f)
   print("Succesfully Created")
 elif("6" in m):
   os.system("zoom")
 elif("7" in m):
   os.system("Whatsapp")
      