# 在线问诊预约网站 —— 用于腾讯云 CloudBase 云托管的镜像构建文件
# 基础镜像：Python 3.12 精简版
FROM python:3.12-slim

# 设置容器内工作目录
WORKDIR /app

# 先复制依赖清单并安装（利用 Docker 缓存，依赖不变时不会重复安装）
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制全部应用代码（app.py / templates / static 等）
COPY . .

# 声明端口（CloudBase 会通过环境变量 PORT 注入实际端口，app.py 已自动读取）
EXPOSE 5000

# 启动网站；CloudBase 会把外部请求转发到容器监听的端口
CMD ["python", "app.py"]
