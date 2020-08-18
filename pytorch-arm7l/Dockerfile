FROM arm32v7/ubuntu:18.04
COPY bin/ /usr/bin/

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update;\
    apt-get install -y libopenblas-dev libblas-dev m4 cmake cython python3-dev python3-yaml python3-setuptools python3-pip git g++ build-essential gfortran libssl-dev
RUN python3 -m pip install --upgrade pip

# Long Running and needed for future package installs
RUN python3 -m pip install Cython \
    && python3 -m pip install pandas \
    && python3 -m pip install sklearn \
    && python3 -m pip install scikit-build

RUN python3 -m pip install numpy ninja pyyaml setuptools cmake cffi typing_extensions future six requests

RUN mkdir /build
WORKDIR /build

RUN git clone --recursive --depth 1 https://github.com/pytorch/pytorch

WORKDIR /build/pytorch

ENV USE_CUDA=0
ENV USE_DISTRIBUTED=0
ENV USE_MKLDNN=0
ENV USE_NNPACK=0
ENV USE_QNNPACK=0
ENV USE_NUMPY=1

RUN python3 setup.py install
