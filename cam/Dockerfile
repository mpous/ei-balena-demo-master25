FROM balenalib/raspberrypi4-64-debian:bullseye-build

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y python3-pip ffmpeg libsm6 libxext6

RUN pip3 install --upgrade pip

RUN pip3 install opencv-contrib-python requests pillow

COPY *.py ./
COPY *.jpg ./

CMD ["sleep", "infinity"]

