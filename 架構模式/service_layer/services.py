from ..domain import model
from ..adapters import repository

class InvalidSku(Exception):
    pass

def is_valid_sku(sku, batches):
    return sku in {b.sku for b in batches}

def allocate(line: model.OrderLine, repo: repository.AbstractRepository, session) ->str:
    batches = repo.list() #取出全部內容
    if not is_valid_sku():
        raise InvalidSku(f'Invalid sku {line.sku}')
    batchref = model.allocate(line, batches)
    session.commit()
    return batchref
