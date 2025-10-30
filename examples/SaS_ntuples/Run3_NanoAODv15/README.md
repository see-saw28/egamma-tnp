# Run3 NanoAODv15

## Fetch datasets

```
fetch-datasets -i Run3_NanoAODv15/input24.yaml -w Eurasia
fetch-datasets -i Run3_NanoAODv15/input25.yaml -w Eurasia
```

## 2024

```
run-analysis --config config.json  --fileset Run3_NanoAODv15/input24.json  --output outputEGM_NanoAODv15/2024 --executor dask/lxplus --scaleout 200 --memory 5GiB --log-directory logs
```
## 2025
```
run-analysis --config config.json  --fileset Run3_NanoAODv15/input25.json  --output outputEGM_NanoAODv15/2025 --executor dask/lxplus --scaleout 200 --memory 5GiB --log-directory logs
```
