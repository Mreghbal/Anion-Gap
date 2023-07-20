def calculate_anion_gap(sodium, chloride, bicarbonate):
    anion_gap = sodium - (chloride + bicarbonate)
    return anion_gap

# Prompt user for input values
sodium = float(input("Enter the value of sodium: "))
chloride = float(input("Enter the value of chloride: "))
bicarbonate = float(input("Enter the value of bicarbonate: "))

# Calculate anion gap
anion_gap = calculate_anion_gap(sodium, chloride, bicarbonate)

# Display the result
print("Anion Gap:", anion_gap)

