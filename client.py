import requests
import sys

# input utente
server_ip = input("Indirizzo IP del server: ").strip()
SERVER = f"http://{server_ip}:5000"

concorrente = input("Nome concorrente: ").strip()

# richiesta domanda
try:
    r = requests.get(f"{SERVER}/question", timeout=5)
except Exception as e:
    print("❌ Errore: server non raggiungibile")
    sys.exit(1)

if r.status_code != 200:
    print("❌ Errore nella richiesta della domanda")
    sys.exit(1)

try:
    q = r.json()
except Exception:
    print("❌ Risposta non valida dal server")
    sys.exit(1)

print("\nDOMANDA:")
print(q["text"])
for i, opt in enumerate(q["options"]):
    print(f"{i}) {opt}")

# risposta concorrente
try:
    answer = int(input("Risposta (0-3): ").strip())
except ValueError:
    print("❌ Risposta non valida")
    sys.exit(1)

# invio risposta
try:
    r = requests.post(
        f"{SERVER}/answer",
        json={
            "student": concorrente,   # chiave REST invariata
            "answer": answer
        },
        timeout=5
    )
except Exception:
    print("❌ Errore di comunicazione con il server")
    sys.exit(1)

# interpretazione risultato
try:
    result = r.json().get("result")
except Exception:
    print("❌ Risposta non valida dal server")
    sys.exit(1)

print("\nRISULTATO:")

if result == "win":
    print("🎉 HAI VINTO! Sei il primo concorrente corretto.")
elif result == "correct":
    print("✅ Risposta corretta, ma non sei il primo.")
elif result == "wrong":
    print("❌ Risposta sbagliata.")
elif result == "too_late":
    print("⏱️ Troppo tardi, un altro concorrente ha già vinto.")
elif result == "already_answered":
    print("⚠️ Hai già risposto.")
else:
    print("⚠️ Esito sconosciuto:", result)