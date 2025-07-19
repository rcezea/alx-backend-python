#!/usr/bin/env python3
"""
Test Module for GitHubOrgClient
"""

import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized
from fixtures import TEST_PAYLOAD



class TestGithubOrgClient(unittest.TestCase):
    """ Test Class to unit test GithubOrgClient class methods """

    @parameterized.expand([
        'google',
        'abc'
    ])
    @patch('client.get_json')
    def test_org(self, org, mock):
        """ Test that GithubOrgClient.org returns correct payload and get_json is called with correct url """
        mock.return_value = {"payload": True}
        obj = GithubOrgClient(org)
        result = obj.org
        mock.assert_called_once_with('https://api.github.com/orgs/{}'.format(org))
        self.assertEqual(result, {"payload": True})

    def test_public_repos_url(self):
        """ method to unit-test GithubOrgClient._public_repos_url """
        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock) as mock:
            mock.return_value = {'repos_url': 'https://api.github.com/orgs/google/repos'}
            obj = GithubOrgClient('google')
            result = obj._public_repos_url
            self.assertEqual(result, mock.return_value['repos_url'])

    @patch('client.get_json')
    def test_public_repos(self, mock_get):
        """"""
        mock_get.return_value = [{"name": 'org-repo'}]

        with patch.object(GithubOrgClient, '_public_repos_url', new_callable=PropertyMock) as mock:
            mock.return_value = 'mocked_url'

            obj = GithubOrgClient('org')
            repo = obj.public_repos()

            self.assertEqual(repo[0], 'org-repo')

            mock.assert_called_once()
            mock_get.assert_called_once_with('mocked_url')

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_value):
        """"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected_value)
