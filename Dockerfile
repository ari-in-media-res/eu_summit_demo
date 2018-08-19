# Pull base image.
FROM ubuntu:17.10

# Install Python.

RUN apt-get update
RUN apt-get install -y software-properties-common vim
RUN add-apt-repository ppa:jonathonf/python-3.6

RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv
RUN apt-get install -y git

# update pip
RUN python3.6 -m pip install pip --upgrade
RUN python3.6 -m pip install wheel
RUN \
  cd /usr/local/bin && \
  ln -s /usr/bin/python3 python && \
  pip3 install --upgrade pip && \
  rm -rf /var/lib/apt/lists/*

RUN python -m pip install 'flask==0.12.2'
RUN python -m pip install 'pandas==0.20.3'
RUN python -m pip install 'scipy==0.19.1'
RUN python -m pip install 'sklearn==0.0'
RUN python -m pip install 'scikit-learn==0.19.0'
RUN python -m pip install 'category_encoders==1.2.6'

ADD app.py /
ADD activity__ma__dtree.pkl /

# Define working directory.
WORKDIR /

CMD [ "python", "./app.py"]
