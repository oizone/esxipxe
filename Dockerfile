FROM alpine:latest
RUN apk add --no-cache dhcp tftp-hpa nginx git
RUN mkdir /tftp
RUN touch /var/lib/dhcp/dhcpd.leases
COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]