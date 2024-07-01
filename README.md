# Turing-Machine


## Description
This project focuses on the design and simulation of a Universal Turing Machine. It uses universal numbers to generate and decode rules that determine the machine's behavior based on the symbol read and the current state. The goal is to demonstrate how a Universal Turing Machine can simulate any other Turing machine, thus establishing theoretical limits on computability.

## Project Content
- **Introduction to Turing Machines:** Explanation of the basic concept and operation of a Turing Machine, including the infinite tape, the read/write head, the states, and the transition function.
- **Universal Turing Number:** Use of the universal number to represent a complete description of a Universal Turing Machine and its conversion to binary.
- **Rule Generation:** Process of adding substrings to the binary string and applying substitution rules to generate the machine's actions.
- **Simulation Algorithms:** Implementation of algorithms for symbol substitution and obtaining instructions from the generated rules.
- **Validation and Examples:** Practical examples of simulation using different numbers to demonstrate the functionality and accuracy of the Universal Turing Machine.

## Code Structure
The code is organized into functions that allow:
- Converting numbers to their binary representation.
- Adding substrings to the binary string.
- Generating and applying substitution rules.
- Obtaining instructions from the rules.
- Simulating the behavior of the Universal Turing Machine.

## Code Explanation
- **Universal Turing Number:** The universal number `7244855335339317577198395039615711237952360672556559631108...` is converted to its binary representation.
- **Binary Conversion:** The number is converted to binary, and substrings `110` are added at the beginning and end of the binary string.
- **Substitution Rules:** The code defines substitution rules in a dictionary, where each rule specifies how to replace symbols on the tape.
- **Rule Application:** The function `convert_bin_maq` takes the binary machine and applies the substitution rules to generate a sequence of symbols.
- **Instruction Generation:** The function `obtener_reglas` generates a list of instructions based on the symbols obtained from the previous step.
- **Universal Turing Machine Simulation:** The function `MUT` simulates the behavior of the Universal Turing Machine by processing the input tape and applying the instructions to move the read/write head and update the tape.
- **Validation:** The code includes validation examples using different numbers to demonstrate the correctness of the Universal Turing Machine simulation.

## References
- Penrose, R. (1990). *The Emperor’s New Mind: Concerning Computers, Minds, and the Laws of Physics*. Oxford University Press.
- Russell, S., & Norvig, P. (2016). *Artificial Intelligence: A Modern Approach*. Pearson.
- Bostrom, N. (2014). *Superintelligence: Paths, Dangers, Strategies*. Oxford University Press.
- Hofstadter, D. R. (1979). *Gödel, Escher, Bach: An Eternal Golden Braid*. Basic Books.
