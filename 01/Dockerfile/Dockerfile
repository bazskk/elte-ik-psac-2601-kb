FROM alpine:latest

COPY ./var/srv/flask-minimal /srv/flask-minimal
COPY ./docker-entrypoint.sh /bin/docker-entrypoint

RUN chmod +x /bin/docker-entrypoint
RUN apk update && apk add python3
RUN cd /srv/flask-minimal && \
    python3 -m venv .venv && \
    . .venv/bin/activate && \
    pip3 install .

ENTRYPOINT [ "/bin/docker-entrypoint" ]

EXPOSE 8080

CMD [ "/bin/sh" ]