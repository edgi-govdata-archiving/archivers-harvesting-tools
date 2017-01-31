# harvesting-tools
A collection of code snippets designed to be dropped into the data harvesting process directly after generating the zip starter kit

## Usage

- Familiarize yourself with the [harvesting instructions](https://github.com/datarefugephilly/workflow/tree/master/harvesting-toolkit) in the Data Rescue workflow repo.  Within the [pipeline app](http://harvest-pipeline.herokuapp.com/), click `Download Zip Starter` from the page related to a URL that you have checked out. 
- unzip the zipfile
- Choose a tool that seems likely to be helpful in capturing this particular resource, and copy the contents of its directory in this repo to the `tools` directory, e.g. with:
  ```
  cp -r harvesting-tools/TOOLNAME/* RESOURCEUUID/tools/
  ```
- Adjust the base URL for the resource along with any other relevant variables, and tweak the content of the tool as necessary
- After the resource has been harvested, proceed with the further steps in the [workflow](https://github.com/datarefugephilly/workflow/). 

## Contributing

To add a new tool to this repository, clone or branch the repo and create a new directory for the tool. This directory should include:
- a `UNIX man`-style README with usage instructions and also a succinct list of any dependencies (shell environment, ruby/python packages, etc.)
- a main executable file
- any other files required in order to run the tool

### Tool Specifications

Each tool should:
* set relevant global variables `path` and `???` in an immediately obvious way at the top of the script, or should provide an obvious way to set those variable through CLI arguments.
* write all harvested data to a `../data` directory

I guess it would be cool if tools ALL read the relevant variables from a `paths.txt` or `url.txt` file. Then potentially users wouldn't have to modify the tools at all -- the `zip starter` could write the URL to the appropriate location, and the user could immediately run the script. 


