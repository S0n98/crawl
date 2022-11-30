#!/bin/bash
export PIPENV_VERBOSITY=-1

if [[ $PIPENV_ACTIVE != 1 ]]; then
  pipenv shell
fi