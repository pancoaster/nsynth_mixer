
from pydub import AudioSegment


for x in range(1, 89):
    t1 = (1 + (x-1)*3) * 1000 #Works in milliseconds    ## 1, 4, 7, 10
    t2 = (3 + (x-1)*3) * 1000                           ## 3, 6, 9, 12
    newAudio = AudioSegment.from_wav("cresendo_prog_piano.wav")
    newAudio = newAudio[t1:t2]
    newAudio.export('cresendo_prog_piano_' + str(x+20) + '.wav', format="wav") #Exports to a wav file in the current path.

exit()




from midiutil.MidiFile import MIDIFile

# create your MIDI object
mf = MIDIFile(1)     # only 1 track
track = 0   # the only track

time = 0    # start at the beginning
mf.addTrackName(track, time, "Sample Track")
mf.addTempo(track, time, 120)

# add some notes
channel = 0
volume = 100
## space 2 beats @ 120 bpm for 1 second delay
## 4 beats @ 120 bpm is 2 seconds per note
pitch = 21
time = 2             
duration = 4         # 2 seconds
mf.addNote(track, channel, pitch, time, duration, volume)

for x in range(22, 109):
    pitch = x
    time = 2 + 6 * (x-21)
    duration = 4
    mf.addNote(track, channel, pitch, time, duration, volume)
    
# write it to disk
with open("output.mid", 'wb') as outf:
    mf.writeFile(outf)

    
exit()




