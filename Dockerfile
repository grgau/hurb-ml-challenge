FROM python:3.10-slim
WORKDIR /hurb-ml-challenge

COPY requirements.txt ./
COPY bentofile.yaml ./
COPY docker-entrypoint.sh ./

RUN pip install \
      --user \
      --trusted-host pypi.org \
      --trusted-host pypi.python.org \
      --default-timeout=300 \
      --no-cache-dir \
      -r requirements.txt &&\
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV PATH=/root/.local/bin:$PATH

COPY src ./src
COPY tests ./tests

EXPOSE 3000
ENTRYPOINT ["bash", "docker-entrypoint.sh"]