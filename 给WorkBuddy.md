# 给 WorkBuddy：装到对方本机（全局）

你现在的任务是**给当前这台电脑安装提速**，不是写作业、不是改出厂程序。

不要只摘要。不要整文件覆盖用户已有设置。不要改、不要清空 `MEMORY.md`。不要动 `claw`、`sandbox`、token、apiKey。

## 必做

1. 若还没有本仓库：
   - 本机已有目录就用本地路径。
   - 否则优先镜像 clone（国内直连 GitHub 常失败）：  
     `git clone --depth 1 https://ghfast.top/https://github.com/anon-research-tools/workbuddy-speed-pack.git`  
     或下载 zip：`https://ghfast.top/https://github.com/anon-research-tools/workbuddy-speed-pack/archive/refs/heads/main.zip`  
     `ghfast.top` 失败则换 `gh-proxy.com`。
2. 进入仓库根目录，运行：`python3 scripts/install.py`
3. 脚本会：
   - 备份并**合并** `hard-settings.json` 到 `~/.workbuddy/settings.json`
   - 把 `rules/fast-default.md` 复制到 `~/.workbuddy/rules/` 和 `~/.codebuddy/rules/`
4. 回复只包括：备份路径、rules 路径、请用户**退出 WorkBuddy 并新开对话**。提醒用户自己关掉 Max、选用快模型。

用户若明确说「只要这个文件夹、不要改全局」，则不要跑安装脚本，只把本仓库当工作区打开即可。
