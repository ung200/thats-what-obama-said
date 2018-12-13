import config
import os


# run twitter script
# output is saved in twitter_dir, we take the long_tweets file, in accordance with DC_TTS limitations (they only take upto 155 char limit of each sentence.)
twitter_dir = config.DIRS['twitter']
os.system('python %s' % twitter_dir+'get_tweets.py')

voice_transfer_input_dir = config.DIRS['voice_transfer_input']

# get obama wav from his youtube address
# output is saved in obama_address_dir, as obama3sec.wav
obama_address_dir = config.DIRS['obama_address']
os.system('bash %sfetch.sh 8 11' % obama_address_dir)
# copying output file to stlye transfer input location
os.system('mv %obamae3sec.wav %/person3sec.wav' %(obama_address_dir, voice_transfer_input_dir))


# input above text file to Text-to-Speech, it reads this file from it's file hyperparams.py, which has this text filename hardcoded for now, will be automized in the future.
# output female voice of obama's tweet is saved iin dc_tts_dir directory under samples folder. the TTS creates .wav file for each sentence in given text file, but we just keep one and remove all others in order to make things clearer.
dc_tts_dir = config.DIRS['dc_tts']
os.system('python %ssynthesize.py' % dc_tts_dir)

# moving one wav file to stlye transfer input location
os.system('mv %samples/6.wav %/person3sec.wav' %(dc_tts_dir, voice_transfer_input_dir))
os.system('rm %samples/*' % dc_tts_dir)



# the above output - person3sec.wav is now given as an input along with obama's address trimmed file - obama3sec.wav to neural style transfer.
# result file is saved as style_transfer_CNN_C.wav in voice transfer dir
voice_transfer_dir = config.DIRS['voice_transfer']
os.system('python %strain.py' % voice_transfer_dir)
obama_final_audio_location = voice_transfer_dir + 'style_transfer_CNN_C.wav'

# obamanet initiates through the script run.sh in it's root dir and takes obama wav file (as outputted from voice transfer) as input and outputs obama's video.
# output is obama's video which is saved in obamanet root dir by the name of output.mp4, an intermediate mp4 file with mouth coefficients is also generated and saved in obamanet root dir.
obamanet_dir = config.DIRS['obamanet']
os.system('bash %srun.sh %s' %(obamanet_dir, obama_final_audio_location))
## output.mp4 is our final end result
