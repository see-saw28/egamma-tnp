# Run2 NanoAODv9

## Fetch datasets

```
fetch-datasets -i Run2_NanoAODv9/input2016.yaml -w Eurasia
fetch-datasets -i Run2_NanoAODv9/input2017.yaml -w Eurasia
fetch-datasets -i Run2_NanoAODv9/input2018.yaml -w Eurasia
```

## 2016

```
run-analysis --config Run2_NanoAODv9/config.json  --fileset Run2_NanoAODv9/input2016.json  --output outputEGM_NanoAODv9/2016 --executor dask/lxplus --scaleout 100 --memory 5GiB
```

## 2017

```
run-analysis --config Run2_NanoAODv9/config.json  --fileset Run2_NanoAODv9/input2017.json  --output outputEGM_NanoAODv9/2017 --executor dask/lxplus --scaleout 100 --memory 5GiB
```

## 2018

```
run-analysis --config Run2_NanoAODv9/config.json  --fileset Run2_NanoAODv9/input2018.json  --output outputEGM_NanoAODv9/2018 --executor dask/lxplus --scaleout 100 --memory 5GiB
```

## Post-processing
```
post-process --input-json Run2_NanoAODv9/input2016.json --output-location outputEGM_NanoAODv9/2016
post-process --input-json Run2_NanoAODv9/input2017.json --output-location outputEGM_NanoAODv9/2017
post-process --input-json Run2_NanoAODv9/input2018.json --output-location outputEGM_NanoAODv9/2018
```

```
get-unprocessed-files --input-json Run2_NanoAODv9/input2016.json --output-location outputEGM_NanoAODv9/2016 --output-json Run2_NanoAODv9/u_input2016.json
get-unprocessed-files --input-json Run2_NanoAODv9/input2017.json --output-location outputEGM_NanoAODv9/2017 --output-json Run2_NanoAODv9/u_input2017.json
get-unprocessed-files --input-json Run2_NanoAODv9/input2018.json --output-location outputEGM_NanoAODv9/2018 --output-json Run2_NanoAODv9/u_input2018.json
```

## Install local changes for postprocessing functions
```
pip install -e .
export PATH="$HOME/.local/bin:$PATH"
cd examples/SaS_ntuples
```