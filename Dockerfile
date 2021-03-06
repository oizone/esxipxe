FROM mcr.microsoft.com/dotnet/core/sdk:3.1
LABEL maintainer="oizone@oizone.net"

#ARG GH_RUNNER_VERSION="2.267.1"
#ARG TARGETPLATFORM
ARG TARGETPLATFORM="linux/arm/v7"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
ENV DEBIAN_FRONTEND=noninteractive
ENV ANSIBLE_HOST_KEY_CHECKING=False
ARG APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE=yes

RUN echo deb http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main | tee -a /etc/apt/sources.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367
RUN apt-get update
RUN apt-get install -y --no-install-recommends jq python-ncclient ansible isc-dhcp-server tftpd-hpa p7zip-full python-xlrd uwsgi-plugin-python

WORKDIR /actions-runner
COPY install_actions.sh /actions-runner

RUN chmod +x /actions-runner/install_actions.sh \
  && /actions-runner/install_actions.sh ${TARGETPLATFORM} \
  && rm /actions-runner/install_actions.sh

RUN touch /var/lib/dhcp/dhcpd.leases

COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh

COPY token.sh /
RUN chmod +x /token.sh

ENTRYPOINT ["/entrypoint.sh"]
