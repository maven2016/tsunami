#!/bin/bash

while read TARGET; do
    OUTPUT="logs/tsunami-output-${TARGET}.json"
    java -cp "tsunami-main-0.0.5-SNAPSHOT-cli.jar:plugins/*" -Dtsunami-config.location=tsunami.yaml com.google.tsunami.main.cli.TsunamiCli --ip-v4-target=${TARGET} --scan-results-local-output-format=JSON --scan-results-local-output-filename=${OUTPUT}
done < hosts.txt
