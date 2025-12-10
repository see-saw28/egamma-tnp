from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path

import fsspec

from egamma_tnp.utils.logger_utils import setup_logger

logger = setup_logger(level="INFO")

def postprocess_files(input_json, output_location, dry_run):
    """Compares expected partitions to existing parquet files and finds missing partitions."""
    fs, token, paths = fsspec.get_fs_token_paths(output_location)
    
    for dataset in input_json.keys():
        logger.info(f"Post-processing dataset: {dataset}")
        output_folder_name = dataset.lstrip("/").replace("/", "_")
        dataset_output_path = f"{output_location}/{output_folder_name}/get_ntuples_1/"
        report = dataset_output_path + "report.json"
        # get full paths then take only the file names
        list_of_output_files = fs.find(dataset_output_path, withdirs=False)

        new_files = [file for file in list_of_output_files if Path(file).name.startswith("NTuples-part") and file.endswith(".parquet")]
        correct_files = [file.replace('.parquet','') for file in list_of_output_files if not Path(file).name.startswith("NTuples-part") and file.endswith(".parquet")]

        # collect report
        try:
            with fs.open(report, "r") as fh:
                report_json = json.load(fh)
        except Exception as e:
            logger.error(f"Could not open report file {report}: {e}")
            continue

        FILES = []
        success_count = 0
        failed_count = 0

        if new_files:
            for idx, file_report in enumerate(report_json):
                # map report entry to corresponding NTuples output (if available)
                file_name = new_files[idx] if idx < len(new_files) else None

                path_full = file_report.get("args", [None])[0]
                uuid = None
                if path_full:
                    uuid = Path(str(path_full).strip("'")).name

                if file_report.get("exception") is None:
                    # successful input -> try to rename corresponding NTuples file
                    if file_name:
                        try:
                            new_name = "NTuples-" + Path(str(path_full).strip("'")).name.replace(".root", ".parquet")
                            dest = str(Path(file_name).with_name(new_name))
                            if dry_run:
                                pass
                            elif hasattr(fs, "mv"):
                                fs.mv(file_name, dest)
                            elif hasattr(fs, "rename"):
                                fs.rename(file_name, dest)
                            else:
                                raise RuntimeError("filesystem has no mv/rename method")
                            success_count += 1
                            FILES.append({"file": file_name, "status": "renamed", "uuid": uuid})
                        except Exception as e:
                            failed_count += 1
                            FILES.append({"file": file_name, "status": "rename_failed", "error": str(e), "uuid": uuid})
                    else:
                        failed_count += 1
                        FILES.append({"file": None, "status": "missing_output_for_success", "uuid": uuid})
                else:
                    # failed input -> try to remove corresponding NTuples file
                    if file_name:
                        try:
                            if dry_run:
                                pass
                            elif hasattr(fs, "rm"):
                                fs.rm(file_name)
                            elif hasattr(fs, "delete"):
                                fs.delete(file_name)
                            elif hasattr(fs, "remove"):
                                fs.remove(file_name)
                            else:
                                raise RuntimeError("filesystem has no rm/delete/remove method")
                            failed_count += 1
                            FILES.append({"file": file_name, "status": "deleted", "uuid": uuid})
                        except Exception as e:
                            failed_count += 1
                            FILES.append({"file": file_name, "status": "delete_failed", "error": str(e), "uuid": uuid})
                    else:
                        failed_count += 1
                        FILES.append({"file": None, "status": "failed_no_output", "uuid": uuid})
            
            total = success_count + failed_count
            logger.info(f"Files already processed: {len(correct_files)}, Total new files processed: {total}  succeeded: {success_count}  failed : {failed_count}")
        else:
            logger.info(f"Files already processed: {len(correct_files)}, no new files to process.")
        # print only final summary


def main():
    parser = argparse.ArgumentParser(description="Find missing parquet partitions in datasets.")
    parser.add_argument("--input-json", type=str, required=True, help="Path to input JSON file.")
    parser.add_argument("--output-location", type=str, required=True, help="Base output location for checking partitions.")
    parser.add_argument("--dry", action="store_true", help="Enable dry run mode (no changes will be made).")
    args = parser.parse_args()

    # Load input JSON
    with fsspec.open(args.input_json, "r") as f:
        input_json = json.load(f)

    # Find missing partitions
    postprocess_files(input_json, args.output_location, args.dry)




if __name__ == "__main__":
    main()
