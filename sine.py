import math
import sys

SAMPLEFREQUENCY = 192000
AUDIOFREQUENCY = 1000
AUDIOBITS = 24
MEMORYBITS = 32

def tc (val):
	if val >= 0:
		return val
	else:
		maximum = int("0xFFFFFF", 16)	# We are calculating with 24 Bit
		return maximum + val + 1		# It should be "maximum - val + 1"
										# val should be subtracted from the maximum
										# But according to the IF-Loop we only get negative values
										# So we add them.


# for norm in range(0,1920):
# 	print(norm, norm / 1919, math.sin(2*math.pi*norm/1919), math.sin(2*math.pi*norm/1919) * 8388608, twos_complement(math.sin(2*math.pi*norm/1919) * 8388608) )

print("Samplefrequency: ", SAMPLEFREQUENCY, "Hz")
print("Audiofrequency: ", AUDIOFREQUENCY, "Hz")
samples = (1/AUDIOFREQUENCY) / (1/SAMPLEFREQUENCY)	# Calculate the number of samples needed for one loop
													# FIXME check if the result of the division is not integer. As soon as any decimal places exist
													# the program will not work.
samples = int(samples)								# Convert to integer
print(samples, "samples needed.")
print(samples * MEMORYBITS, "kBit needed.")		# FIXME If the memory needed is bigger than the 36k the Spartan-7 has there should be at least a warning.

x = []
y = []
twos = []										# Create a list

for var in range(0, samples):
	x.append(var)								# Backup var for display on the x-axis
	var = var / samples							# Normalize var between 0 and 1
	var = math.sin(2*math.pi*var)				# Generate a sine between -1 and 1
	var = round(var * 2 ** (AUDIOBITS-2), 0)	# Scale up to the maximum amplitude of AUDIOBITS.
												# It's AUDIOBITS-2, because the sine goes from -1 to +1
	y.append(var)								# Make a Backup
	var = int(var)								# Convert to integer
	var = tc(var)								# Convert to Two's complement
	var = hex(var)								# Convert from int to string
	var = var.replace("0x","")					# Delete "0x"
	var = var.replace("-","")					# Delete "-"
	var = var.rjust(8,"0")						# Stuff with zeroes
	twos.append(var)							# Append to the list
print(twos)

zeilen = int(samples / 8)						# The destination text file will get 8 samples per line

file = open(f'table_{AUDIOFREQUENCY}.txt','w')	# FIXME Please, some basic error check...

for outer in range(0, zeilen):
	addr_hex = hex(outer)
	addr_hex = addr_hex.replace("0x", "")
	addr_hex = addr_hex.rjust(2, "0")	
	file.write(f'INIT_{addr_hex} => X"')
	for inner in reversed(range(8)):
		file.write(twos[outer*8+inner])
	file.write("\",\n")

file.close						