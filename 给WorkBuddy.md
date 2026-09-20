# 给 WorkBuddy：装到对方本机（全局）

你现在的任务是**给当前这台电脑安装提速**，不是写作业、不是改出厂程序。

不要只摘要。不要整文件覆盖用户已有设置。不要改、不要清空 `MEMORY.md`。不要动 `claw`、`sandbox`、token、apiKey。

## 必做

1. 若还没有本仓库：先 clone 或下载，进入仓库根目录。
2. 运行：`python3 scripts/install.py`
3. 脚本会：
   - 备份并**合并** `hard-settings.json` 到 `~/.workbuddy/settings.json`（关思考、关自动记忆、关一批插件）
   - 把 `rules/fast-default.md` 复制到 `~/.workbuddy/rules/` 和 `~/.codebuddy/rules/`（`alwaysApply`，全局每轮灌入）
4. 回复只包括：备份路径、rules 路径、请用户**退出 WorkBuddy 并新开对话**。提醒用户自己关掉 Max、选用快模型。

用户若明确说「只要这个文件夹、不要改全局」，则不要跑安装脚本，只把本仓库当工作区打开即可。
