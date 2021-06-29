import wave

def saveWaveFile(framesRec,name,sample_size,framerate,channels):
    wf = wave.open(name, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(sample_size)
    wf.setframerate(framerate)
    wf.writeframes(b''.join(framesRec))
    
    wf.close()
