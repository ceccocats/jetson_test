sudo nvpmodel -m8
sudo jetson_clocks --fan
sudo rmmod uvcvideo
sudo modprobe uvcvideo quirks=128
python3 utils/hub_reset.py
sleep 3
python3 utils/read_cam.py /dev/video0 &
python3 utils/read_cam.py /dev/video1 &
python3 utils/read_cam.py /dev/video2 &
python3 utils/read_cam.py /dev/video3 &
./tkDNN/build/test_rtinference ./tkDNN/build/yolo4_fp16.rt 1 0 &
./tkDNN/build/test_rtinference ./tkDNN/build/yolo4_fp16.rt 1 0 &
stress -c 3

kill $(jobs -p)
