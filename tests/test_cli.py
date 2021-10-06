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


# Install commands
def test_cli_install_no_params():
    """Install command uses default valid URL for source and attempt install in /greengrass/v2"""
    runner = CliRunner()
    result = runner.invoke(cli, ["install"])
    assert result.exit_code == 1
    assert (
        "java.lang.RuntimeException: Cannot create all required directories"
        in result.output
    )


def test_cli_install_temp(tmpdir):
    """Install from default URL to temp directory w/o system setup"""
    runner = CliRunner()
    result = runner.invoke(
        cli,
        args=[
            "install",
            "--target",
            tmpdir,
            "--system-setup",
            "false",
        ],
    )
    assert result.exit_code == 0
    assert "Greengrass successfully installed in" in result.output


def test_cli_install_invalid_source_zip_file(tmpdir):
    """Source set to local file zip file, but not the Greengrass one"""
    runner = CliRunner()
    result = runner.invoke(
        cli,
        args=[
            "install",
            "--source",
            "tests/data/greengrass-nucleus-latest.zip",
            "--target",
            tmpdir,
        ],
    )
    print(result.output)
    assert result.exit_code == 1
    assert "Unable to access jarfile" in result.output


def test_cli_install_source_not_zip_file():
    """Source set to local non-zip file"""
    runner = CliRunner()
    result = runner.invoke(
        cli,
        [
            "install",
            "--source",
            "tests/test_cli.py",
            "--target",
            "/tmp",
        ],
    )
    assert result.exit_code == 1
    assert "is not a valid zip file\n" in result.output


def test_cli_file_does_not_exist():
    """Source set to invalid"""
    runner = CliRunner()
    result = runner.invoke(
        cli,
        [
            "install",
            "--source",
            "file_does_not_exist",
            "--target",
            "/tmp",
        ],
    )
    assert result.exit_code == 1
    assert "Installation source: file_does_not_exist does not exist\n" in result.output


def test_cli_invalid_source(tmpdir):
    """File does not exist at URL"""
    runner = CliRunner()
    result = runner.invoke(
        cli,
        [
            "install",
            "--source",
            "https://asdfasfasfasfasgdfgas.com/file.zip",
            "--target",
            tmpdir,
        ],
    )
    assert result.exit_code == 1
    assert "Invalid download URL" in result.output


# Provision commands
#
# Init config file values
#               Create  reference
# thing         todo    todo
# certificate   todo    todo
# IoT policy    todo    todo
# Role alias    todo    todo
#  IAM role     todo    todo
# For all:
#  iot endpoint
#  credential provider endpoint
#
# options
#  --override config
#  --access-key
#  --secret-access-key
#  --credential-provider-endpooint
#  --certificate
#  --private-key