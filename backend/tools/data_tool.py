from memory.context_store import add_context, get_context

def get_context():
    return context_store.get_recent()
def store_context(data):
    add_context(str(data))


