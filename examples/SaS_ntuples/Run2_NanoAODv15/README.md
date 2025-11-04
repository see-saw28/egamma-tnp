# Run2 NanoAODv15

## Fetch datasets

```
fetch-datasets -i Run2_NanoAODv15/input2016.yaml -w Eurasia
fetch-datasets -i Run2_NanoAODv15/input2017.yaml -w Eurasia
fetch-datasets -i Run2_NanoAODv15/input2018.yaml -w Eurasia
```

## 2016

```
run-analysis --config config.json  --fileset Run2_NanoAODv15/input2016.json  --output outputEGM_NanoAODv15/2016 --executor dask/lxplus --scaleout 200 --memory 5GiB --log-directory logs
```

## 2017

```
run-analysis --config config.json  --fileset Run2_NanoAODv15/input2017.json  --output outputEGM_NanoAODv15/2017 --executor dask/lxplus --scaleout 200 --memory 5GiB --log-directory logs
```

## 2018

```
run-analysis --config config.json  --fileset Run2_NanoAODv15/input2018.json  --output outputEGM_NanoAODv15/2018 --executor dask/lxplus --scaleout 200 --memory 5GiB --log-directory logs
```
