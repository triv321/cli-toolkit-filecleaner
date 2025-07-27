#!/bin/bash

grep "HOME" sample.log | awk '{print $1}'