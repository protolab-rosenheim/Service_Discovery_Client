FROM alpine:3.8

WORKDIR /usr/src/app

RUN apk --no-cache add \
        python3 \
        libstdc++ \
        lapack \
        openssl \
        libffi \
        libxml2 \
        libxslt \
        nano \
        && \
    pip3 install --no-cache-dir --upgrade pip setuptools && \
    apk add --no-cache --virtual .build-deps \
        build-base \
        python3-dev \
        lapack-dev \
        gfortran \
        g++ \
        make \
        openssl-dev \
        libffi-dev \
        libxml2-dev \
        libxslt-dev \
        && \
    ln -s /usr/include/locale.h /usr/include/xlocale.h && \
    rm -fr /root/.cache && \
    rm /usr/include/xlocale.h


COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN apk del .build-deps

ENV TZ=Europe/Berlin
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY . .

ENV PYTHONPATH `pwd`/..

CMD ["python3", "SD_Client", "-l", "DEBUG"]