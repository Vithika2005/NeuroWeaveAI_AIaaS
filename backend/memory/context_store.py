context_buffer = []

def add_context(entry):
    context_buffer.append(entry)
    if len(context_buffer) > 5:
        context_buffer.pop(0)

def get_context():
    return "\n".join(context_buffer)
