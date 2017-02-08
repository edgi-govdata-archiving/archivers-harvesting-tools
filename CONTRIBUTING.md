# Contributing Guidelines

We love improvements to our tools! To add a new tool to this repository, follow our EDGI [guidelines for contributing](https://github.com/edgi-govdata-archiving/overview/blob/master/CONTRIBUTING.md) to create a new directory for the tool on a fork or branch. 

## Directory Structure

This directory should include:
- a `UNIX man`-style README with usage instructions and also a succinct list of any dependencies (shell environment, ruby/python packages, etc.) The use-case for ht tool should also be described as well as possible. 
- a main executable file
- any other files required in order to run the tool

Please also add a brief description of the tool **and use-case** to this page.  

## Tool Specifications

Each tool should:

* set relevant global variables `path` and `base url` at the top of the script, or should provide an obvious way to set those variables through CLI arguments.
* write all harvested data to a `./data` directory
