from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path

import fsspec

from egamma_tnp.utils.logger_utils import setup_logger

logger = setup_logger(level="INFO")



def find_missing_partitions(input_json, output_location):
    """Compares expected partitions to existing parquet files and finds missing partitions."""
    fs, token, paths = fsspec.get_fs_token_paths(output_location)
    new_input_json = {}

    for dataset, data in input_json.items():
        output_folder_name = dataset.lstrip("/").replace("/", "_")
        dataset_output_path = f"{output_location}/{output_folder_name}/get_ntuples_1/"
        report = dataset_output_path + "report.json"

        # get full paths then take only the file names
        list_of_output_files = fs.find(dataset_output_path, withdirs=False)
        file_names = [Path(p).name for p in list_of_output_files]
        files_already_processed = [file for file in file_names if not file.startswith("NTuples-part") and file.endswith(".parquet")]
        files_to_reprocess = {}
        list_of_files = data.get("files", {})
        for k, v in list_of_files.items():
            k_store = k.split("/")[-1].replace(".root", "")
            match = all((k_store not in p) for p in files_already_processed)
            if match:
                files_to_reprocess[k] = v

        # preserve same structure: files (kept) and metadata (copied)
        if files_to_reprocess:
            new_input_json[dataset] = {
                "files": files_to_reprocess,
                "metadata": data.get("metadata", {})
            }
            logger.info(f"Out of the {len(list_of_files)} files specified for dataset '{dataset}' in json file, {len(list_of_files) - len(files_to_reprocess)} were fully processed. ")
        else:
            logger.info(f"All {len(list_of_files)} files specified for dataset '{dataset}' in json file were fully processed. ")
    # write output JSON (same top-level structure, only failed files kept)

    return new_input_json


def main():
    parser = argparse.ArgumentParser(description="Find missing parquet partitions in datasets.")
    parser.add_argument("--input-json", type=str, required=True, help="Path to input JSON file.")
    parser.add_argument("--output-location", type=str, required=True, help="Base output location for checking partitions.")
    parser.add_argument("--output-json", type=str, default="missing_partitions.json", help="Path to save missing partitions JSON.")
    args = parser.parse_args()

    # Load input JSON
    with fsspec.open(args.input_json, "r") as f:
        input_json = json.load(f)

    # Find missing partitions
    missing_files = find_missing_partitions(input_json, args.output_location)

    if not missing_files:
        logger.info("All samples were fully processed. Output file will not be created.")

    else:
        logger.info(f"Output file will be saved in {args.output_json}.")

        # Save output
        with fsspec.open(args.output_json, "w") as f:
            json.dump(missing_files, f, indent=4)


if __name__ == "__main__":
    main()
