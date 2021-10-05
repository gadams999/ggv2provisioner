"""
    Amazon.com, Inc.

License:
    Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

    Licensed under the Apache License, Version 2.0 (the "License"). You may not use 
    this file except in compliance with the License. A copy of the License is located at

        http://aws.amazon.com/apache2.0/

    or in the "license" file accompanying this file. This file is distributed on an "AS IS" 
    BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the 
    License for the specific language governing permissions and limitations under the License.
"""

import os
import subprocess
import zipfile
import tempfile
import validators
import requests
from pathlib import Path


def install_greengrass(source: str, target_dir: Path, system_setup: str):
    """Install Greengrass from locally available zip file or download from URL

    :param source: Greengrass installation zipfile or URL to download
    :type source: str
    :param target_dir: Path where to install Greengrass
    :type target_dir: str
    :param system_setup: Inform Greengrass setup to create systemd
    :type system_setup: str
    """

    print(f"Stating installation of Greengrass from: {source}")
    # validate file and uncompress into install dir
    with tempfile.TemporaryDirectory() as install_dir:
        if not validators.url(source) and Path(source).is_file():
            # Reference local file (zip or Greengrass.jar)
            source_file = Path(source)
            print(f"Using file {source_file} as source")
        elif validators.url(source):
            # Otherwise download from URL
            source_file = Path(tempfile.gettempdir(), source.split("/")[-1])
            try:
                results = requests.get(source)
                with open(source_file, "wb") as f:
                    f.write(results.content)
            except:
                print(f"Error: {source} is not a valid source URL")
                raise SystemExit(1)
        else:
            # Not a file and not a validator
            print(f"Installation source: {source} does not exist")
            raise SystemExit(1)

        # check if zip file
        if zipfile.is_zipfile(source_file):
            zipfile.ZipFile(source_file).extractall(install_dir)
        else:
            print(f"{source} is not a valid zip file")
            raise SystemExit(1)

        # Run base installation, overrides existing setup
        command: list = [
            "java",
            f"-Droot={target_dir}",
            "-jar",
            os.fspath(Path(".", install_dir, "lib", "Greengrass.jar")),
            "--provision",
            "false",
            "--setup-system-service",
            system_setup,
            "--start",
            "false",
        ]
        command_results = subprocess.run(command, capture_output=True)
        if command_results.returncode != 0:
            print(f"Error installing Greengrass with command: {' '.join(command)}")
            print(f"Install command output:\n{command_results.stderr.decode()}")
            raise SystemExit(1)

    # if file, decompress if needed and verify Greengrass.jar included

    # else if URL, download and decompress
    print(f"Greengrass successfully installed in {install_dir}")
    return
