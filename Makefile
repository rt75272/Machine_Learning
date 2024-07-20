# -----------------------------------------------------------------------------
# Makefile
#
# Bash automation.
#
# Usage:
#   $ make <target>
# -----------------------------------------------------------------------------

# Run all regressor.
all: linear polynomial

# Run linear regression.
linear:
	@echo "\nRunning linear regression..."
	@python3 linear_reg.py

# Run polynomial regression.
polynomial:
	@echo "\nRunning polynomial regression..."	
	@python3 polynomial_reg.py