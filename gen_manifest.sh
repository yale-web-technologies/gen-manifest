#!/bin/sh

export GEN_MANIFEST_HOME="$(cd "$(dirname "${BASH_SOURCE[0]}")/" && pwd)"

files_file=$1
config_file=$2

$GEN_MANIFEST_HOME/gen_manifest.py $files_file $config_file
