# Copyright (c) ACSONE SA/NV 2018
# Distributed under the MIT License (http://opensource.org/licenses/MIT).

from oca_github_bot.version_branch import is_main_branch_bot_branch, is_protected_branch


def test_is_main_branch_bot_branch():
    assert not is_main_branch_bot_branch("6.1")
    assert not is_main_branch_bot_branch("7.0")
    assert is_main_branch_bot_branch("8.0")
    assert is_main_branch_bot_branch("12.0")
    assert not is_main_branch_bot_branch("10.0-something")


def test_is_protected_branch():
    assert is_protected_branch("master")
    assert is_protected_branch("6.0")
    assert is_protected_branch("12.0")
    assert not is_protected_branch("10.0-something")
