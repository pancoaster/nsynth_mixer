# VARIABLES

recorder = 0;
visualizer = 0;
instruments = 0;
notesPerChord = 0;
canvases = [];
nowPlaying = 0;
fullSong = 0;
runLocal = False;
visualizers = [];
visualizerArr = [];
isInputVoice = True;
isRecording = False;
supportsMidi = False;
audioRecorded = 0;
recordingBroken = False;
midiDrums = [36, 38, 42, 46, 41, 43, 45, 49, 51];
jazzHits = [51, 53, 54, 42, 59, 44, 46];
# audioCtx = new (AudioContext || webkitAudioContext)();
tf = 0;
z1 = 0;
z2 = 0;
tsynth = 0;
drumMap = 0;
progSeqs = 0;
chordSeqs = 0;
programMap = 0;
playerMaster = 0;
globalReverb = 0;
globalLimiter = 0;
Z_DIM = 256;
numExtraBars = 3;
numExtraSteps = 1;
numSteps = numExtraBars * 6 * numExtraSteps;
MAX_NOTE = 71;
MIN_NOTE = 20;
MAX_PAN = 0.2;
MIN_DRUM = 35;
MAX_DRUM = 81;
sectionSize = 8;
globalCompressor = 0;
numContainers = 9;
STEPS_PER_QUARTER = 24;
HUMANIZE_SECONDS = 0.07;
chords = [];
numChords = 4;
numTimes = sectionSize / numChords;
onsets_frames_uni = 0;
multitrack_chords = 0;
drum_kit_rnn = 0;
midiRecorder = 0;
trio_4bar = 0;
vae = 0;
pulsePattern = True;
temperature = 1.1;


# TRIO_EXAMPLE = { notes: [], quantizationInfo: { stepsPerQuarter: 4 } };

# not needed anymore, was required for web ui
def initObjects():
    pass


def initModels():
    pass


def init():
    print("Hello from a init function")
    initObjects();
    initModels();


###############################
init();

##############################################################
import os
import numpy as np
import matplotlib.pyplot as plt
from magenta.models.nsynth import utils
from magenta.models.nsynth.wavenet import fastgen
from IPython.display import Audio


fname = 'seek_09.wav'
fname2 = 'cresendo_prog_piano_42.wav'
ckpt_path = os.path.abspath('model.ckpt-200000')
sr = 16000

audio = utils.load_audio(fname, sample_length=sr*2, sr=sr)
audio2 = utils.load_audio(fname2, sample_length=sr*2, sr=sr)

sample_length = audio.shape[0]
sample_length2 = audio2.shape[0]

enc1 = fastgen.encode(audio, ckpt_path, sample_length)
enc2 = fastgen.encode(audio2, ckpt_path, sample_length2)

enc_mix = (enc1 + enc2) / 2.0
save_paths = ['gen_' + fname2]
fastgen.synthesize(enc_mix,
                   save_paths=save_paths,
                   checkpoint_path=ckpt_path,
                   samples_per_save=int(sample_length / 10))




