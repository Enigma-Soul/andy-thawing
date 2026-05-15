# andy-thawing 刘德华解冻倒计时
## 预览
![light](https://raw.githubusercontent.com/Enigma-Soul/andy-thawing/output/light.png#gh-light-mode-only)
![dark](https://raw.githubusercontent.com/Enigma-Soul/andy-thawing/output/dark.png#gh-dark-mode-only)

## 使用方法
建议:Fork后在自己仓库内进行

```markdown
![light](https://raw.githubusercontent.com/<Your Name>/andy-thawing/output/light.png#gh-light-mode-only)
![dark](https://raw.githubusercontent.com/<Your Name>/andy-thawing/output/dark.png#gh-dark-mode-only)
```

### 本地开发
需要安装 [uv](https://docs.astral.sh/uv/)

```bash
uv sync
uv run python -m andy_thawing
```

## 文件说明
```markdown
andy-thawing/
├── pyproject.toml           # uv 项目配置
├── src/
│   └── andy_thawing/        # Python 包
│       ├── __init__.py      # 版本号
│       ├── __main__.py      # 入口点
│       ├── config.py        # 集中配置（日期、尺寸等）
│       ├── resources.py     # 资源路径解析
│       ├── ice.py           # 冰块效果
│       ├── counting.py      # 倒计时计算与生成
│       └── ew2_count.py     # 流浪地球风格渲染
├── resources/               # 静态资源
│   ├── fonts/               # 字体文件
│   └── img/                 # 图片素材
├── .github/workflows/
│   ├── build.yml            # 合并到 main 自动打包
│   └── daily.yml            # 每天定时生成图片
└── README.md
```
