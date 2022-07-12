import os

import pytest
import python_freeipa
from dotenv import load_dotenv
from python_freeipa import exceptions


class TestFreeIPAConnection:
    @pytest.fixture(autouse=True)
    def env_setup(self):
        load_dotenv()

    def test_environment_variable_setup(self):
        user_name = os.environ.get("IPA_ADMIN_USER")
        user_password = os.environ.get("IPA_ADMIN_PASSWORD")
        ipa_url = os.environ.get("IPA_URL")

        assert user_name is not None
        assert user_password is not None
        assert ipa_url is not None

    def test_successful_user_login(self):
        user_name = os.environ.get("IPA_ADMIN_USER")
        user_password = os.environ.get("IPA_ADMIN_PASSWORD")
        ipa_url = os.environ.get("IPA_URL")
        client = python_freeipa.ClientMeta(host=ipa_url, dns_discovery=False)

        try:
            client.login(user_name, user_password)
            assert client.user_find("testuser")["count"] == 1
        finally:
            client.logout()

    def test_failed_user_login_with_wrong_password(self):
        user_name = "testuser"
        user_password = "bogus_password"
        ipa_url = os.environ.get("IPA_URL")
        client = python_freeipa.ClientMeta(host=ipa_url, dns_discovery=False)

        with pytest.raises(exceptions.Unauthorized):
            try:
                client.login(user_name, user_password)
            finally:
                client.logout()

    def test_failed_user_login_with_wrong_username_and_password(self):
        user_name = "non_existent_user"
        user_password = "bogus_password"
        ipa_url = os.environ.get("IPA_URL")
        client = python_freeipa.ClientMeta(host=ipa_url, dns_discovery=False)

        with pytest.raises(exceptions.Unauthorized):
            try:
                client.login(user_name, user_password)
            finally:
                client.logout()
