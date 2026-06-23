from supabase import create_client

MAX_CONTACTS = 3

def fetch_contacts(supabase_url, supabase_key):
    client = create_client(supabase_url, supabase_key)

    response = (
        client.table("contatos")
        .select("nome,telefone")
        .eq("ativo", True)
        .order("created_at")
        .limit(MAX_CONTACTS)
        .execute()
    )

    return response.data
