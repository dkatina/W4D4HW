
def gimmebook(book_id, a_list):
    return (list(filter(lambda book: book['id']==book_id, a_list))[0])