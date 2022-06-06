
import re
String = input("Enter your word: ")
Uppercase_Characters = re.findall(r"[A-Z]", String)
Lowercase_Characters = re.findall(r"[a-z]", String)
Numerical_Characters = re.findall(r"[0-9]", String)
Special_Characters = re.findall(r"[, .!@%$^&*]", String)
print("The number of uppercase characters is", len(Uppercase_Characters))
print("The number of lowercase characters is", len(Lowercase_Characters))
print("The number of numerical characters is", len(Numerical_Characters))
print("The number of special characters is", len(Special_Characters))



