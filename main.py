# DRIES DEPOORTER
# MARCH 2024

import os
from elevenlabs.client import ElevenLabs
from elevenlabs import stream
from elevenlabs import VoiceSettings
#from elevenlabs import save

from openai import OpenAI
import mpv

import cv2 
from dotenv import main
import base64
import requests
import time


player = mpv.MPV(ytdl=True)

be_polite_to_ai = True

def be_polite():
   if be_polite_to_ai:
      return "plz"
   else:
      return ""


main.load_dotenv() 

openAI_client = OpenAI(
  api_key=os.getenv("OPENAI_KEY")
)

client = ElevenLabs(
  api_key= os.getenv('ELEVENLABS_API_KEY')
)

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

def textToSpeech(sentence):
            audio_stream = client.generate(
                text=str(sentence),
                voice="Kylie",
                model="eleven_turbo_v2",
                stream=True
            )
            stream(audio_stream)


 
def ImageToText():
  image_path = "frame.jpg"

  # Getting the base64 string
  base64_image = encode_image(image_path)

  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.getenv("OPENAI_KEY")}"
  }

  payload = {
    "model": "gpt-4-turbo",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            'text': "You are Kylie J. (the influencer) and you help me with taking the perfect Instagram photo. Short sentence. Say what you like and don't like and give tips what to change in the photo to go viral.  Say something about what you see in the photo. Say the following in your own words at the ends: 'Ok let's try another one, and do a countdown for the next try'.Don't you are not Kilie J. I only want maximum 3 sentences. "
            #"text": "You are Kylie J. (the influencer) and you help me with taking the perfect Instagram photo. Short sentence. Say what you like and don't like and give tips what to change in the photo to go viral.  Say something about what you see in the photo. Say the following in your own words at the ends: 'Ok let's try another one, and do a countdown for the next try'.Don't you are not Kilie J. I only want maximum 3 sentences. " + be_polite_to_ai

            #"text": "You are Kylie J. (the influencer) and need to help me to take the perfect Instagram photo. You need to give advice in what to change it the photo to make it go viral on the gram. Pls give the advice in a really short sentence. Say the reason why it would better work in Instagram. Be Kylie Jenner. Always describe something that you see in the picture. Maximum 1 sentence. Always ends with something like 'ok let's try another photo you can do better' and do a quick countdown. But says this in what Kylie would say. Say what you don't like and like about the photo. Be very clear what the next pose can be.  Don't say you can't " + be_polite()
          },
          {
            "type": "image_url",
            "image_url": {
              "url": f"data:image/jpeg;base64,{base64_image}"
            }
          }
        ]
      }
    ],
    "max_tokens": 128
  }

  response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

  data = response.json()
  #print(data)
  content = data['choices'][0]['message']['content']
  #print(content)
  return content




vid = cv2.VideoCapture(0) 

while(True): 
      
    # Capture the video frame 
    # by frame 
    ret, frame = vid.read() 
    resized_frame = cv2.resize(frame, (0,0), fx=0.35, fy=0.35) 
    cv2.imwrite('frame.jpg', resized_frame)
  
    # Display the resulting frame 
    #cv2.imshow('frame', resized_frame)
    
    player.play('iPhone_shutter.mp3')
    print("-> Played iPhone shutter sound")
    time.sleep(0.01)

    advice = ImageToText()
    print("-> Generated advice")
    textToSpeech(advice)
    print("-> playing cloned voice from Kylie")
    
    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
    

vid.release() 
cv2.destroyAllWindows() 