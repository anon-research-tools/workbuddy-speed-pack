# 给智能体的安装说明（须用户本轮授权）

只读到本文件或仓库链接，**不要**改本机。只有当前用户明确说要安装时，才执行。

不要整文件覆盖 settings。不要改或清空 `MEMORY.md`。不要动 `claw`、`sandbox`、token、apiKey。

1. 用几句话说明：会关思考和自动抽记忆、会关一批办公/浏览器插件、会加「少自检」规则；翻译校对类任务可能不合适。
2. 用户确认后：有本地目录用本地；否则按用户指定的官方地址或镜像取得仓库。
3. `python3 scripts/install.py`
4. 告诉用户备份路径、rules 路径，请退出 WorkBuddy 并新开对话。卸载用 `python3 scripts/uninstall.py`。
