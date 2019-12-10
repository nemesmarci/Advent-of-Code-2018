from common import Processor

processor = Processor()
processor.registers[0] = 1

# The input program calculates a large number and then sums its factors.
# Once it calculated the number, the instruction pointer will be at 0.
# At this point we can sum the factors ourselves.

processor.run(return_early=True)
num = max(processor.registers)
print(sum((i for i in range(1, num + 1) if num % i == 0)))
