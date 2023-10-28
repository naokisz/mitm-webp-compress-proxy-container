#!/bin/bash

if [ -z $MITM_USER ] || [ -z $MITM_PASS ]; then
  echo 'Please set the "SMITM_USER" and "$MITM_PASS" environment variable and try again.' >&2
  exit -1
fi

gosu mitmproxy mitmdump --listen-port 3126 --ssl-insecure -s /home/mitmproxy/files/flows.py --set stream_large_bodies=10m --ignore-hosts '(mzstatic|apple|icloud|mobilesuica|crashlytic|google-analytics|merpay|paypay|rakuten-bank|fate|colopl|rakuten-sec|line|kyash|plexure)' --set block_global=false --set flow_detail=1 --showhost --rawtcp --proxyauth ${MITM_USER}:${MITM_PASS}
