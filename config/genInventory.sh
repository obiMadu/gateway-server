#!/bin/bash
cd ../deploy
echo $(terraform output --raw gate_ip) > ../inventory