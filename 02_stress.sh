sudo nvpmodel -m8
sudo jetson_clocks --fan
sudo rmmod uvcvideo
sudo modprobe uvcvideo quirks=128
python3 utils/hub_reset.py
echo "start test in 5 sec ... "
sleep 5

tmux \
	new-session  "./tkDNN/build/test_rtinference ./tkDNN/build/yolo4_fp16.rt 1 0" \; \
	splitw -h "python3 utils/read_cam.py /dev/video0" \; \
	selectp -t 0 \; splitw "stress -c 3" \; \
	selectp -t 2 \; splitw "jtop" \; \
	selectp -t 0 \; splitw "./tkDNN/build/test_rtinference ./tkDNN/build/yolo4_fp16.rt 1 0" \; \
	selectp -t 3 \; splitw "python3 utils/read_cam.py /dev/video2" \; \
	selectp -t 3 \; splitw "python3 utils/read_cam.py /dev/video1" \; \
	selectp -t 5 \; splitw "python3 utils/read_cam.py /dev/video3"

#python3 utils/read_cam.py /dev/video0 &
#python3 utils/read_cam.py /dev/video1 &
#python3 utils/read_cam.py /dev/video2 &
#python3 utils/read_cam.py /dev/video3 &
#./tkDNN/build/test_rtinference ./tkDNN/build/yolo4_fp16.rt 1 0 &
#./tkDNN/build/test_rtinference ./tkDNN/build/yolo4_fp16.rt 1 0 &
#stress -c 3


