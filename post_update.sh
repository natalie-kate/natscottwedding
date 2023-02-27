#!/bin/bash
if (/usr/local/web_text.xml); then
    docker cp /usr/local/web_test.xml wedding:/WEB-INF/web.xml
    docker restart wedding
fi