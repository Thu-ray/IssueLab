"""测试 @mention 解析器"""

from issuelab.parser import has_agent_mentions, parse_agent_mentions


def test_parse_single_mention():
    """测试解析单个 @mention"""
    result = parse_agent_mentions("@moderator 请审核")
    assert result == ["moderator"]


def test_parse_multiple_mentions():
    """测试解析多个 @mention"""
    result = parse_agent_mentions("@moderator 审核，@reviewer_a 评审")
    assert result == ["moderator", "reviewer_a"]


def test_parse_unknown_mention_filtered():
    """未知 @mention 不应被识别为 agent"""
    result = parse_agent_mentions("@mod @reva @someone")
    assert result == []


def test_parse_uppercase_mention():
    """测试大写 @Mention 也应解析"""
    result = parse_agent_mentions("@MODERATOR 审核")
    assert result == ["moderator"]


def test_parse_mentions_with_digits_and_hyphen():
    """应支持包含数字和连字符的已注册 agent 名称"""
    result = parse_agent_mentions("@gqy20 请看下 @zhang2023-byte 也请参与")
    assert result == ["gqy20", "zhang2023-byte"]


def test_has_mentions():
    """测试检测是否有 @mention"""
    assert has_agent_mentions("请 @moderator 处理") is True
    assert has_agent_mentions("请 @gqy20 处理") is True
    assert has_agent_mentions("请 @zhang2023-byte 处理") is True
    assert has_agent_mentions("这是普通评论") is False
