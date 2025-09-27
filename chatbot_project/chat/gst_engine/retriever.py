def retrieve(query,model,index,chunks,top_k=5):
    query_vector=model.encode([query],convert_to_numpy=True)
    _,indices=index.search(query_vector,top_k)
    passages = []
    for i in indices[0]:
        surrounding = " ".join(chunks[max(0, i-1): i+2])  
        passages.append(surrounding)
    return passages
