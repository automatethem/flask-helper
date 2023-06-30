

def base64_preprocess(inputs):
    for k in inputs.keys():
        v = inputs[k]
        if v and "base64," in v:
            base64_decoded = base64_decode(v)
            inputs[k] = base64_decoded
