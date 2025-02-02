FROM python:3.13-slim-bullseye

RUN useradd -mU mitmproxy
RUN apt-get update \
    && apt-get install -y --no-install-recommends gosu gcc wget zlib1g-dev libjpeg-dev libwebp-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install -U pip \
    && CC="cc -mavx2" pip install -U --force-reinstall pillow-simd --global-option="build_ext" --global-option="--enable-webp" \
    && pip install mitmproxy

VOLUME /home/mitmproxy/.mitmproxy

RUN wget -P /usr/local/bin https://raw.githubusercontent.com/mitmproxy/mitmproxy/main/release/docker/docker-entrypoint.sh \
    && chmod 755 /usr/local/bin/docker-entrypoint.sh
ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 3126

CMD ["/home/mitmproxy/files/run.sh"]
