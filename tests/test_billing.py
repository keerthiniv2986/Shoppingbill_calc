import pytest
from app.billing import BillingSystem

def test_calculate_total():
    billing = BillingSystem()
    assert billing.calculate_total(10.50, 4) == 42.00
    assert billing.calculate_total(0, 5) == 0.00
    
    with pytest.raises(ValueError):
        billing.calculate_total(-5, 2)