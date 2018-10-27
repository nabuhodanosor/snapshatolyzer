# snapshatolyzer
Project to manage AWS EC2 instance snapshots

## About

This project is a test, and uses boto3 to manage AWS EC2 instance snapshots.

## Configuration

snappy uses the configuration file created by the AWS cli

`aws configure --profile snappy`

## Running

`pipenv run "python snappy.py"`

*command* is list, start, or stop
*project* is optional
