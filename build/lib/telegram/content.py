def content(context, ids):
    try:
        if ids in context.keys():
            return context[ids]
        else:
            return None
    except:
        pass