FROM alpine:latest
RUN apk add --no-cache dhcp tftp-hpa nginx
#ENTRYPOINT [""]