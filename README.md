# VoiceTube - Video with TTS and voice coloning
The software can make any voice that read your subtitles on the video.(final project)
![VoiceTube logo](https://github.com/yakircohen/Video-with-TTS-and-voice-coloning/blob/main/logo.png)


## Subtitles Edit:
![Subtitles Edit](https://github.com/yakircohen/Video-with-TTS-and-voice-coloning/blob/main/Subtitles%20Edit.png)
### Edit subtitles screen:
Load file: select a subtitle file and uploads into the table.
Open video: Select a video and upload it to the screen.
The table: each cell in the table can be edited by double-clicking.
Delete: deletes a row in the table to which it belongs.
Start: Determining the start time of the subtitle appearance.
End: Determining the final time of subtitle disappearance.
Add: After adding the text and its appearance times the button adds it to the table.
Go to TTS(text to speech): After the user has finished editing the subtitles, he is taken to the recording stage.

## Converter:
![converter1](https://github.com/yakircohen/Video-with-TTS-and-voice-coloning/blob/main/12.png)
![converter2](https://github.com/yakircohen/Video-with-TTS-and-voice-coloning/blob/main/13.png)
Converter screen:
Choose text to speech: Gives you different options of voices and also your voice.
Record new: Takes you to the recording screen where you can record yourself so that the software can learn your voice.
Audio select: Opens a window for selecting an audio file that the software will learn to emulate.
Produce audio: Begins the process of imitating the voice and transferring the subtitles that the user puts to the voice and pasting it on the video that the user initially selected.
Video audio only combine: Allows you to get only the voice you selected on the video without the subtitles.
Subtitle audio video combine: Allows you to get only the voice you selected on the video with the subtitles.
Start: Subtitle voice start time.
End: Subtitle voice end time.
Use suggested srt file time: Option to select the subtitle end times along with the subtitle voice.
Play video result: After completing the entire process, the user will see a window with the video that he selected with the voice and the subtitles.

## Recorder:
![record](https://github.com/yakircohen/Video-with-TTS-and-voice-coloning/blob/main/recorod.png)
record screen:
Back: return to the main screen.
Auto gain for frequency spectrum: Shows the frequency more deeply in the screen below. 
Manual gain level for frequency spectrum: Manual deep frequency selection.
Select device: Gives you some recording options from all existing computer devices.
Record: Begins to record the user
Stop: Stops recording without being able to continue recording any more
Play: Plays the recording.
Pause: Pauses the recording
Save: Gives the user the option to save the recording he made after giving it a name in the next row.

## Video out:
![video](https://github.com/yakircohen/Video-with-TTS-and-voice-coloning/blob/main/output.png)
Video out screen:
Shows you the result of the video you selected together with the voice and also the subtitles if the user selected the option to paste the subtitles.

# Usage
1. Using python 3.7
2. Install pytorch
3. If you using windows
```
conda install pytorch torchvision torchaudio cpuonly -c pytorch
```
otherwise go to https://pytorch.org/get-started/locally/ 

4.run spyder or any other python installer as admin
Install the packages:
conda install pyaudio
pip install sounddevice
pip install pyqtwebengine
pip install PyQt5==5.10
pip install matplotlib
pip install pymediainfo
pip install scipy
pip install unidecode
pip install inflect
pip install tensorflow==1.15
pip install librosa
pip install multiprocess
pip install webrtcvad
pip install pyttsx3

5.install also klite codec kit

For more details, contact me at yakircohen320@gmail.com





