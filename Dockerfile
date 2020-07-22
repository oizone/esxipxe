FROM alpine:latest
RUN apk add --no-cache dhcp tftp-hpa nginx git p7zip
RUN mkdir -p /tftp/cd
RUN touch /var/lib/dhcp/dhcpd.leases
RUN mkdir /run/nginx
COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh
#ENTRYPOINT ["/entrypoint.sh"]