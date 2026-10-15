# 在线问诊预约网站 —— 腾讯云 CloudBase 云托管 部署指引

> 适用于：没有国际信用卡、想用国内平台、要公网地址给评委访问的同学。
> 前提：你已经有 GitHub 仓库（里面是 WebProject 的全部代码），且已在本地把本目录用 GitHub Desktop 推送过。
> 本目录已新增 `Dockerfile` 和 `.dockerignore`，**部署前请先把这两个新文件也推送到 GitHub**（见第 0 步）。

---

## 第 0 步：先把 Dockerfile / .dockerignore 推上 GitHub（重要）

CloudBase 要从 GitHub 拉代码构建镜像，必须包含 `Dockerfile`。

1. 打开 GitHub Desktop
2. 左侧应显示你的仓库有改动（新增了 `Dockerfile`、`.dockerignore`）
3. 下方写个说明，如「add Dockerfile for CloudBase」，点 **Commit to main**
4. 点 **Push origin** 推送到 GitHub

推送完成后才进行下面的注册部署。

---

## 第 1 步：注册腾讯云并实名

1. 打开 https://cloud.tencent.com
2. 右上角「注册」，用微信扫码或手机号注册
3. 按提示做**实名认证**（上传身份证，几分钟过）
4. 进入控制台后，按提示**绑定微信支付 / 支付宝**（只是验证，不会扣费；免费额度内不花钱）

---

## 第 2 步：开通 CloudBase 云托管

1. 控制台搜索「**云开发 CloudBase**」并进入
2. 开通服务 → 新建一个环境（选**按量计费 / 免费额度**档，名称随意，如 `clinic-env`）
3. 进入环境后，左侧菜单找「**云托管**」→ 点击开通

> 云托管是按容器跑的，正好用我们准备的 `Dockerfile`。

---

## 第 3 步：新建服务并关联 GitHub

1. 云托管里点「**新建服务**」
2. 服务名称：`clinic-appointment`（随意）
3. 选择「**从代码仓库导入**」→ 授权关联你的 **GitHub**
4. 选中你的网站仓库（WebProject）
5. 代码分支：`main`
6. 构建方式：选「**Dockerfile**」（会自动读取仓库里的 `Dockerfile`）
7. 服务端口：填 `5000`（和 Dockerfile 里的 EXPOSE 一致；CloudBase 会按需改映射）
8. 点「**保存并部署**」

---

## 第 4 步：等构建完成，拿到公网地址

1. 部署开始后，页面会显示构建日志（拉代码 → 装 Flask → 启动）
2. 看到日志出现 `Running on http://0.0.0.0:5000` 或状态变「**正常**」即成功
3. 在「服务详情」里找到**默认域名**，形如：
   ```
   https://xxx.ap-shanghai.run.tcloudbase.com
   ```
   这个就是你的**公网地址**，发给评委即可访问。

---

## 第 5 步：验证

1. 浏览器打开上面的公网地址 → 应看到「在线问诊预约系统」首页
2. 填一条预约提交 → 点「查看预约列表」能看到刚提交的数据
3. 演示前提前点开一次，确保服务是「唤醒」状态

---

## 常见问题

**Q：部署失败，日志报 `ModuleNotFoundError: flask`？**
A：说明没装依赖。确认 `requirements.txt` 已推上 GitHub，且构建方式选了 Dockerfile。

**Q：日志报 `app.py not found`？**
A：确认 GitHub 仓库根目录直接有 `app.py`（不要套多一层文件夹）。如果仓库根目录是 `web_project` 而不是 `WebProject`，把 Root/构建目录留空（默认根目录）即可。

**Q：免费额度会扣钱吗？**
A：小网站访问量极低，基本在免费额度内。只要不手动升级套餐，不会扣费。建议演示完可暂停服务以防万一。

**Q：数据会丢吗？**
A：云托管容器硬盘是临时的，重新部署后 SQLite 里的预约记录会清空（和 Render 一样）。演示时重新提交一条即可，不影响流程。

**Q：想改功能（加取消预约、登录等）？**
A：改完本地 `app.py` / 模板后，用 GitHub Desktop 重新 Commit + Push，CloudBase 可设置「提交后自动部署」，会自动重新构建上线。
