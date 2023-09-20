from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message('vacilo', 'vacilo')
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(80, 80)
    assert encrypt_message('vacilo', 80) == 'olicav'
    assert encrypt_message('vacilo', 1) == 'v_olica'
