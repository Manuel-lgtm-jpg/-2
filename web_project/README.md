# 在线问诊预约系统

基于 Flask 的在线问诊预约网站，支持预约提交、预约列表查看。

## 本地运行

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
python app.py
```

访问 http://localhost:5000

## 部署（免费公网）

- **Render**: 关联本仓库，Start Command 填 `python app.py`，即可获得 `xxx.onrender.com`
- **Hugging Face Spaces**: 选 Docker 模板，推送本仓库即可获得 `xxx.hf.space`
- 平台会自动 `pip install -r requirements.txt`，无需上传 `.venv`

## 项目结构

```
app.py                 # Flask 后端 + SQLite 存储
requirements.txt       # 依赖
Procfile               # 部署启动命令
templates/             # 页面模板
  index.html           # 预约表单页
  appointments.html    # 预约列表页
static/style.css       # 样式
```
