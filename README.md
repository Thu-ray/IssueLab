# IssueLab

AI 辅助科研评审系统。

## 快速开始

```bash
# 克隆仓库
git clone https://github.com/gqy20/IssueLab.git
cd IssueLab

# 安装 uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# 同步依赖
uv sync
```

## 使用方法

**@mention 并行触发**（推荐）：
```markdown
请 @Moderator 分诊，@ReviewerA 评审，@ReviewerB 找问题
```

**/command 顺序触发**：
```markdown
/review
```

## 文档

- [MVP 方案](docs/MVP.md)

## 许可证

MIT
