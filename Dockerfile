FROM ghcr.io/prefix-dev/pixi:latest

RUN apt update && apt install -y git
COPY . /app
WORKDIR /app
RUN pixi install

ENTRYPOINT ["pixi"]
CMD ["run", "serve"]