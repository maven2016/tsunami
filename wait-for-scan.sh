#!/bin/bash

set -e

cmd="$@"

until [ "$(ls -A logs )" ]; do 
    echo "tsunami scan is not complete yet" 
    sleep 2 
done

>&2 echo "tsunami scan is complete"
exec $cmd
