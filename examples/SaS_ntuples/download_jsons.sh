mkdir jsons

#Download 2022 golden JSON and pileup JSON
curl https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions22/Cert_Collisions2022_355100_362760_Golden.json -o jsons/Cert_Collisions2022_355100_362760_Golden.json
cp /cvmfs/cms-griddata.cern.ch/cat/metadata/LUM/Run3-22CDSep23-Summer22-NanoAODv12/latest/puWeights.json.gz jsons/puWeights_2022.json.gz
cp /cvmfs/cms-griddata.cern.ch/cat/metadata/LUM/Run3-22EFGSep23-Summer22EE-NanoAODv12/latest/puWeights.json.gz jsons/puWeights_2022EE.json.gz

#Download 2023 golden JSON and pileup JSON
curl https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions23/Cert_Collisions2023_366442_370790_Golden.json -o jsons/Cert_Collisions2023_366442_370790_Golden.json
cp /cvmfs/cms-griddata.cern.ch/cat/metadata/LUM/Run3-23CSep23-Summer23-NanoAODv12/latest/puWeights.json.gz jsons/puWeights_2023.json.gz
cp /cvmfs/cms-griddata.cern.ch/cat/metadata/LUM/Run3-23DSep23-Summer23BPix-NanoAODv12/latest/puWeights.json.gz jsons/puWeights_2023BPix.json.gz


# Download 2024 golden JSON and pileup JSON
curl https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions24/Cert_Collisions2024_378981_386951_Golden.json -o jsons/Cert_Collisions2024_378981_386951_Golden.json
cp /afs/cern.ch/user/p/pagaigne/public/pileup_jsons/puWeights_2024.json.gz jsons/puWeights_2024.json.gz

# Download 2016, 2017, 2018 golden JSON and pileup JSONs
curl https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions16/13TeV/Legacy_2016/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt -o jsons/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt
cp /cvmfs/cms-griddata.cern.ch/cat/metadata/LUM/Run2-2016preVFP-UL-NanoAODv9/2021-09-10/puWeights.json.gz jsons/puWeights_2016preVFP.json.gz
cp /cvmfs/cms-griddata.cern.ch/cat/metadata/LUM/Run2-2016postVFP-UL-NanoAODv9/2021-09-10/puWeights.json.gz jsons/puWeights_2016postVFP.json.gz
curl https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions17/13TeV/Legacy_2017/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt -o jsons/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt
cp /cvmfs/cms-griddata.cern.ch/cat/metadata/LUM/Run2-2017-UL-NanoAODv9/2021-09-10/puWeights.json.gz jsons/puWeights_2017.json.gz
curl https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions18/13TeV/Legacy_2018/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt -o jsons/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt
cp /cvmfs/cms-griddata.cern.ch/cat/metadata/LUM/Run2-2018-UL-NanoAODv9/2021-09-10/puWeights.json.gz jsons/puWeights_2018.json.gz


  