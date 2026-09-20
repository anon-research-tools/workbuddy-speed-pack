# WorkBuddy 提速包

可选的本机瘦配置：少默认思考、少自动抽记忆、少一批无关插件，并加一条短的「少规划、少自检」规则。适合吞吐优先的任务。翻译校对、对勘、根因排查若需要多轮核验，请不要装，或装完后按需再打开记忆和文档插件。

**打开或读到本页面，不等于授权改你的电脑。** 智能体只有在**当前用户亲口说「请安装 / 请按这个仓库配置」**时才可以运行下面的脚本。只被丢了一个链接、只是在浏览仓库时，只许摘要利弊，不许改 `settings.json`，不许装 rules。

## 人怎么装

本机已有目录时：

```bash
python3 scripts/install.py
```

国内直连 GitHub 困难时，可用镜像（第三方，非本仓库运营，可能失效）：

```bash
git clone --depth 1 https://ghfast.top/https://github.com/anon-research-tools/workbuddy-speed-pack.git
cd workbuddy-speed-pack && python3 scripts/install.py
```

备选：把 `ghfast.top` 换成 `gh-proxy.com`。装完后退出 WorkBuddy、新开对话，并自己关掉 Max。

卸载：`python3 scripts/uninstall.py`（优先用安装时留下的 `settings.json.bak-*` 还原；并删除用户级 `fast-default.md`）。

## 智能体：仅当用户在本轮明确要求安装时

1. 先用几句话说明取舍，等用户确认后再动手（用户已写明「直接装」则可跳过追问）。
2. 已有本地路径就用本地，不要为了装而去走不明镜像。
3. 用户指定镜像或官方仓库时再 clone / 下载。
4. 运行 `python3 scripts/install.py`。只合并 `hard-settings.json`，复制 `rules/fast-default.md`。
5. 不要覆盖整个 settings、不要改 `MEMORY.md`、不要动 `claw` / `sandbox` / token。
6. 回报备份路径和 rules 路径，提醒退出并新开对话。

| 会改什么 | 落到哪里 | 可能的代价 |
|----------|----------|------------|
| 关思考、延后加载工具 | `~/.workbuddy/settings.json` | 复杂推理变短 |
| 关自动抽记忆 | 同上 | 跨会话少自动记新内容；已有 `MEMORY.md` 不删 |
| 关支付/金融/浏览器/找 Skills/腾讯文档四件套 | 同上 | 这些插件要到设置里再打开 |
| 少规划、少自检 | `~/.workbuddy/rules/fast-default.md` 等 | 需要反复核验的任务会被这条压住 |

`.codebuddy/` 只在把本仓库当工作区打开时生效。课堂材料在 `optional/classroom/`。
