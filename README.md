# paloalto-ip-parser

In order to divert the traffic that has the AWS network as destination, we need a dynamic list based on: https://ip-ranges.amazonaws.com/ip-ranges.json. Since PA cannot ingest JSON natively, we are parsing json to a HTTP response  with IP addresses only.
