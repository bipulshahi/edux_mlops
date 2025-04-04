import sys
import pathlib

print()
print(pathlib.Path(__file__))
print()
print(pathlib.Path(__file__).resolve())
print()
print(pathlib.Path(__file__).resolve().parents[1])
print()
print(pathlib.Path(__file__).resolve().parents[0])