sudo nvpmodel -m8
sudo jetson_clocks --fan
./tkDNN/build/test_rtinference ./tkDNN/build/yolo4_fp16.rt
echo ""
echo "RESULT SHOULD BE 25/30 FPS"
