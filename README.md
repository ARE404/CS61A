# CS61A
homework,projects,labs for CS61A learning

## parsons issues
Don't know why parsons didn't work for me every first time, eventually I found out there is a problem with $lab(hw)/parsons/werkzeug/serving.py$, so I made an avalible corrected version in $CS61A/fixed serving file/serving.py$
If you have the same issue, just copy this verison to replace the original.
$cp ../../fixed\ serving\ file/serving.py "$(pwd)/parsons/werkzeug"$
