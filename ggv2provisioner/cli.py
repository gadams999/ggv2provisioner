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

import click
from .install import install_command


@click.group()
def cli() -> None:
    pass


@cli.command()
@click.option(
    "-s",
    "--source",
    required=True,
    default="https://d2s8p88vqu9w66.cloudfront.net/releases/greengrass-nucleus-latest.zip",
)
@click.option("-t", "--target", required=True, default="/greengrass/v2")
def install(source, target):
    install_command.install_greengrass(source=source, target_dir=target)


if __name__ == "__main__":
    cli()