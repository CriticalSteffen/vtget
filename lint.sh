#!/bin/bash

paths="vtget.py"
isort $paths
black -l 79 $paths
pycodestyle $paths
pydocstyle $paths
for p in $(echo $paths); do
    pylint $p
done