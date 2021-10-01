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

import subprocess
import zipfile
import tempfile
import validators
import requests
from pathlib import Path


def install_greengrass(source: str, target_dir: Path):
    """Install Greengrass from locally available zip file or download from URL

    :param source: Greengrass installation zipfile or URL to download
    :type source: str
    :param target_dir: Path where to install Greengrass
    :type source: str
    """

    # validate file and uncompress into install dir
    with tempfile.TemporaryDirectory() as install_dir:
        source_file: Path
        if not validators(source) and Path(source).is_file:
            # Reference local file (zip or Greengrass.jar)
            source_file = Path(source)

        elif validators(source):
            # Otherwise download from URL
            source_file = Path(tempfile.gettempdir(), source.split("/")[-1])
            try:
                results = requests.get(source)
                with open(source_file, "wb") as f:
                    f.write(results.content)
            except:
                print("no bueno")
        else:
            # Not a file and not a validator
            print(f"Installation file {source} does not exist")
            raise SystemExit(2)

        # check if zip file
        if zipfile.is_zipfile(source_file):
            zipfile.ZipFile(source_file).extractall(install_dir)
        else:
            print(f"{source} is not a valid zip file")
            raise SystemExit(2)

    # Verify java is available
    try:
        result = subprocess.run(["java", "-version"], capture_output=True)
    except FileNotFoundError as e:
        print(
            "ERROR - Java not found on path. Java required to install and run Greengrass."
        )
        raise SystemExit(2)

    # if file, decompress if needed and verify Greengrass.jar included

    # else if URL, download and decompress
    print("Greengrass successfully installed in /greengrass/v2")
    return
