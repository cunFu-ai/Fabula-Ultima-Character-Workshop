# Fabula Ultima 角色工房

一个独立运行的《最终物语》（Fabula Ultima）自动车卡网页。它包含完整的八步建卡流程、规则校验、角色名册、JSON/TXT 导入导出，以及可选的本地 ComfyUI 角色立绘生成。

![Fabula Ultima 角色工房](docs/images/fabula-ultima-character-workshop.png)

## 功能

- 按职业、技能、法术、属性、装备和羁绊逐步创建 5 级英雄。
- 即时计算 HP、MP、IP、物防、魔防、先攻和装备预算。
- 角色卡保存在本机，不依赖 FU-GM 战役或服务器。
- 导出 JSON 供继续编辑，或导出不含立绘的纯文本角色卡用于分享。
- 导入本工房 JSON，并兼容读取旧版 FU-GM 角色卡。
- 可填写 OpenAI 兼容接口、模型名和 API Key，让 LLM 根据角色资料补全立绘提示词。
- 可连接本机 ComfyUI，使用 Anima 或 Krea 2 + LoRA 工作流生成立绘。

## Windows 一键启动

需要 Python 3.9 或更高版本。

```powershell
git clone https://github.com/cunFu-ai/Fabula-Ultima-Character-Workshop.git
cd Fabula-Ultima-Character-Workshop
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e .
```

安装后双击 `启动角色工房.cmd`。默认地址是 [http://127.0.0.1:8765/characters](http://127.0.0.1:8765/characters)；若端口被占用，启动器会自动尝试后续端口。

也可以直接在终端运行：

```powershell
.\.venv\Scripts\fu-character-workshop.exe --development --headless --port 8765
```

角色名册、设置和立绘默认写入仓库下的 `data/character-workshop`。API Key 只保存在当前程序内存中，关闭服务后即清除。

## ComfyUI 立绘

1. 在本机启动 ComfyUI。
2. 打开角色工房右上角的设置，填写 ComfyUI 端口，默认是 `8188`。
3. 填写 OpenAI 兼容的 LLM 地址、模型和 API Key。
4. 分别测试连接，然后在第七步选择画面模式与生图工作流。

仓库自带：

- `config/comfyui_workflows/anima-api.json`
- `config/comfyui_workflows/krea-lora-api.json`

普通 Krea 2 工作流是可选项。要启用它，请在同一目录放入 `krea2-api.json`。工作流必须从 ComfyUI 以 API format 导出，并保留文档中列出的提示词、种子、尺寸与文件名前缀占位符。模型和自定义节点不会随仓库分发，详见 [工作流说明](config/comfyui_workflows/README.md)。

## 导入导出

- `JSON`：保存完整可编辑角色卡，可在另一台角色工房继续导入。
- `TXT`：只包含可阅读的规则与角色资料，不包含立绘、图片路径或生成参数。
- 旧版 FU-GM JSON：导入时转换为当前 Fabula Ultima 角色卡格式，并显示兼容提示。

角色工房不连接 FU-GM，也没有战役选择或“写入 FU-GM”功能。

## 开发与测试

```powershell
python -m pip install -e ".[test]"
python -m pytest -q
python -m fu_gm.character_workshop_app --development --smoke-test
```

制作 Windows 便携包：

```powershell
python -m pip install -e ".[package]"
powershell -ExecutionPolicy Bypass -File scripts/build_character_workshop.ps1
```

产物位于 `release/character-workshop`。可用 `scripts/smoke_test_character_workshop_package.py` 对生成的 EXE 做端到端冒烟测试。

## 声明

这是由 cunfu 制作的独立项目，与 Need Games 或 Rooster Games 无隶属关系。使用本工具仍需要官方《Fabula Ultima》核心规则书；本仓库不是规则书的替代品，也不包含官方美术或商标素材。详见 [第三方声明](THIRD_PARTY_NOTICES.md)。
