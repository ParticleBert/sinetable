# sinetable - generates a sinetable block ram for xilinx FPGAs

This python-code generates a textfile containing a sinetable, which can be pasted into the VHDL-Initialization of a XILINX Blockram.

Four parameters can be setup:
* SAMPLEFREQUENCY: In Hz. Can be 44100, 48000, 192000 etc. This is the target samplefrequency the system will run with.
* AUDIOFREQUENCY: In Hz. Can be 100, 500 etc.
* AUDIOBITS: How many bits do you use in your audio transmission? In my example it is 24.
* MEMORYBITS: How wide is the memory bus of your Block RAM? In my example it is 32

I have used this code with an audiofrequency of 200 and 1000Hz, a samplefrequency of 192.000Hz, 24 Audio- and 32 Memorybits. The code generates a file called *table_**audiofrequency**.txt*
  
I have omitted a lot of clean programming paradigms. I was more interested in the result. Sorry for this.
* There should be a basic check if the textfile can be opened.
* The function calculating the needed *samples* should check if there is a remainder. If you need a 1000Hz-Sine with a frequency of 192kHz it is straightforward: You need 192 samples. If you need a 1005Hz-Sine with a frequency of 192kHz you need 192.04 samples. This is a problem. At the moment the decimal .04 will be cut without comment
* If the number of samples exceeds the BRAM-Sizes of 18k or 36k the code should mention this.
* The text manipulation from the STRING to put it into the textfile does not take into consideration the parameters AUDIOBITS and MEMORYBITS. At the moment it is hard coded to stuff 24 audiobits in 32 memorybits.
