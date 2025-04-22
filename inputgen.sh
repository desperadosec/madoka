honggfuzz -i input -o output -x -- ./wrapper ___FILE___
# This should generate inputs that also crash
# TODO: Modify the line to save non-unique inputs as well
# We want to go for speed and volume over any uniqueness

