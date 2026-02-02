# IssueLab

AI 辅助科研评审系统。基于 GitHub Issues + Claude Agent SDK。

## 使用

**@mention 并行触发**（推荐）：
```markdown
请 @Moderator 分诊，@ReviewerA 评审，@ReviewerB 找问题
```

**/command 顺序触发**：
```markdown
/review      # 完整评审流程
/summarize   # 汇总共识
/triage      # 仅 Moderator 分诊
/quiet       # 机器人静默
```

## 模板

| 模板 | 用途 |
|------|------|
| Paper | 论文讨论 |
| Proposal | 实验提案 |
| Result | 结果复盘 |
| Question | 技术问题 |

## 本地开发

```bash
uv sync
uv run python -m issuelab execute --issue 1 --agents moderator
```
