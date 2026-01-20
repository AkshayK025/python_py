string_a = 'Hello Elon'

# Basic String Methods 
# len(),str()
print("Basic String Methods")
print(len(string_a),
      str(string_a),
      type(string_a),
      sep='\n')

# String Case Methods
print()
print("String Case Methods")
string_a = "hello elon"

print(
    f"upper(): {string_a.upper()}",
    f"lower(): {string_a.lower()}",
    f"capitalize(): {string_a.capitalize()}",
    f"title(): {string_a.title()}",
    f"swapcase(): {string_a.swapcase()}",
    sep=",\n"
)

