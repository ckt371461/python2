import sys
sys.path.append('../../')
from service_layer import services 
from domain import model
from adapters.repository import FakeRepository
import pytest

"""用FakeSession偽造資料庫"""
class FakeSession():
    committed = False
    def commit(self):
        self.committed = True

def test_returns_allocation():
    line = model.OrderLine('o1', 'COMPLICATED-LAMP', 10)
    batch = model.Batch('b1', 'COMPLICATED-LAMP', 100, eta=None)
    repo = FakeRepository([batch])

    result = services.allocate(line, repo, FakeSession())
    assert result == 'b1'

def test_error_for_invalid_sku():
    line = model.OrderLine('o1', 'COMPLICATED-LAMP', 10)
    batch = model.Batch('b1', 'AREALSKU', 100, eta=None)
    repo = FakeRepository([batch])

    with pytest.raises(services.InvalidSku, match='Invalid sku NONEXISTENTSKU'):
        services.allocate(line, repo, FakeSession())
    
def test_commits():
    line = model.OrderLine('o1', 'OMINOUS-MIRROR', 10)
    batch = model.Batch('b1', 'OMINOUS-MIRROR', 100, eta=None)
    repo = FakeRepository([batch])
    session = FakeSession

    services.allocate(line, repo, session)
    assert session.commited is True     
