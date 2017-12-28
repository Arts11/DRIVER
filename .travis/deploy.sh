#!/usr/bin/env bash

set -e
set -x

for image in app editor web gradle analysis;
do
  docker push "quay.io/azavea/driver-${image}:${TRAVIS_TAG}"
  docker tag "quay.io/azavea/driver-${image}:${TRAVIS_TAG}" "quay.io/azavea/driver-${image}:${TRAVIS_TAG}"
  docker push "quay.io/azavea/driver-${image}:${TRAVIS_TAG}"
done
