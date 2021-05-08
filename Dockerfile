FROM adoptopenjdk/openjdk13:debianslim as base
ENV HOME=/usr/

RUN apt-get update \
 && apt-get install -y --no-install-recommends git ca-certificates

RUN bash -c "$(curl -sfL https://raw.githubusercontent.com/google/tsunami-security-scanner/master/quick_start.sh)" \
    && rm -rf $home/tsunami/repos

FROM adoptopenjdk/openjdk13:debianslim

RUN apt-get -y update && apt-get install -y \
    nmap \
    ncrack \
    ca-certificates
    
WORKDIR /usr/tsunami

COPY --from=base /usr/tsunami /usr/tsunami

COPY startup.sh /usr/tsunami 

CMD ["./startup.sh"]
