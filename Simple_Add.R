
# commandArgs will ingest arguments from the command line
x <- commandArgs(trailingOnly = TRUE)

# Convert to numerics and manipulate
nums <- as.numeric(x)
total <- sum(nums)

# Return the value to command line
cat(total)