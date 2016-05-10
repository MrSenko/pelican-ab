#!/bin/bash

flake8 pelican_ab/ tests/ && \
coverage run --source pelican_ab/ --branch -m unittest discover tests -v && \
coverage report -m
