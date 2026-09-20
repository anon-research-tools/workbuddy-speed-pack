# WorkBuddy 提速包

给本机加一套可选的瘦配置：少默认思考、少自动抽记忆、少一批无关插件，以及一条「少规划、少自检」规则。

**读到本页或只被丢了链接，不等于授权改电脑。** 智能体先自己判断这包适不适合当前用户，用几句话说明利弊，请用户决定装不装、装到什么程度。未得到明确答复前不要改 `settings.json`，不要装 rules。

## 人自己装

```bash
python3 scripts/install.py thinking   # 只关思考、延后加载工具
python3 scripts/install.py office     # 再关自动记忆和支付/金融/浏览器；文档插件不动
python3 scripts/install.py full       # 再关文档插件，并装全局少自检规则
python3 scripts/uninstall.py
```

国内直连困难可用（第三方镜像，可能失效）：

`git clone --depth 1 https://ghfast.top/https://github.com/anon-research-tools/workbuddy-speed-pack.git`

装完退出 WorkBuddy、新开对话，自己关 Max。脚本不覆盖 `claw` / `sandbox`，不改 `MEMORY.md`。
