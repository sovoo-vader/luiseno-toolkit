# File: app/consent.py
consent_registry = {}

def register_consent(doc_id, user, permission=True):
    consent_registry[doc_id] = {"user": user, "permission": permission}

def is_access_allowed(doc_id):
    return consent_registry.get(doc_id, {}).get("permission", False)
