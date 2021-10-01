# ggv2provisioner

Callable package and command line to download, install and provision AWS IoT Greengrass

## Commands

The provisioner can perform different functions by running the following commands:

- `ggv2provisioner install` - Download (optional) and install Greengrass on the local system.
- `ggv2provisioner provision` - Create and obtain all cloud resources then provision Greengrass locally for first run
- `ggv2provisioner clean` - Clear current state of Greengrass identity and any targeted resources on the local system.
- `ggv2provisioner describe` - Create configuration of all cloud and local resources for the Greengrass core device
