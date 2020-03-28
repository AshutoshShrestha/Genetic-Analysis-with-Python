from matplotlib import pyplot as pylab
import random

correctInput = False
while not correctInput:
	motif = input("Motif: ")
	for i in range(len(motif)):
		if(motif[i] != "A" and motif[i] != "T" and motif[i] != "C" and motif[i] != "G"):
			correctInput = False
			print("Invalid nucleotide in the motif. Try entering again.")
			break 
		else:
			correctInput = True

correctInput = False
while not correctInput:
	print("Enter frequencies for each nucleotide in genome: ")
	freqA = int(input("A: "))
	freqT = int(input("T: "))
	freqC = int(input("C: "))
	freqG = int(input("G: "))

	if freqA + freqT + freqC + freqG == 100:
		correctInput = True
	else:
		print("Frequencies don't add up to a 100. Try again.")

N = len(motif)
Probability = 1

for i in range(N):
	if motif[i] == "A":
		Probability *= freqA/100
	elif motif[i] == "C":
		Probability *= freqC/100
	elif motif[i] == "T":
		Probability *= freqT/100
	else:
		Probability *= freqG/100

print("Probability of appearing in a sequence N =", N, "is", Probability, "(", Probability*100, "%)")

probabilities = []

for i in range(N, 5000):
	probabilities.append(1-(1-Probability)**i)


pylab.figure("Plot of probability of finding at least one of these motifs in a sequences of length N to 5,000")
pylab.plot(range(N, 5000), probabilities)
pylab.ylabel("Plot of probability of finding at least one of these motif")

avgExpectedMotifs = []
sequenceLength = [100,1000,2000,5000,10000]
for i in sequenceLength:
	expectedMotifs = []
	for j in range(100):
		sequence=""
		for z in range(i):
			randomNum = random.random()*100
			if randomNum < freqA:
				sequence += "A"
			elif randomNum >= freqA and randomNum < freqA+freqT:
				sequence += "T"
			elif randomNum >=freqA+freqT and randomNum < freqA+freqT+freqC:
				sequence += "C"
			else:
				sequence += "G"
		i = 0
		count = 0
		while i < (len(sequence)-(N-1)):
			if motif == sequence[i:i+N]:
				count += 1
				i += N
			else:
				i += 1
		expectedMotifs.append(count)
	avgExpectedMotifs.append(sum(expectedMotifs)/100)

pylab.figure("Expected number of motifs in sequences of length N = 100, N = 1000, N = 2000, N = 5000, and N = 10000")
pylab.scatter(sequenceLength, avgExpectedMotifs) 
pylab.show()