
if [[ $# -lt 2 ]];then
    echo 'please give trim start and end second'
    exit
else
    echo 'two given'
fi

# fetching obama address in wav format
youtube-dl -f bestaudio --extract-audio --audio-format wav --output president_obama_address.wav https://www.youtube.com/watch\?v\=Gh76oepKFc8


# trimming wav in order to input it to Text-To-Speech model
echo "ffmpeg -i president_obama_address.wav -ss $1 -to $2 -c copy obama3sec.wav"

rm president_obama_address.wav

