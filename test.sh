#!/bin/bash

flake8 pelican_ab/ && \
coverage run --source pelican_ab/ --branch -m unittest -v pelican_ab.tests && \
coverage report -m
