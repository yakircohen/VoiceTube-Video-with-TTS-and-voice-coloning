# VoiceTube - Video with TTS and voice coloning
The software can imitate any voice which later will be used as the announcer's voice for the video's subtitles.(final project)
![VoiceTube logo](https://github.com/yakircohen/Video-with-TTS-and-voice-coloning/blob/main/logo.png)


## Subtitles Edit
![Subtitles Edit](https://github.com/yakircohen/Video-with-TTS-and-voice-coloning/blob/main/Subtitles%20Edit.png)
### Edit subtitles screen:
1.	Load file: select a subtitle file and uploads it to the table.
2.	Open video: Select a video and upload it to the screen.
3.	The table: each cell in the table can be edited by double-clicking.
4.	Delete: deletes a row in the table to which it belongs.
5.	Start: set the starting time for the subtitle to appear.
6.	End: set the final time for the subtitle to disappear.
7.	Add: After adding the text and its appearance times the button adds it to the table.
8.	Go to TTS (text to speech): After the user finished editing the subtitles, he is being taken to the recording stage.


## Converter
![converter1](https://github.com/yakircohen/Video-with-TTS-and-voice-coloning/blob/main/12.png)
![converter2](https://github.com/yakircohen/Video-with-TTS-and-voice-coloning/blob/main/13.png)
### Converter screen:
1. 1.	Choose text to speech: Gives you different options of voices and also record your voice.
2.	New Record: Takes you to the recording screen where you can record yourself so that the software can learn your voice.
3.	Select Audio: Opens a window for selecting an audio file that the software will learn to emulate.
4.	Produce audio: Begins the process of imitating the voice and transferring the subtitles that the user puts to the voice and pasting it on the video that the user initially selected.
5.	Combination video and audio Combination: Allows adding only the voice you selected, without the subtitles.
6.	video, audio and subs Combination: Allows you to add the subtitles in addition to the voice you selected.
7.	Start: Subtitle voice starting time.
8.	End: Subtitle voice ending time.
9.	Use suggested subtitles file time: Option to select the subtitle end times along with the subtitle voice.
10.	Play video result: After completing the entire process, the user will see a window with the video, voice and subtitles he selected.

## Recorder:
![record](https://github.com/yakircohen/Video-with-TTS-and-voice-coloning/blob/main/recorod.png)
### recording screen:
1.	Back: return to the main screen.
2.	Auto gain for frequency spectrum: Shows the frequency more clearly in the screen below.
3.	Manual gain level for frequency spectrum: Manual zooming frequency selection.
4.	Select device: Gives you some recording options from all existing computer devices.
5.	Record: starts recording the user
6.	Stop: Stops recording without being able to continue recording any more.
7.	Play: Plays the recording.
8.	Pause: Pauses the recording
9.	Save: Gives the user the option to save the recording he made after giving it a name in the next row.


## Video out:
![video](https://github.com/yakircohen/Video-with-TTS-and-voice-coloning/blob/main/output.png)
### Video out screen:
Shows you the final video together with the voice and subtitles that the user selected. 
# Usage
1. Ffmpeg installed in command line.  
2. k-lite codec kit.
3. Python 3.7 with the following installs:<br/>
Install pytorch<br/>
If using windows<br/>
```
conda install pytorch torchvision torchaudio cpuonly -c pytorch
```
installing this sould install more libraries like Numpy and more.<br/>
otherwise go to https://pytorch.org/get-started/locally/ <br/>
make sure your python folder is not locked (as partially read only, read only)

4. if you don't have conda you might have to install it
then run: <br/>
    conda install pyaudio<br/>
    pip install sounddevice<br/>
    pip install pyqtwebengine<br/>
 pip install PyQt5==5.10<br/>
 pip install matplotlib<br/>
 pip install pymediainfo<br/>
pip install scipy<br/>
pip install unidecode<br/>
pip install inflect<br/>
pip install tensorflow==1.15<br/>
pip install librosa<br/>
pip install multiprocess<br/>
pip install webrtcvad<br/>
pip install pyttsx3<br/>

5. Download tacotron  https://drive.google.com/file/d/1KWt2kvAIjJV4EDtaKCOLdgCZkgjrX64D/view?usp=sharing   <br/>
   insert him here==>  SStV2Ref\synthesizer\saved_models\logs-pretrained\taco_pretrained<br/>
   
For more details, contact me at yakircohen320@gmail.com





