#!/bin/bash

flake8 pelican_ab/ && \
coverage run --source pelican_ab/ --branch -m unittest discover pelican_ab/tests -v && \
coverage report -m
