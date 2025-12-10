# Run3 NanoAODv15

## Fetch datasets

```
fetch-datasets -i Run3_NanoAODv15/input22.yaml -w Eurasia
fetch-datasets -i Run3_NanoAODv15/input23.yaml -w Eurasia
fetch-datasets -i Run3_NanoAODv15/input24.yaml -w Eurasia
fetch-datasets -i Run3_NanoAODv15/input25.yaml -w Eurasia
```

## 2022

```
run-analysis --config config.json  --fileset Run3_NanoAODv15/input22.json  --output outputEGM_NanoAODv15/2022 --executor dask/lxplus --scaleout 100 --memory 5GiB
```

## 2023

```
run-analysis --config config.json  --fileset Run3_NanoAODv15/input23.json  --output outputEGM_NanoAODv15/2023 --executor dask/lxplus --scaleout 100 --memory 5GiB
```

## 2024

```
run-analysis --config config.json  --fileset Run3_NanoAODv15/input24.json  --output outputEGM_NanoAODv15/2024 --executor dask/lxplus --scaleout 200 --memory 5GiB
```
## 2025
```
run-analysis --config config.json  --fileset Run3_NanoAODv15/input25.json  --output outputEGM_NanoAODv15/2025 --executor dask/lxplus --scaleout 200 --memory 5GiB
```


## Post-processing
```
post-process --input-json Run3_NanoAODv15/input24.json --output-location outputEGM_NanoAODv15/2024
post-process --input-json Run3_NanoAODv15/input25.json --output-location outputEGM_NanoAODv15/2025

```

```
get-unprocessed-files --input-json Run3_NanoAODv15/input24.json --output-location outputEGM_NanoAODv15/2024 --output-json Run3_NanoAODv15/u_input24.json
get-unprocessed-files --input-json Run3_NanoAODv15/input25.json --output-location outputEGM_NanoAODv15/2025 --output-json Run3_NanoAODv15/u_input25.json

```

## Install local changes for postprocessing functions
```
pip install -e .
export PATH="$HOME/.local/bin:$PATH"
cd examples/SaS_ntuples
```