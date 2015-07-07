#!/bin/bash

DIST_DIR=.
BUILD_DIR=$(cd ~/rpmbuild/ && pwd)
VERSION=0.8.2.2

rm -rf ${BUILD_DIR}/*
mkdir -p ${BUILD_DIR}/{BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}

curl -o ${BUILD_DIR}/SOURCES/UcsSdk-${VERSION}.tar.gz https://pypi.python.org/packages/source/U/UcsSdk/UcsSdk-${VERSION}.tar.gz

cp ${DIST_DIR}/*.spec ${BUILD_DIR}/SPECS/
sed -i -e "s/Version:.*/Version: $VERSION/g" *.spec

rsync -rlpt --exclude ".git*" --exclude "*.spec" --exclude "build-rpm.sh" ${DIST_DIR}/ ${BUILD_DIR}/SOURCES/

rpmbuild -bs ${BUILD_DIR}/SPECS/*.spec

srpm_file=`ls ${BUILD_DIR}/SRPMS/. | awk '{print $1}'`
mock --rebuild "${BUILD_DIR}/SRPMS/${srpm_file}" --resultdir "${BUILD_DIR}/RPMS/"