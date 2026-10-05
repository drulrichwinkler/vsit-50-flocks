# VSIT-50 – Möwenschwärme

Übungsmaterial zur Vorlesung „Mutationen in Distributed Systems“: das Flock-Quiz, seine Behebung ohne Mutation und als Ausbau Schwärme mit Id und Version.
Die Übung ist unbewertet.

1. Repository in GitHub Codespaces oder lokal in VS Code als Devcontainer öffnen
   (Python 3.12, Pakete aus `.devcontainer/requirements.txt` werden automatisch installiert).
2. Das Quiz starten: `python flock.py` – vorher im Kopf rechnen.
3. `erkunden.ipynb` öffnen und der Reihe nach ausführen; die Aufgaben stehen zwischen den Abschnitten.
4. Die Tests sind die Spezifikation und anfangs rot: `pytest tests/test_flock.py`,
   für den Ausbau `pytest tests/test_flock_ids.py`.
