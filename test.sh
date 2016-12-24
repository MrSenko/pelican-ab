#!/bin/bash

flake8 pelican_ab/ tests/ && \
pylint -rn pelican_ab tests/*.py && \
coverage run --source pelican_ab/ --branch -m unittest discover tests -v && \
coverage report -m
