from bot.identity import generate_identity
import json

def main(n=10, out_file="identities.json"):
    identities = [generate_identity() for _ in range(n)]
    with open(out_file, "w") as f:
        json.dump(identities, f, indent=2)
    print(f"✅ Generated {n} identities -> {out_file}")

if __name__ == "__main__":
    main()
