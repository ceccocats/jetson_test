sudo nvpmodel -m8
sudo jetson_clocks --fan
python3 utils/hub_reset.py
sleep 3
python3 utils/read_cam.py &
./tkDNN/build/test_rtinference ./tkDNN/build/yolo4_fp16.rt 1 0 &
./tkDNN/build/test_rtinference ./tkDNN/build/yolo4_fp16.rt 1 0 &
stress -c 3

kill $(jobs -p)
