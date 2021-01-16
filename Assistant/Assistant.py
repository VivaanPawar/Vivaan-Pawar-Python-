# Import the Gtts module for text  
# to speech conversion 
from gtts import gTTS 
  
# import Os module to start the audio file
import os 
  
mytext = 'Hi Guys,My Name Is Vivaan Pawar And You Are Watching My YouTube Channel Vivaan MAt'
  
# Language we want to use 
language = 'en'
  

myobj = gTTS(text=mytext, lang=language, slow=False) 
  

myobj.save("output2.mp3") 
  
# Play the converted file 
os.system("start output2.mp3") 