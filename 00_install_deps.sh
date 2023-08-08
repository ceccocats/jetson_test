apt update
apt install -y python3-serial python3-can python3-smbus
apt install -y libeigen3-dev libyaml-cpp-dev cmake wget

wget http://github.com/Kitware/CMake/releases/download/v3.19.3/cmake-3.19.3-Linux-aarch64.sh
bash cmake-3.19.3-Linux-aarch64.sh --skip-license --prefix=/usr/local/
rm cmake-3.19.3-Linux-aarch64.sh

mkdir -p tkDNN/build ; cd tkDNN/build ; cmake .. ; make -j4 test_rtinference
wget -nc https://github.com/ceccocats/tkDNN/releases/download/v0.6/yolo4_fp16.rt
