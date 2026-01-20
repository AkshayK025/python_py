string_a = 'Hello Elon'

# Basic String Methods 
# len(),str()
print("Basic String Methods")
print(len(string_a),
      str(string_a),
      type(string_a),
      sep='\n')

# String Case Methods
# upper(),lower(),capitalize(),title(),swapcase()
print()
print("String Case Methods")
string_a = "hello elon"

print(string_a,
    f"upper(): {string_a.upper()}",
    f"lower(): {string_a.lower()}",
    f"capitalize(): {string_a.capitalize()}",
    f"title(): {string_a.title()}",
    f"swapcase(): {string_a.swapcase()}",
    sep=",\n"
)

# Search and Find Methods
# find():,rfind():,index():,rindex():,str.endswith(suffix),str.startswith(prefix)
print()
string_b = string_a + " " + 'hello'
print(string_b)
print(f'find(hello):{string_b.find('hello')}',
      f'rfind(hello):{string_b.rfind('hello')}',
      f'index(l):{string_b.index('l')}',
      f'rindex(l):{string_b.rindex('l')}',
      f'endswith(hello):{string_b.endswith('hello')}',
      f'startswith(hello):{string_b.startswith('hello')}',
      sep='\n'
      )
