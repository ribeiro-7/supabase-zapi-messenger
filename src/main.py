import os
import sys

from dotenv import load_dotenv

from supabase_client import fetch_contacts

def get_required_environment_variable(name):
    value = os.getenv(name)

    if not value:
        raise ValueError(f"Variável de ambiente obrigatória não configurada: {name}")

    return value

def main():
    load_dotenv()

    try:
        supabase_url = get_required_environment_variable("SUPABASE_URL")
        supabase_key = get_required_environment_variable("SUPABASE_KEY")
        contacts = fetch_contacts(supabase_url, supabase_key)
    except ValueError as error:
        print(f"Erro de configuração: {error}", file=sys.stderr)
        return 1
    except Exception:
        print("Não foi possível consultar os contatos no Supabase.", file=sys.stderr)
        return 1

    if not contacts:
        print("Nenhum contato ativo encontrado.")
        return 0

    print(f"{len(contacts)} contato(s) ativo(s) encontrado(s):")

    for contact in contacts:
        print(f"- {contact['nome']}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
