FROM google/cloud-sdk:latest

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        zlib1g-dev \
        libssl-dev \
        libbz2-dev \
        libreadline-dev \
        libsqlite3-dev \
        swig \
        mecab \
        libmecab-dev \
        locales \
        locales-all && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/lib/x86_64-linux-gnu/mecab/dic && \
    git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git /tmp/neologd && \
    /tmp/neologd/bin/install-mecab-ipadic-neologd -n -u -y && \
    rm -rf /tmp/neologd

RUN git clone https://github.com/riywo/anyenv ~/.anyenv && \
    echo "export PATH=$HOME/.anyenv/bin:$PATH" >> ~/.bash_profile && \
    echo "eval $(anyenv init -)" >> ~/.bash_profile

RUN /bin/bash -lc 'mkdir -p ~/.anyenv/plugins && \
    git clone https://github.com/znz/anyenv-update.git ~/.anyenv/plugins/anyenv-update'

RUN /bin/bash -lc 'anyenv install pyenv'

RUN /bin/bash -lc 'pyenv install 2.7.15 && \
    pyenv install 3.6.7 && \
    pyenv global 2.7.15 3.6.7'

WORKDIR /usr/src/app

COPY Pipfile Pipfile.lock ./

ENV PYTHONUNBUFFERED=1 \
    LANG=C \
    LC_CTYPE=en_US.UTF-8 \
    MECAB_DICDIR=/usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd

RUN /bin/bash -lc 'pip3 install -U pip && \
    pip3 install pipenv && \
    pipenv install --system'

COPY . ./

CMD ["python", "app.py"]
