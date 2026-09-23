gekochte_stuks = int(input())
kostprijs_stuk = float(input())
barcodes_nodig = int(input())
mijlen = int(input())

uitgegeven = float(gekochte_stuks * kostprijs_stuk)
flyer_mijlen = int(mijlen * (gekochte_stuks // barcodes_nodig))

print(f"Phillips spendeerde ${uitgegeven} voor {flyer_mijlen} frequent flyer mijlen.")
