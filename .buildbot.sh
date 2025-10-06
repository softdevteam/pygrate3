#!/bin/sh

set -e

./configure
make -j `nproc`
./python -m test
