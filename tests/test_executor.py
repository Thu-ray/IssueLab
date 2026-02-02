"""测试并行执行器"""
import pytest
from unittest.mock import patch, MagicMock
from issuelab.executor import load_prompt


def test_load_prompt():
    """测试加载提示词"""
    # prompts 目录不存在时返回空字符串
    result = load_prompt("nonexistent")
    assert result == ""


def test_load_prompt_known_agent():
    """测试加载已知代理的提示词（目录不存在时返回空）"""
    result = load_prompt("moderator")
    # prompts 目录不存在，预期返回空
    assert result == ""
