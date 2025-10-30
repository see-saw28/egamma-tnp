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
cp /afs/cern.ch/user/p/pagaigne/public/pileup_jsons/puWeights_2024.json.gz jsons/
