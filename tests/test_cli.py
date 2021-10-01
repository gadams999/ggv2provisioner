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

import pytest
import os
from click.testing import CliRunner
from ggv2provisioner.cli import cli


def test_execute_cli_no_params():
    runner = CliRunner()
    result = runner.invoke(cli, "")
    assert result.exit_code == 0
    assert (
        result.output
        == "Usage: cli [OPTIONS] COMMAND [ARGS]...\n\nOptions:\n  --help  Show this message and exit.\n\nCommands:\n  install\n"
    )


def test_cli_install_no_params():
    """Install command should return help text"""
    runner = CliRunner()
    result = runner.invoke(cli, "install")
    assert result.exit_code == 2
    assert (
        "Usage: cli install [OPTIONS]\nTry 'cli install --help' for help.\n"
        in result.output
    )


def test_cli_install_source_file():
    """Source set to local file"""
    runner = CliRunner()
    result = runner.invoke(
        cli, "install --source tests/data/greengrass-nucleus-latest.zip, --target /tmp"
    )
    assert result.exit_code == 0
    assert "Greengrass successfully installed in /greengrass/v2\n" in result.output


# test install from valid url - correct one
# test install from invalid url
# test install from valid url - incorrect content