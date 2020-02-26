#!/bin/sh

pip install -r requirements.txt
# git clone http://people.csail.mit.edu/hubert/git/pyaudio.git
# python pyaudio/setup.py install
sudo apt-get install libportaudio-dev
sudo apt-get install python-dev
sudo apt-get install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev
pip install pyaudio
python -m nltk.downloader punkt