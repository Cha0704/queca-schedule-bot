FROM ubuntu:24.04

WORKDIR /usr/src/app

RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

RUN apt update
RUN apt install -y curl python3 python3-pip

RUN curl -O https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get install -yq --no-install-recommends ./google-chrome-stable_current_amd64.deb && \
    apt-get clean && rm google-chrome-stable_current_amd64.deb

COPY requirements.txt ./
RUN pip3 install --no-cache-dir --break-system-packages -r requirements.txt

COPY . .

CMD [ "python3", "-m", "tyouseisan" ] 