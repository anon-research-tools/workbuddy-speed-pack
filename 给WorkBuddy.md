# 给智能体

只读到链接：列出 README 里的 A/B/C/D，各用一句话讲风险，等用户选。不要装，不要长篇克隆核实。

用户选了 B/C/D 之后，再取仓库并运行对应的：

- B → `python3 scripts/install.py thinking`
- C → `python3 scripts/install.py office`
- D → `python3 scripts/install.py full`

不动 `MEMORY.md`、`claw`、`sandbox`、token。
