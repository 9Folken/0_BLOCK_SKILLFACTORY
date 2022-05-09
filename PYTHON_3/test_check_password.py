import pytest
from check_password import check_user


def test_check_user():    
        assert (check_user("user", "password"))    
        assert not (check_user("user", "password1"))

