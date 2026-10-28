
def status_lulus(nilai):
    if nilai > 60:
        return "Lulus"
    return "Tidak lulus"


print("Status 60:", status_lulus(60))
print("Status 75:", status_lulus(75))
