import pyaudio
import speech_recognition as sr
import webbrowser as wb
import subprocess

print("-------------")
print("-  Options  -")
print("-------------")
print("1.Search <ProgramName>")
print("2.Browse <BrowseQuery>")
r=sr.Recognizer()
r.energy_threshold=4000
with sr.Microphone() as source:
	print("Say Something!")
	audio=r.listen(source)
	try:
		spokenText=r.recognize_google(audio)
		print("You said "+ spokenText)
	except LookupError:
   		print('Speech not understood')
if(spokenText[0]=='b' or spokenText[0]=='B'):
	spokenList=spokenText.split(' ',1)
	var=wb.get('firefox')
	url="https://www.google.com.tr/search?q={}".format(spokenList[1])
	var.open(url)
elif(spokenText[0]=='s' or spokenText[1]=='S'):
	spokenList=spokenText.split(' ',1)
	spokenList1=spokenList[1].replace(' ','')
	subprocess.call(["bash","script.bash",spokenList1])
else:
	print("InValid Request")
	
