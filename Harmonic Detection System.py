# Harmonic-Detection-System
## Harmonic Detection System — Simple Python Program

This beginner-level program calculates the **fundamental frequency** and detects harmonic frequencies in an electrical signal.

```
frequency = float(input("Enter fundamental frequency (Hz): "))
harmonic = int(input("Enter harmonic number: "))

harmonic_frequency = frequency * harmonic

print("Fundamental Frequency =", frequency, "Hz")
print("Harmonic Number =", harmonic)
print("Harmonic Frequency =", harmonic_frequency, "Hz")

if harmonic == 1:
    print("No harmonic detected")
else:
    print("Harmonic detected")
```

### Example Output

```
Enter fundamental frequency (Hz): 50
Enter harmonic number: 3

Fundamental Frequency = 50.0 Hz
Harmonic Number = 3
Harmonic Frequency = 150.0 Hz
Harmonic detected
```

### Detect multiple harmonics

```
frequency = float(input("Enter fundamental frequency (Hz): "))

print("\nHarmonic Frequencies:")

for n in range(1, 6):
    harmonic_frequency = frequency * n
    print("Harmonic", n, "=", harmonic_frequency, "Hz")
```

**Example:**

```
Enter fundamental frequency (Hz): 50

Harmonic Frequencies:
Harmonic 1 = 50.0 Hz
Harmonic 2 = 100.0 Hz
Harmonic 3 = 150.0 Hz
Harmonic 4 = 200.0 Hz
Harmonic 5 = 250.0 Hz
```

**Project name:** Harmonic Detection System **Electrical concept:** Harmonics in AC power systems **Python concepts:** `input()`, variables, multiplication, `if-else`, and `for` loop.
