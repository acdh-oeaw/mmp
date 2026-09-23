# MMP

[![Linting](https://github.com/acdh-oeaw/mmp/actions/workflows/lint.yml/badge.svg)](https://github.com/acdh-oeaw/mmp/actions/workflows/lint.yml)
[![Test](https://github.com/acdh-oeaw/mmp/actions/workflows/test.yml/badge.svg)](https://github.com/acdh-oeaw/mmp/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/acdh-oeaw/mmp/branch/main/graph/badge.svg?token=PQTAIJWOGX)](https://codecov.io/gh/acdh-oeaw/mmp)

## Mapping Medieval Peoples: Visualizing Semantic Landscapes in Early Medieval Europe

### About

A Django based backend for <https://mmp.acdh.oeaw.ac.at/>

## Docker

### building the image

```shell
docker build -t mmp:latest .
```

```shell
docker build -t mmp:latest --no-cache .
```

### running the image

```shell
docker run -it --network="host" --rm --env-file env.default mmp:latest
```
