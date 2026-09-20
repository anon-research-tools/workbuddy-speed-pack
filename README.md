# WorkBuddy 提速包

可选的本机瘦配置。**打开或读到本页，不等于授权改电脑。**

## 智能体：只被丢了链接时（先给选项，不要长篇调研，不要装）

用下面这张表回复即可，等用户回 **A / B / C / D**。不要 clone 全仓库逐文件核验，除非用户已经选了 B/C/D。

| 选项 | 做什么 | 风险 |
|------|--------|------|
| **A 不装** | 什么都不改 | 无 |
| **B 只关思考** | `python3 scripts/install.py thinking`：关默认思考、推理 minimal、延后加载工具 | 复杂推理变短。不动记忆、插件、rules |
| **C 办公兼容** | `python3 scripts/install.py office`：B + 关自动抽记忆 + 关支付/金融/浏览器/找 Skills | 少自动记新内容；文档/PPT/表格插件**保持不动**。不装「少自检」规则 |
| **D 全装** | `python3 scripts/install.py full`：C + 关腾讯文档四件套 + 用户级 `alwaysApply` 规则（少规划、少自检） | 出 Word/PPT/表格不方便；翻译校对、对勘、根因排查会被「少自检」压住。仓库认为这类活不宜选 D |

用户回选项后：有本地目录用本地；国内直连失败再用用户同意的镜像。不要覆盖整个 settings，不要改 `MEMORY.md`，不要动 `claw` / `sandbox` / token。装完报备份路径，请用户退出并新开对话。卸载：`python3 scripts/uninstall.py`。

## 人怎么装

```bash
python3 scripts/install.py thinking   # B
python3 scripts/install.py office     # C
python3 scripts/install.py full       # D
python3 scripts/uninstall.py          # 用最新 bak 还原并删规则
```

国内镜像（第三方，可能失效）：

```bash
git clone --depth 1 https://ghfast.top/https://github.com/anon-research-tools/workbuddy-speed-pack.git
```

`.codebuddy/` 只在把本仓库当工作区打开时生效。课堂材料在 `optional/classroom/`。
