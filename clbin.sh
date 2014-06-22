#!/bin/bash
# version:0.2
# author:mhohai

# quick upload screen shot
# setting your own screen shot default save Directory
cd ~/Pictures
if [ $1 ]; then
	# You can add yourself picture as $1
	png=$1
else
	# gnome-screenshot -a
	png=`ls -rt | tail -1`
fi
url=`curl -F "clbin=@$png" https://clbin.com`
# Require:sudo apt-get install xclip
echo $url | xclip -sel clip
notify-send "Done $url"
# Thanks https://clbin.com
