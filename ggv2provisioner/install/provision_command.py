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


def provision_greengrass(install_dir: str):
    """Provision Greengrass either via new or existing resources"""
    # pre-flight
    # is greegrass installed?
    # is greengrass pre-configured and override set to false?
    # is greengrass running?

    # provision resources - for each resource:
    #   if creating:
    #       does resource already exist?
    #       create resource and download assets or capture arn
    #   else if referencing - for each resource:
    #       does resource exist?
    #       if local resource, is it available and valid?
    #       validate arns or resource
    #   capture other details needed:
    #       iot data endpoint
    #       region
    #       cred provider endpoint
    # Create config.yaml and run --init to reset

    print(f"Greengrass successfully installed in {install_dir}")
    return
