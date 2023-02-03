#!/bin/bash

gunicorn -w 1 --access-logfile access.log --error-logfile error.log -b localhost:8070 getID:app

