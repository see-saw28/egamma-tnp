# Run3 NanoAODv13

## Fetch datasets

```
fetch-datasets -i Run3_NanoAODv13/input22.yaml -w Eurasia
fetch-datasets -i Run3_NanoAODv13/input23.yaml -w Eurasia
```

## 2022

```
run-analysis --config config.json  --fileset Run3_NanoAODv13/input22.json  --output outputEGM_NanoAODv13/2022 --executor dask/lxplus --scaleout 200 --memory 5GiB --log-directory logs
```

## 2023

```
run-analysis --config config.json  --fileset Run3_NanoAODv13/input23.json  --output outputEGM_NanoAODv13/2023 --executor dask/lxplus --scaleout 200 --memory 5GiB --log-directory logs
```
