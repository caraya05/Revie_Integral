#!/bin/bash
echo 'init qa code'
pylint  $(find . -name "*.py" -type f)