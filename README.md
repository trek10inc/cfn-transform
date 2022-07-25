<p align="center">
</p>

# CFN-TRANSFORM

## Installation and Quick Start
### Pre-Requisites
- `cfn-transform` requires python 3.7 or greater 
- `cfn-transform` is installed via pip
### Installation
The recommended and tested way fo installing cfn-transform is via pip. 

cfn-transform can be installed using the following command: 
```
pip install cfn-transform
```

### Quick Usage 
Once you have your cfn-transform installed, you are now free to utilize our PyPi.

Run either of the following commands to view our current supported options for cfn-transform.

```
cfn-transform --help
```
## Overview
### What is cfn-transform
Cfn-transform is a command-line utility used to return transformed SAM templates.

With cfn-transform , you are able to return a fully transformed SAM template either to the command line or directly to a file. Unlike other tools for returning transformed files, cfn-transform does not require any AWS credentials and can be ran locally on your machine. 
### How does it work? 
Cfn-transform works by utilizing the functionality of the decode command within `cfn-lint`. The current linter creates the transformed template using `aws-sam-cli.samtranslator` and checks it to make sure that it is a valid template. Cfn-transform uses the same translator, and returns it to be displayed for the user. Similarly to the process used in cfn-lint, the current library returns a default transformation for the region `us-east-1`. 

### Features
**Commands currently supported :**
```
cfn-transform [example.json]
cfn-transform [example.yaml]
```
*Base command to return transformed to command line* 

**Command Options currently supported :**
```
cfn-transform [example.json] -f [text.txt]
cfn-transform [example.yaml] --file [text.txt]
```
*Option to attach to return transformed to a specified text file*
