import os
import sys

from dotenv import load_dotenv

from supabase_client import fetch_contacts
from zapi_client import send_text


def get_required_environment_variable(name):
    value = os.getenv(name)

    if not value:
        raise ValueError(f"Variável de ambiente obrigatória não configurada: {name}")

    return value


def build_message(name):
    return f"Olá, {name} tudo bem com você?"


def mask_phone(phone):
    return f"final {phone[-4:]}"


def send_messages(contacts):
    try:
        instance_id = get_required_environment_variable("ZAPI_INSTANCE_ID")
        instance_token = get_required_environment_variable("ZAPI_INSTANCE_TOKEN")
        client_token = get_required_environment_variable("ZAPI_CLIENT_TOKEN")
    except ValueError as error:
        print(f"Erro de configuração: {error}", file=sys.stderr)
        return 1

    successful_sends = 0
    failed_sends = 0

    for contact in contacts:
        message = build_message(contact["nome"])
        masked_phone = mask_phone(contact["telefone"])

        try:
            send_text(
                instance_id,
                instance_token,
                client_token,
                contact["telefone"],
                message,
            )
        except Exception:
            failed_sends += 1
            print(
                f"Falha ao enviar para {contact['nome']} ({masked_phone}).",
                file=sys.stderr,
            )
        else:
            successful_sends += 1
            print(f"Mensagem enviada para {contact['nome']} ({masked_phone}).")

    print(
        f"Envios concluídos: {successful_sends} sucesso(s), "
        f"{failed_sends} falha(s)."
    )

    return 1 if failed_sends else 0


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

    return send_messages(contacts)


if __name__ == "__main__":
    raise SystemExit(main())
