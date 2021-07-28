from string import ascii_letters


def range_alpha(start_letter, end_letter):
  return ascii_letters[
    ascii_letters.index(start_letter):ascii_letters.index(end_letter) + 1
  ]

print(range_alpha('a', 'z'))
print(range_alpha('A', 'Z'))
print(range_alpha('a', 'Z'))