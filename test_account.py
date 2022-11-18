import pytest
from account import *
class Test:
    def setup_method(self):
        self.acc1 = Account("1 - Dio Moreno")

    def teardown_method(self):
        del self.acc1

    def test_init(self):
        assert self.acc1.get_name() == "1 - Dio Moreno"
        assert self.acc1.get_balance() == 0

    def test_deposit(self):
        assert self.acc1.deposit(100) == True
        assert self.acc1.get_balance() == 100
        assert self.acc1.deposit(-100) == False
        assert self.acc1.get_balance() == 100
        assert self.acc1.deposit(100.50) == True
        assert self.acc1.get_balance() == pytest.approx(200.50, abs=0.001)
        assert self.acc1.deposit(0) == False
        assert self.acc1.get_balance() == pytest.approx(200.50, abs=0.001)

    def test_withdraw(self):
        assert self.acc1.withdraw(100) == False
        assert self.acc1.get_balance() == 0
        assert self.acc1.withdraw(0) == False
        assert self.acc1.get_balance() == 0
        self.acc1.deposit(1000)
        assert self.acc1.withdraw(500.75) == True
        assert self.acc1.get_balance() == pytest.approx(499.25, abs = 0.001)
        assert self.acc1.withdraw(50) == True
        assert self.acc1.get_balance() == pytest.approx(449.25, abs=0.001)