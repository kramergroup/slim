docker build -f Dockerfile.buildcentos -t slim-build-centos .
docker container create --name extract slim-build-centos:latest
docker container cp extract:/root/rpmbuild/RPMS .
docker container cp extract:/root/rpmbuild/SRPMS .
docker rm extract
