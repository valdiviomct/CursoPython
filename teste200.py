creature_names = ['Sammy', 'Ashley', 'Jo', 'Olly', 'Jackie', 'Charlie']

def names_vowels(x):
  return x[0].lower() in 'aeiou'

filtered_names = filter(names_vowels, creature_names)

print(list(filtered_names))