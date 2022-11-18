import pytest
from account import *

def test_init():
    acc1 = account("Dio")
    assert acc1.getname() == "Dio"
    assert acc1.getbalance() == 0

def test_deposit():
    acc1 = account("Dio")
    acc1.deposit(50)
    assert acc1.getbalance() == 50

def test_withdraw():
    acc1 = account("Dio")
    acc1.deposit(250)
    acc1.withdraw(50)
    assert acc1.getbalance() == 200